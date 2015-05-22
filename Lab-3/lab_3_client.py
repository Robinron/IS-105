# -*- coding: latin-1 -*-

import socket #For sockets.
import sys #For exit.
import lab2 #Importerer lab2 for å kunne bruke roman2dec funksjon. 

# Lager dgram udp socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error:
    print 'Feilet å lage socket'
    sys.exit()
#Legger til en feilmelding og går ut av systemet dersom en error oppstår.      
host = 'localhost';
#Definerer et navn til serveren.
port = 8888;

while(1) :
    try: 
        msg = raw_input('Fra lower to uppercase : ')
        #Prompt, bruker setter en input. 
        s.sendto(msg, (host, port))
        d = s.recvfrom(1024)
        msg_send = d[0]
        addr = d[1]
        #Sender input med lowercase bokstaver til serveren. 
        print msg_send
        
        
        romanTo = raw_input ('Roman til desimal : ')
        s.sendto(romanTo, (host, port))
        e = s.recvfrom(1024)
        msg_send = e[0]
        addr = e[1]
        #Sender input med romersk tall til serveren.
    
        print lab2.roman2dec(romanTo)
        #Printer ut desimale siffer fra romersk tallsystem. Bruker funksjon fra lab2.
    except: 
        print 'Noe er galt'
        
        sys.exit()
