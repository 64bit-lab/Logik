from http.server import BaseHTTPRequestHandler, HTTPServer


class LogikAPIRequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self, code=200):
        self.send_response(code)
        self.send_header("Content-Type", "text/tab-separated-values")
        self.end_headers()

        def do_HEAD(self):
            self._set_headers()

    def do_GET(self):
        self._set_headers(400)
        self.wfile.write(
            b'<h1>Unacceptable input</h1><iframe src="https://giphy.com/embed/QUaqJRizED5NC" width="480" height="279" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/adventure-time-lemongrab-unacceptable-QUaqJRizED5NC">via GIPHY</a></p>'
        )

    def do_POST(self):
        if "Content-Length" in self.headers:
            content_length = int(self.headers['Content-Length'])
        else:
            content_length = 0
        post_data = self.rfile.read(content_length)

        self.send_response(200)
        self.wfile.write(b"Input:\n" + post_data)


def run(server_class=HTTPServer, handler_class=LogikAPIRequestHandler,
        port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print("Starting server on port " + str(port))
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
