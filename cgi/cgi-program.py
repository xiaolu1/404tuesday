#!/usr/bin/env python

from __future__ import print_function

import sys, os, cgi

print("Blah!", file = sys.stderr)

#print("HTTP/1.0 302 Found")
#print("Location: http://google.com/")
#print("")
print("Content-type: text/html")
#text/plain
print("")
#print("Hello, this is the CGI script!")
#print("I am process %i" % os.getpid())
print("<HTML><BODY><FORM method='POST'><INPUT name='x'></FORM></BODY></HTML>")

#print(os.environ)
print("")
form = cgi.FieldStorage()
print(form.getvalue("x"))

