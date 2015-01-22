# Rob Hackman Lab 2 CMPUT 410
# Code taken from http://www.binarytides.com/python-socket-programming-tutorial/

import socket
import sys
from thread import *
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
#Start listening on socket
s.listen(10)
print 'Socket now listening'


def clientthread(conn):
    while True:
        data = conn.recv(1024)
        if (ord(str(data).strip()[0]) == 27):
            reply = "OMG YOU HIT ESCAPE GOODBYE\r\n"
            conn.sendall(reply)
            break
        reply = str(data).strip() + " Rob Hackman\r\n"
        if not data:
            break
     
        conn.sendall(reply)
    conn.close()
    
while 1:
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])

    start_new_thread(clientthread ,(conn,))
 
s.close()