import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

SAMPLE = Path(__file__).parent / "sample_search.json"
MOCK_KEY = "mock-key-123"


class MockPrimo(BaseHTTPRequestHandler):
    def do_GET(self):
        url = urlparse(self.path)
        params = parse_qs(url.query)
        if url.path != "/primo/v1/search":
            return self.reply(404, {"error": "Not found"})

        header_key = self.headers.get("Authorization", "").removeprefix("apikey ")
        key = params.get("apikey", [""])[0] or header_key
        if key != MOCK_KEY:
            return self.reply(401, {"errorsExist": True, "error": "Invalid API key"})

        for name in ("vid", "tab", "scope", "q"):
            if name not in params:
                return self.reply(400, {"error": f"Missing parameter:{name}"})

        if "toomany" in params["q"][0]:  # lets you practise a 429
            return self.reply(429, {"errorCode": "PER_SECOND_THRESHOLD"})

        data = json.loads(SAMPLE.read_text(encoding="utf-8"))
        limit = int(params.get("limit", ["10"])[0])
        data["docs"] = data["docs"][:limit]
        self.reply(200, data)

    def reply(self, status, body):
        payload = json.dumps(body).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)


if __name__ == "__main__":
    print("Mock Primo at http://127.0.0.1:8001  (Ctrl+C to stop)")
    HTTPServer(("127.0.0.1", 8001), MockPrimo).serve_forever()