import sys
import os.path
import posixpath
import socket
import readline
from select import select

# HACK - python doesn't include a binding to rl_callback_read_char
import readline
import ctypes

rl_lib = ctypes.cdll.LoadLibrary("libreadline.so")

readline.callback_handler_remove = rl_lib.rl_callback_handler_remove
readline.callback_read_char = rl_lib.rl_callback_read_char

# the callback needs special treatment:
rlcallbackfunctype = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_char_p)

def setcallbackfunc(prompt, thefunc):
    rl_lib.rl_callback_handler_install(prompt, rlcallbackfunctype(thefunc))

readline.callback_handler_install = setcallbackfunc
# ENDHACK

ROOT = os.path.abspath(os.path.dirname(__file__))
PROMPT = 'fics> '

def erase_prompt():
    print(chr(8)*len(PROMPT))

def print_prompt():
    readline.callback_handler_remove()
    setcallbackfunc(PROMPT, process_input)

def process_input(input):
    input = input.strip()
    if not len(input):
        requests.append('\r\n')

    erase_prompt()
    requests.append(input)
    print_prompt()

print_prompt()

requests = []

fics = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#fics.connect(('freechess.org', 5000))

import bottle

@bottle.route('/')
def hello():
    return bottle.template('index')

@bottle.route('/static/pieces/:piece')
def static(piece):
    return bottle.static_file(piece + '.gif', root=ROOT + '/static/pieces')

@bottle.route('/static/:filename')
def static(filename):
    return bottle.static_file(filename, root=ROOT + '/static')

from wsgiref.simple_server import make_server

server = make_server('', 8000, bottle.default_app())

while True:
    #r, w, x = select([sys.stdin, fics, server.socket], [fics, server.socket], [])
    r, w, x = select([sys.stdin, server], [server], [])

    #if fics in w:
        #for request in requests:
            #fics.send(request + '\r\n')
        #requests = []

    #if fics in r:
        #erase_prompt()
        #print fics.recv(4096)
        #print_prompt()

    if sys.stdin in r:
        readline.callback_read_char()

    if server in r:
        server._handle_request_noblock()
