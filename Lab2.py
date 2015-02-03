# -*- coding: utf-8 -*-

def int_to_roman (integer):

    returnstring=''
    table=[['M',1000],['CM',900],['D',500],['CD',400],['C',100],['XC',90],['L',50],['XL',40],['X',10],['IX',9],['V',5],['IV',4],['I',1]]

    for pair in table:

        while integer-pair[1]>=0:

            integer-=pair[1]
            returnstring+=pair[0]

    print returnstring

def rom_to_int(string):

    table=[['M',1000],['CM',900],['D',500],['CD',400],['C',100],['XC',90],['L',50],['XL',40],['X',10],['IX',9],['V',5],['IV',4],['I',1]]
    returnint = 0
    for pair in table:


        continueyes=True

        while continueyes:
            if len(string)>=len(pair[0]):

                if string[0:len(pair[0])]==pair[0]:
                    returnint+=pair[1]
                    string=string[len(pair[0]):]

                else: continueyes=False
            else: continueyes=False

    print returnint
    
#def rom_addisjon(string1, string2):

    #table=[['M'],['CM'],['D'],['CD'],['C'],['XC'],['L'],['XL'],['X'],['IX'],['V'],['IV'],['I']]
    
def addRoman(left, right):
    newString = left + right                  
    print newString
    
addRoman("III", "I")
        
    
