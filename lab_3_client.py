# -*- coding: latin-1 -*-

import socket   #for sockets
import sys  #for exit

 
# Lager dgram udp socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()
 
host = 'localhost';
port = 8888;
 
 
while(1) :
    msg = raw_input('Enter message to send : ')
     
    try :
        #Sett string
        s.sendto(msg, (host, port))
         
        # motta data fra client(data, addr)
        d = s.recvfrom(1024)
        msg_send = d[0]
        addr = d[1]
        
        print msg_send
        
        #print ' '.join(format(ord(x), 'b') for x in reply)
    except socket.error, msg:
        sys.exit()
