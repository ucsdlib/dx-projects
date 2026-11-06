#!/usr/bin/env python3
"""Fetch UC San Diego databases A-Z assets from the Springshare API."""

import argparse
import json
import pathlib
import sys
import urllib.error
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
TOKEN_URL = "https://lgapi-us.libapps.com/1.2/oauth/token"
AZ_URL = "https://lgapi-us.libapps.com/1.2/az"
EXPAND = "subjects,friendly_url,az_types,az_props,az_flags"


def load_env(path):
    """Read a simple KEY=VALUE .env file."""
    env = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            raise ValueError("Invalid .env line: {!r}".format(raw_line))
        key, value = line.split("=", 1)
        env[key.strip()] = value.strip()
    return env


def get_token(client_id, client_secret, timeout):
    """Exchange client credentials for a short-lived access token."""
    data = urllib.parse.urlencode(
        {
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": "client_credentials",
        }
    ).encode("utf-8")
    request = urllib.request.Request(
        TOKEN_URL,
        data=data,
        headers={"Accept": "application/json"},
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        payload = json.load(response)

    token = payload.get("access_token")
    if not token:
        raise RuntimeError("Springshare did not return an access token.")
    return token


def fetch_assets(token, timeout):
    """Fetch all A-Z assets with the metadata expansions needed for reuse."""
    query = urllib.parse.urlencode({"expand": EXPAND})
    request = urllib.request.Request(
        "{}?{}".format(AZ_URL, query),
        headers={
            "Accept": "application/json",
            "Authorization": "Bearer {}".format(token),
        },
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.load(response)


def write_json(path, assets):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(assets, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def print_summary(assets):
    hidden = 0
    popular = 0
    featured_subject_matches = 0
    with_subjects = 0
    with_types = 0
    updated_2026 = 0
    for asset in assets:
        meta = asset.get("meta", {})
        if str(asset.get("enable_hidden", meta.get("enable_hidden", ""))) in (
            "1",
            "1.0",
        ):
            hidden += 1
        try:
            if int(float(meta.get("enable_popular", 0))):
                popular += 1
        except (TypeError, ValueError):
            pass
        if asset.get("subjects"):
            with_subjects += 1
        if any(subject.get("featured") == "1" for subject in asset.get("subjects", [])):
            featured_subject_matches += 1
        if (asset.get("updated") or "").startswith("2026"):
            updated_2026 += 1
        if asset.get("az_types"):
            with_types += 1

    print("Unique IDs: {}".format(len({asset.get("id") for asset in assets})))
    print("Visible: {}".format(len(assets) - hidden))
    print("Hidden: {}".format(hidden))
    print("Popular/Best Bets: {}".format(popular))
    print("Featured subject matches: {}".format(featured_subject_matches))
    print("With subjects: {}".format(with_subjects))
    print("With types: {}".format(with_types))
    print("Updated in 2026: {}".format(updated_2026))


def main():
    parser = argparse.ArgumentParser(
        description="Fetch UC San Diego databases A-Z assets from Springshare."
    )
    parser.add_argument(
        "--output",
        default="temp/az_database_list_api.json",
        help="Output JSON path, relative to the uc-library-search skill directory.",
    )
    parser.add_argument("--timeout", type=int, default=60)
    args = parser.parse_args()

    env_path = ROOT / ".env"
    if not env_path.exists():
        raise FileNotFoundError(
            "Missing {}. Add LIBAPPS_CLIENT_ID and LIBAPPS_CLIENT_SECRET.".format(env_path)
        )

    env = load_env(env_path)
    client_id = env.get("LIBAPPS_CLIENT_ID")
    client_secret = env.get("LIBAPPS_CLIENT_SECRET")
    if not client_id or not client_secret:
        raise ValueError(
            "Set LIBAPPS_CLIENT_ID and LIBAPPS_CLIENT_SECRET in {}.".format(env_path)
        )

    token = get_token(client_id, client_secret, args.timeout)
    assets = fetch_assets(token, args.timeout)
    if not isinstance(assets, list):
        raise RuntimeError("Expected a JSON array of A-Z assets.")

    write_json(ROOT / args.output, assets)
    print("Saved {} assets to {}".format(len(assets), ROOT / args.output))
    print_summary(assets)


if __name__ == "__main__":
    try:
        main()
    except (OSError, RuntimeError, ValueError, json.JSONDecodeError) as exc:
        print("ERROR: {}".format(exc), file=sys.stderr)
        sys.exit(1)
