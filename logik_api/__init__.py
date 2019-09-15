from http.server import BaseHTTPRequestHandler, HTTPServer
from io import StringIO
import logik


class LogikAPIRequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self, code=200, content_type="text/tab-separated-values"):
        self.send_response(code)
        self.send_header("Content-Type", "text/tab-separated-values")
        self.end_headers()

    def _evaluate(self, ast):
        var_list = logik.get_vars(ast)
        envs, tab = logik.make_env(var_list)

        if len(var_list) > 0:
            return "text/tab-separated-values", '\n'.join(
                ['\t'.join([*var_list, 'resultat'])] + [
                    '\t'.join(
                        str(x) for x in (*tab[i], logik.evaluate(ast, env)))
                    for i, env in enumerate(envs)
                ]) + '\n'
        else:
            return "text/text", f"Value: {logik.evaluate(ast, {})}\n"

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
        post_data = self.rfile.read(content_length).decode("utf-8")
        seq = logik.Seq(list(logik.lex(post_data)))
        ast = logik.parse(seq)
        content_type, data = self._evaluate(ast)
        self._set_headers(content_type=content_type)
        self.wfile.write(bytes(data, "utf-8"))


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
