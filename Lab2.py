# -*- coding: utf-8 -*-
import re
import math


# Regular expression used to validate and parse Roman numbers
roman_re = re.compile("""^
   ([M]{0,9})   # thousands
   ([DCM]*)     # hundreds
   ([XLC]*)     # tens
   ([IVX]*)     # units
   $""", re.VERBOSE)

# This array contains valid groups of digits and encodes their values.
# The first row is for units, the second for tens and the third for
# hundreds. For example, the sixth element of the tens row yields the
# value 50, as the first is 0.
d2r_table = [
    ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
    ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
    ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']]



def roman2dec(roman):
    """Converts a roman number, encoded in a string, to a decimal number."""
    roman = roman.upper()
    match = roman_re.match(roman)

    if not match:
        raise ValueError

    thousands, hundreds, tens, units = match.groups()
    result = 1000 * len(thousands)
    result += d2r_table[2].index(hundreds) * 100
    result += d2r_table[1].index(tens) * 10
    result += d2r_table[0].index(units)

    print result


def dec2roman(dec):
    """Converts a positive decimal integer to a roman number."""
    if dec == 0:
        return ''

    digit = 0
    rem = dec
    result = ''

    # Length in digits of the number dec
    dec_len = int(math.ceil(math.log10(dec)) + 1)

    # Scan the number digit-by-digit, starting from the MSD (most-significant
    # digit)
    while dec_len > 0:
        # Let's take the current digit
        factor = 10 ** (dec_len - 1)
        digit = rem / factor

        # And remove it from the number
        rem = rem - digit * factor

        if dec_len >= 4:
            # Thousands
            result = result + digit * 'M'
        else:
            # Look in the look-up table
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
