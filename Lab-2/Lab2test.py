# -*- coding: utf-8 -*-

#
#  IS-105 LAB2
#
#  
#         
#
#
import sys
import Lab2

# Skriv inn fullt navn på gruppemedlemene (erstatte '-' med navn slikt 'Kari Trå')
gruppe = {  'student1': 'Robin Amir Rondestvedt Moudnib', \
            'student2': 'Ricky Løtoft Omland', \
            'student3': 'Cuong Bui', \
            'student4': 'Kojar Heresh Baban', \
            'student5': 'Lars Ole Vatne', \
            'student6': 'Sondre Flovik', \
}

def test():

    assert Lab2.roman2dec('v') == 5
    assert Lab2.roman2dec('XII') == 12
    assert Lab2.dec2roman(2129) == 'MMCXXIX'
    assert Lab2.dec2roman(20) == 'XX'
    assert Lab2.doit('II + III') == 'V'
    assert Lab2.doit('X - V') == 'V'
    print "Alle tester gikk gjennom feilfritt"

test()
