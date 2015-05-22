# -*- coding: utf-8 -*-

#
#  IS-105 LAB1
#
#  lab1.py - kildekode vil inneholde studentenes løsning.
#         
#
#
import sys


# Skriv inn fullt navn på gruppemedlemene (erstatte '-' med navn slikt 'Kari Trå')
gruppe = {  'student1': 'Robin Amir Rondestvedt Moudnib', \
            'student2': 'Ricky Omland', \
            'student3': 'Kojar Baban', \
            'student4': 'Lars Vatne', \
            'student5': 'Cuong Bui', \
            'student6': 'Sondre Flovik', \
}

#
#  Oppgave 1
#    Leke med utskrift 
#    Skriv ut følgende "ascii art" i en funksjon (erstatte pass)
#    Funksjonen skal hete ascii_fugl() og skal være uten argumenter og uten returverdier
#    Den skal skrive ut følgende når den brukes ascii_fugl
#
#       \/_
#  \,   /( ,/
#   \\\' ///
#    \_ /_/
#    (./
#     '` 
def ascii_fugl():

    print '        \/_'
    print '    \,  /(  ,/'
    print '     \\\\\\\' ///'
    print '      \\_ /_/ '
    print '      (./ '  
    print '       \'` '

ascii_fugl()

# 
#  Oppgave 2
#    bitAnd - x&y
#	 Implementer funksjonen som gjør en "bitwise" AND operasjon (erstatt pass)
#    Eksempel: bitAnd(6, 5) = 4
#		Forklaring: 6 binært er 110, mens 5 er 101. Hvis vi sammenligner bitvis
#					1 AND 1 gir 1, 1 AND 0 gir 0 og 0 AND 1 gir 0 => 100 binært
#					er 4 desimalt. Antagelse: posisjonsbasert tallsystem og 
#					den mest signifikante bit-en er lengst til venstre
def bitAnd(x, y):
    return x&y




#
#  Oppgave 3
#    bitXor - x^y
#    Eksempel: bitXor(4, 5) = 1
#
def bitXor(x, y):
    return x^y
	

#
#  Oppgave 4
#    bitOr - x|y
#    Eksempel: bitOr(0, 1) = 1
#
def bitOr(x, y):
    return x|y


#
#  Oppgave 5
#
#  Tips:
#    For å finne desimalverdien til et tegn kan funksjonen ord brukes, for eksempel
#      ord('A') , det vil gi et tall 65 i ti-tallssystemet
#    For å formattere 6 i ti-tallssystemet til 00000110 i to-tallssystemet
#      '{0:08b}'.format(6)
#      00000110
#
#    Formatteringsstrengen forklart:
#      {} setter en variabel inn i strengen
#      0 tar variabelen i argument posisjon 0
#      : legger til formatteringsmuligheter for denne variabelen (ellers hadde den 6 desimalt)
#      08 formatterer tall til 8 tegn og fuller med nuller til venstre hvis nødvendig
#      b konverterer tallet til dets binære representasjon
#
#	 Hvilke begrensninger vil en slik funksjon ha? (tips: prøv med bokstaven 'å', f.eks.)
#    Svar: Ved bruk av denne funksjonen vil det være begrensninger innad i ascii biblioteket som er det eneste som støttes her. 
#    Norske bokstaver er ikke inkludert i dette, og vi vil dermed få en feilmelding.
#
#	 Forklar resultatet ascii8Bin('å')
#    Svar: Når vi forsøker å kjøre ascii8Bin('å') får vi feilmeldingen: "TypeError: ord() expected a character, but string of length 2 found"
#    Dette da fordi norske bokstaver som sagt ikke er inkludert i ascii-biblioteket.
#
#	 Hvilke faktorer påvirker resultatet? Forklar.
#    Svar: Ascii sitt bibliotek. 
#    Vi må derfor bruke tegn som er inkludert i dette for å unngå feil.
#
def ascii8Bin(bokstav):
	binobjekt = ord(bokstav)
	return '{0:08b}'.format(binobjekt)
	
# 
#  Oppgave 6
#    transferBin - ta en tilfeldig streng som argument og skriver ut en blokk av 8-bits strenger
#                  som er den binære representasjon av strengen
#    Eksempel: transferBin("Hi") skriver ut: 
#                01001000
#                01101001
#	 Forklart hver linje i denne funksjonen (hva er list, hva gjør in)
#    Først definerer vi funksjonen og legger inn at den trenger input som er string
#    Deretter lager vi en variabel som er en liste av string.
#    Så bruker vi løkken til å hente ut bokstavene av type string
#    Til slutt returneres strengene formatert ved hjelp av vår ascii8Bin funksjon.
#    
#	 Skriv selv inn tester ved å bruke assert i funksjonen test()
#
def transferBin(string): 
	l = list(string)
	for c in l:
            return ascii8Bin(c)
            
#   Her blir blokkene returnert i stedet for skrevet ut. 
#   Grunnen til dette er at dersom koden ikke returnerer noe vil ikke assert-setningen vår i test() funksjonen gå gjennom
#   Dersom vi endrer return her til print vil blokkene bli skrevet ut men ikke gå gjennom testen          




	   



#
#  Oppgave 7
#    transferHex - gjør det samme som transferBin, bare skriver ut representasjonen
#					av strengen heksadesimalt (bruk formattering forklart i Oppgave 6)
#					Skriv gjerne en støttefunksjon ascii2Hex, som representerer et tegn
#					med 2 heksadesimale tegn
#    Skriv selv inn tester ved å bruke assert i funksjonen test()
#  
def ascii2hex(bokstav):
    hexb = ord(bokstav)
    toHex ="{0:02x}".format(hexb)
    return(toHex)
    
 


def transferHex(string):
	l = list(string)
	for c in l:
            return ascii2hex(c)


#   Her blir den heksadesimale representasjonen returnert i stedet for skrevet ut. 
#   Grunnen til dette er at dersom koden ikke returnerer noe vil ikke assert-setningen vår i test() funksjonen gå gjennom
#   Dersom vi endrer return her til print vil blokkene bli skrevet ut men ikke gå gjennom testen         
    

#
# Oppgave 8
# 		Implementer en funksjon unicodeBin, som kan behandle norske bokstaver
# 		Kravspesifikasjon for denne funksjonen er den samme som for ascii8Bin funksjonen
def unicodeBin(bokstav):
    return '{0:08b}'.format(ord(bokstav.decode('utf8')))



#
# Oppgave 9
# 	Studer python module psutils (må være obs på versjon)
#   Prøv å finne ut hvordan du kan finne ut og skrive ut følgende informasjon om din 
#   datamaskin-node:
#
# 			Brand and model
# 			Hard drive capacity
# 			Amount of RAM
# 			Model and speed of CPU
# 			Display resolution and size
# 			Operating system
#	
#	Forklar hvorfor man kan / ikke kan finne denne informasjon vha. psutil modulen.
#	Skriv en funksjon printSysInfo som skriver ut den informasjon som psutil kan finne.
#	Kan dere skrive en test for denne funksjonen?
#	Hvilke andre muligheter har man for å finne informasjon om maskinvare i GNU/Linux?
#
def printSysInfo():
	pass
#  Det er dette som mangler


def test():
	assert bitAnd(6, 5) == 4
	assert bitXor(4, 5) == 1
	assert bitOr(0, 1) == 1
	assert ascii8Bin('B') == '01000010'
	assert ascii8Bin('C') == '01000011'
	assert transferBin('Hi') == '01001000', '01101001'
	assert ascii2hex('H') == '48'
	assert transferHex('Hi') == '48', '69'
	assert unicodeBin('å') == '11100101' 
	return "Testene er fullført uten feil."


# Bruk denne funksjonen for å vise at alle testene er kjørt feilfritt
print test()
		
