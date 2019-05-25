from wsgiref.simple_server import make_server
from cgi import parse_qs, escape
def simple_app(environ, start_response):
    """Simplest possible application object"""
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return [bytes("Hello world!\n", 'utf-8')]


def param_app(environ, start_response):
    status = '200 OK'
    responce_headers = [('Content-type', 'text/plain')]
    d = parse_qs(environ['QUERY_STRING'])
    start_response(status, responce_headers)
    ans = "Hello world!\n" + str(d)
    return [bytes(ans, 'utf-8')]


