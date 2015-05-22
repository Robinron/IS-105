# -*- coding: utf-8 -*-

import socket
import sys
import lab2
 
 gruppe = {  'student1': 'Robin Amir Rondestvedt Moudnib', \
            'student2': 'Ricky Løtoft Omland', \
            'student3': 'Cuong Bui', \
            'student4': 'Kojar Heresh Baban', \
            'student5': 'Lars Ole Vatne', \
            'student6': 'Sondre Flovik', \
}
 
HOST = 'localhost'   # Localhost
PORT = 8888 # En ureservert port


 
# Datagram (udp) socket
try :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print 'Socket created'
except socket.error, msg :
    print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
 
 
# Bind socket til local host og port
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
#kommuniser med client

def msg_to_upper(msg_in): 
    msg_ut = [] 
    for char in msg_in: 
        msg_ut.append(chr(bitXor(ord(char)))) 
    
    return msg_ut
        
def bitXor(x):
    return x^32
    
def test():
    #_t = msg_to_upper('a')[0];
    #print("test: "+_t);
    
    assert msg_to_upper('a')[0] == 'A'
    #raise AssertionError()
    return "Testen er fullført uten feil"
print test()
#while 1:
    # motta data fra client (data, addr)
    #d = s.recvfrom(1024)
    #msg = d[0]
   # addr = d[1]
     
    #if not msg: 
    #    break
   # print msg
   # print ' '.join(format(ord(x), 'b') for x in msg) 
   # reply = ''.join(msg_to_upper(msg))
    #data.decode('utf-8').upper().encode('utf-8')
    
   # print ' '.join(format(ord(x), 'b') for x in reply)
   # print
   # s.sendto(reply , addr)
    #print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.upper()
while 2:
    d = s.recvfrom(1024)
    msg = d[0]
    addr = d[1]
     
    if not msg: 
        break
    print msg
    reply = lab2.roman2dec(msg)
    msg_send = str(reply)
    s.sendto(msg_send,addr)

     




s.close()

