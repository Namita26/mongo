from app import app as application


if __name__ == "__main__":
    application.run()
"""
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return bytearray("", "utf-8")
"""
