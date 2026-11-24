import json
import logging
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

SERVICE = os.getenv("SERVICE", "claims-demo")
ENVIRONMENT = os.getenv("ENVIRONMENT", "lab")
VERSION = os.getenv("VERSION", "1.0.0")
PORT = int(os.getenv("PORT", "8080"))

logging.basicConfig(level=logging.INFO, format="%(message)s")


def write_log(level, message, request_id=None, path="/"):
    log_entry = {
        "timestamp": __import__("datetime").datetime.now().astimezone().isoformat(),
        "level": level,
        "service": SERVICE,
        "environment": ENVIRONMENT,
        "version": VERSION,
        "request_id": request_id,
        "path": path,
        "message": message,
    }
    logging.info(json.dumps(log_entry))


class RequestHandler(BaseHTTPRequestHandler):

    def send_json(self, status_code, data):
        response = json.dumps(data).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)

    def do_GET(self):
        parsed_url = urlparse(self.path)

        if parsed_url.path == "/health":
            self.send_json(200, {"status": "healthy", "service": SERVICE})
            return

        if parsed_url.path == "/generate-log":
            query = parse_qs(parsed_url.query)
            request_id = query.get("request_id", ["missing-request-id"])[0]

            write_log(
                "INFO",
                "Use Case 18 known log message",
                request_id,
                parsed_url.path,
            )

            self.send_json(
                200,
                {
                    "status": "logged",
                    "request_id": request_id,
                    "service": SERVICE,
                },
            )
            return

        self.send_json(404, {"error": "not found"})

    def log_message(self, format, *args):
        return


if __name__ == "__main__":
    write_log("INFO", "Use Case 18 application started", "startup", "/")
    try:
        HTTPServer(("0.0.0.0", PORT), RequestHandler).serve_forever()
    except KeyboardInterrupt:
        pass
