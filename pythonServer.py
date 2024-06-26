#!/usr/bin/env python

# Attribution: https://stackoverflow.com/questions/21956683/enable-access-control-on-simple-http-server

# Python 3
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler
from http.server import test as test_orig


def test(*args):
    test_orig(*args, port=int(sys.argv[1]) if len(sys.argv) > 1 else 8000)


class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        SimpleHTTPRequestHandler.end_headers(self)


if __name__ == "__main__":
    test(CORSRequestHandler, HTTPServer)
