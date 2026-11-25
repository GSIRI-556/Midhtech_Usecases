import json
import logging
import os
import time
from collections import Counter
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

SERVICE = os.getenv("SERVICE", "claims-demo")
ENVIRONMENT = os.getenv("ENVIRONMENT", "usecase19")
VERSION = os.getenv("VERSION", "1.0.0")
PORT = int(os.getenv("PORT", "8080"))

START_TIME = time.time()
REQUESTS = Counter()
SERVER_ERRORS = 0

logging.basicConfig(level=logging.INFO, format="%(message)s")


def write_log(level, message, request_id=None, path="/"):
    log_entry = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
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

    def send_json(self, status_code, data, metric_path=None):
        global SERVER_ERRORS

        if metric_path is not None:
            REQUESTS[(metric_path, str(status_code))] += 1
            if status_code >= 500:
                SERVER_ERRORS += 1

        response = json.dumps(data).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)

    def do_GET(self):
        parsed_url = urlparse(self.path)

        if parsed_url.path == "/metrics":
            lines = [
                "# HELP claims_demo_http_requests_total Total HTTP requests",
                "# TYPE claims_demo_http_requests_total counter",
            ]

            for (path, status), count in sorted(REQUESTS.items()):
                lines.append(
                    f'claims_demo_http_requests_total{{path="{path}",status="{status}"}} {count}'
                )

            lines.extend([
                "# HELP claims_demo_http_server_errors_total Total HTTP 5xx responses",
                "# TYPE claims_demo_http_server_errors_total counter",
                f"claims_demo_http_server_errors_total {SERVER_ERRORS}",
                "# HELP claims_demo_start_time_seconds Application start time",
                "# TYPE claims_demo_start_time_seconds gauge",
                f"claims_demo_start_time_seconds {START_TIME}",
            ])

            response = ("\n".join(lines) + "\n").encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; version=0.0.4")
            self.send_header("Content-Length", str(len(response)))
            self.end_headers()
            self.wfile.write(response)
            return

        if parsed_url.path == "/health":
            self.send_json(
                200,
                {"status": "healthy", "service": SERVICE},
                "/health",
            )
            return

        if parsed_url.path == "/generate-log":
            query = parse_qs(parsed_url.query)
            request_id = query.get("request_id", ["missing-request-id"])[0]

            write_log(
                "INFO",
                "Use Case 19 known log message",
                request_id,
                "/generate-log",
            )

            self.send_json(
                200,
                {
                    "status": "logged",
                    "request_id": request_id,
                    "service": SERVICE,
                },
                "/generate-log",
            )
            return

        self.send_json(404, {"error": "not found"}, "unmatched")

    def log_message(self, format, *args):
        return


if __name__ == "__main__":
    write_log("INFO", "Use Case 19 application started", "startup", "/")
    HTTPServer(("0.0.0.0", PORT), RequestHandler).serve_forever()
