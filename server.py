import os,sys
from SimpleHTTPServer import BaseHTTPServer,SimpleHTTPRequestHandler

webdir='.'
port = 80 
if len(sys.argv) > 1: webdir = sys.argv[1] 
if len(sys.argv) > 2: port = int(sys.argv[2]) 
print('webdir "%s", port %s' % (webdir, port))
os.chdir(webdir) # run in HTML root dir
srvraddr = ('', port) # my hostname, portnumber
srvrobj =BaseHTTPServer.HTTPServer(srvraddr, SimpleHTTPRequestHandler)
srvrobj.serve_forever()
