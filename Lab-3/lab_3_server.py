# -*- coding: utf-8 -*-

import socket
import sys
import lab2

HOST = 'localhost' # Localhost
PORT = 8888 # En ureservert port

# Datagram (udp) socket
try :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print 'Socket opprettet'
except socket.error, msg :
    print 'Feilet å lage socket. Error kode: ' + str(msg[0]) + ' Beskjed ' + msg[1]
    sys.exit()
    
# Bind socket til local host og port
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind feilet. Error kode : ' + str(msg[0]) + ' Beskjed ' + msg[1]
    sys.exit()
    
print 'Socket bind komplett'

#Kommuniserer med client

def msg_to_upper(msg_in):
    msg_ut = []
    for char in msg_in:
        msg_ut.append(chr(bitXor(ord(char))))
    return msg_ut
#Våres funksjon for å gjøre meldingen vi mottar fra lower til uppercase. 
  
def bitXor(x):
    return x^32
    #Funksjon som flipper den sjette bit'en.
    #Dette fører til at den bokstaven den flipper går fra lower til uppercase.
    
def test():
    test = msg_to_upper('a')[0];
    print("Test: "+ test);
    assert msg_to_upper('a')[0] == 'A', 'Noe er fullstendig feil'
    return "Testen er fullført uten feil"
print test()    
#En testfunksjon som bruker assert for å sjekke funksjonen msg_to_upper(),
#om overføringen fra liten til store bokstaver.

while 1:
    d = s.recvfrom(1024)
    #mottar data fra client (data, addr). 
    msg = d[0]
    addr = d[1]
    #Avsenders adresse settes inn en variabel og blir returadressen.
    if not msg:
        break
    print msg
    print ' '.join(format(ord(x), 'b') for x in msg)
    reply = ''.join(msg_to_upper(msg))
    print ' '.join(format(ord(x), 'b') for x in reply)
    s.sendto(reply , addr)
    #Går gjennom liste og printer ut bokstavene i lower case som binærtall.
    
   
s.close()
