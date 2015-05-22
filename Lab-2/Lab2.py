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
            'student2': 'Ricky Løtoft Omland', \
            'student3': 'Cuong Bui', \
            'student4': 'Kojar Heresh Baban', \
            'student5': 'Lars Ole Vatne', \
            'student6': 'Sondre Flovik', \
}

import re
import math

# Uttrykk brukt for å validere og analysere Romerske tall
roman_re = re.compile("""^
   ([M]{0,9})   # thousands
   ([DCM]*)     # hundreds
   ([XLC]*)     # tens
   ([IVX]*)     # units
   $""", re.VERBOSE)

# Dette arrayet inneholder gyldige grupperinger av siffer og deres verdi.
# Den første rekken er for entall, den andre rekken for titall og den tredje for hundretall.
# For eksempel, det sjette elementet i tier-rekken har verdien 50, siden det første er 0.
d2r_table = [
    ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
    ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
    ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']]



def roman2dec(roman):
# Konverterer et romertall kodet i string til desimaltall.
    roman = roman.upper()
    match = roman_re.match(roman)
# Om stringen ikke samstemmer med en gyldig verdi så gis feilmelding. 
    if not match:
        raise ValueError
# Angir verdiene til feltene units, tens, hundreds
    thousands, hundreds, tens, units = match.groups()
    result = 1000 * len(thousands)
    result += d2r_table[2].index(hundreds) * 100
    result += d2r_table[1].index(tens) * 10
    result += d2r_table[0].index(units)

    print result

# Konverterer en positiv desimal integer til et romertall.
def dec2roman(dec):
 
    if dec == 0:
        return ''

    digit = 0
    rem = dec
    result = ''

    # Antall siffer i nummeret dec
    dec_len = int(math.ceil(math.log10(dec)) + 1)

    # Skanner nummeret digit-by-digit, starter fra MSD (most-significant-digit)
    while dec_len > 0:
        # Ta det gjeldende sifferet
        factor = 10 ** (dec_len - 1)
        digit = rem / factor

        # Fjern det fra nummeret
        rem = rem - digit * factor

        if dec_len >= 4:
            # Tusentall
            result = result + digit * 'M'
        else:
            # Sjekker i look-up table
            result = result + d2r_table[dec_len - 1][digit]

        dec_len -= 1

    
    print result
dec2roman(2129) 
roman2dec("XII")

m=zip((1000,900,500,400,100,90,50,40,10,9,5,4,1),
('M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I'))
def doit(s):
 x={'M':1e3,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1};y=[];z='';a='0';s='+'+s
 for c in s.upper():
  if c in x:
   z+=c;y.append(x[c])
   if len(y)>1and y[-1]>y[-2]:y[-2]*=-1
   x[z]=sum(y)
  elif c in"+/*-":a='('+a+z+')'+c;y=[];z=''
 a+=z;i=eval(a,x);r = ''
 for n,c in m:d=int(i/n);r+=c*d;i-=n*d
 return r


print doit("II + III")
print doit("x - v")
