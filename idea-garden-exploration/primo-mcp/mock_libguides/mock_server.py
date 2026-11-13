import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

SAMPLE = Path(__file__).parent / "sample_az.json"


class MockLibGuides(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/1.2/oauth/token":
            return self.reply(404, {"error": "Not found"})
        form = self.rfile.read(int(self.headers.get("Content-Length", 0))).decode()
        if "client_id=mock-id" in form and "client_secret=mock-secret" in form:
            return self.reply(200, {"access_token": "mock-token", "token_type": "Bearer",
                                    "expires_in": 3600})
        self.reply(401, {"error": "invalid_client"})

    def do_GET(self):
        if self.path.split("?")[0] != "/1.2/az":
            return self.reply(404, {"error": "Not found"})
        if self.headers.get("Authorization") != "Bearer mock-token":
            return self.reply(401, {"error": "unauthorized"})
        self.reply(200, json.loads(SAMPLE.read_text(encoding="utf-8")))

    def reply(self, status, body):
        payload = json.dumps(body).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)


if __name__ == "__main__":
    print("Mock LibGuides at http://127.0.0.1:8002  (Ctrl+C to stop)")
    HTTPServer(("127.0.0.1", 8002), MockLibGuides).serve_forever()