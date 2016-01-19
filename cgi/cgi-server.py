#!/usr/bin/env python
#Copyright by Nick Zarczynski. I probably don't have permission to post this on github 
# but I am going to anyway hope Nick Zarczynski do not sue me.
#https://pointlessprogramming.wordpress.com/2011/02/13/python-cgi-tutorial-1/
#Retrieved 2016-01-19

import BaseHTTPServer
import CGIHTTPServer
import cgitb; cgitb.enable()  ## This line enables CGI error reporting
 
server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler
server_address = ("", 8000)
handler.cgi_directories = ["/"]
 
httpd = server(server_address, handler)
httpd.serve_forever()
