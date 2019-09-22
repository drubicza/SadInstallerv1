import base64, zlib, marshal, sys, os, socket, random, signal

W  = '\x1b[1;37m'
RR = '\x1b[1;37m\x1b[31m'
O  = '\x1b[33m'
B  = '\x1b[34m'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(('8.8.8.8', 80))
print W + '                      [+]' + B + ' YOUR IP : ' + RR + sock.getsockname()[0] + W + ' [+]'
sys.exit()
