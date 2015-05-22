# -*- coding: latin-1 -*-

#
#  IS-105 LAB4
#
#         
#
#
import sys
import random 
import math
import itertools
from collections import defaultdict

gruppe = {  'student1': 'Robin Amir Rondestvedt Moudnib', \
            'student2': 'Ricky Løtoft Omland', \
            'student3': 'Cuong Bui', \
            'student4': 'Kojar Heresh Baban', \
            'student5': 'Lars Ole Vatne', \
            'student6': 'Sondre Flovik', \
}



def poker(hands):
    "Return a list of winning hands: poker([hand,...]) => [hand,...]"
    # Tar i bruk allmax funksjonen som er under og bruker hand_rank til å rangere hendene
    return allmax(hands, key = hand_rank)

def allmax(iterable, key=lambda x:x):
    "Return a list of all items equal to the max of the iterable."
    # Her itereres det over alle elementer som er lagt til listen
    maxi = max(iterable, key=key)
    return [element for element in iterable if key(element) == key(maxi)]

def hand_rank(hand):
    "Return a value indicating how high the hand ranks."
    # 
    # counts is the count of each rank
    # ranks lists corresponding ranks
    # E.g. '7 T 7 9 7' => counts = (3, 1, 1); ranks = (7, 10, 9)
    groups = group(['--23456789TJQKA'.index(r) for r, s in hand])
    counts, ranks = unzip(groups)
    # Counts teller og rangerer i synkende rekkefølge. Eksempelet ovenfor illustrerer.
    # Ranks er rangeringen av kortene og under her legges det til en unntaksregel for kortet ess
    # Dette fordi kortet ess kan ha verdien 1 og 14
    if ranks == (14, 5, 4, 3, 2):
        ranks = (5, 4, 3, 2, 1)
    # Her definerer vi at straight = lengden av ranks = 5
    # Og at det er fire kort fra det høyeste kortet til det laveste. 
    # Eks: 9, 8, 7, 6, 5
    straight = len(ranks) == 5 and max(ranks)-min(ranks) == 4
    # Her definerer vi at flush = at alle suits (typer) for ranks(kort) skal være like.
    flush = len(set([s for r, s in hand])) == 1
    # Her er rangeringen fra 9 som er 5 like dersom vi har flere kortstokker
    # Under kommer straight flush med en rangering på 8 osv helt ned til 0
    # Dette er da at man ikke har par og bare går på høyeste kort.
    return (
        9 if (5, ) == counts else
        8 if straight and flush else
        7 if (4, 1) == counts else
        6 if (3, 2) == counts else
        5 if flush else
        4 if straight else
        3 if (3, 1, 1) == counts else
        2 if (2, 2, 1) == counts else
        1 if (2, 1, 1, 1) == counts else
        0), ranks 

def group(items):
    "Return a list of [(count, x)...], highest count first, the highest x first"
    # Her lages en liste hvor kortene "telles" for å kunne gi en rank til hånden
    # Eksempelvis 7, 7, 7, 4, 3 blir da [3, 1, 1] Da det er tre 7ere og en hver av 4 og 3
    groups = [(items.count(x), x) for x in set(items)]
    return sorted(groups, reverse = True)

def unzip(pairs):
    return zip(*pairs)

def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    # ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    # ranks = [{'A':14,
    #           'K':13,
    #           'Q':12,
    #           'J':11,
    #           'T':10,
    #           }.get(r,r) for r, s in hand]
    
    #            Lister opp verdiene i stigende/synkende rekkefølge
    #            Hvis ikke A er presentert, så gå nedover rangstigen osv
    #            Lager en for løkke
    #            Rangeringen blir sortert og lager en regel for at revers rangering har samme verdi
    #            Returnerer ranks hvis ranks ikke er lik 5,4,3,2
    #            Her er det lagd en unntaksregel slik at programmet forstår at det er en straight. 
    #            I andre tilfeller vil ess ha verdi lik 14     
    
    ranks = [14 if r == 'A' else
             13 if r == 'K' else
             12 if r == 'Q' else
             11 if r == 'J' else
             10 if r == 'T' else
             int(r)
             for r, s in hand]
    ranks.sort(reverse = True)
    return ranks if ranks != [14, 5, 4, 3, 2] else [5, 4, 3, 2, 1]

def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    # Her sjekker vi om kortene blir straight
    return sum(ranks) - min(ranks)*5 == 10

def flush(hand):
    "Return True if all the cards have the same suit."
    # Som beskrivelsen, sjekker om kortene er av samme type og blir true om de har det
    suits = [s for r, s in hand]
    return len(set(suits)) == 1

def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    # Sjekker om det er to par, og setter dem inn i en tuple fra høyest til lavest
    # Om ikke returneres ingen ting (altså None)
    result = [r for r in set(ranks) if ranks.count(r) == 2]
    if len(result) == 2:
        return (max(result), min(result))

def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    # Returnerer den første ranken som denne hånden har n av
    # Eksempel: Hvis n er 3 returneres ranken til three of a kind
    for r in set(ranks):
        if ranks.count(r) == n:
            return r
    return None

deck = [r+s for r in '23456789TJQKA' for s in 'SHDC'] 

def deal(numhands, n = 5, deck = [r+s for r in '23456789TJQKA' for s in 'SHDC']):
    "Return a list of numhands hands consisting of n cards each"
    # Her deles det ut numhands antall hender med n kort i hver hånd
    # Hendene består av kort med r fra 2 til A og s av SHDC
    random.shuffle(deck)
    # Kortene stokkes
    deck = iter(deck)
    return [[next(deck) for card in range(n)] for hand in range(numhands)]

def test():
    "Tester for funksjonene i poker programmet"
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    s1 = "AS 2S 3S 4S 5C".split() # A-5 straight
    s2 = "2C 3C 4C 5S 6S".split() # 2-6 straight
    s3 = "TC JC QC KS AS".split() # 10-A straight    
    tp = "5S 5D 9H 9C 6S".split() # two pair
    ah = "AS 2S 3S 4S 6C".split() # A high
    sh = "2S 3S 4S 6C 7D".split() # 7 high
    assert poker([sf, fk, fh]) == [sf] # Sjekker om straight flush er høyere enn fk og fh
    assert poker([fk, fh]) == [fk] # Sjekker om fk er høyere enn fh
    assert poker([fh, fh]) == [fh, fh] # Sjekker om fh og fh er like høyt rangert
    assert poker([sf]) == [sf] # Sjekker om sf er lik sf
    assert poker([sf] + 99*[fh]) == [sf] # Sjekker om sf er høyere en 99 fh
    assert poker([s1, s2]) == [s2] # Sjekker om s2 straight er høyere enn s1 straight
    assert poker([s1, tp]) == [s1] # Sjekker om s1 straight er høyere enn to par
   

    assert card_ranks(sf) == [10, 9, 8, 7, 6] # Sjekker om  straight flush består av synkende verdier
    assert card_ranks(fk) == [9, 9, 9, 9, 7] # Sjekker fire like
    assert card_ranks(fh) == [10, 10, 10, 7, 7] # Sjekker fult hus
    assert card_ranks(['AC', '3D', '4S', 'KH']) == [14, 13, 4, 3] # Sjekker at kortene rangeres riktig og sortere

    # Sjekker at en hånd med Ess som høyest slår en hånd med 7 som høyest
    assert (card_ranks(['AS', '2C', '3D', '4H', '6S']) >
            card_ranks(['2D', '3S', '4C', '6H', '7D']))
    # Sjekker at straight opp til fem blir slått av straight opp til 6
    assert (card_ranks(['AS', '2C', '3D', '4H', '5S']) <
            card_ranks(['2D', '3S', '4C', '5H', '6D']))
    
    # Lager variabler for fire like og to par
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    
    # Videre testing av funksjonene
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7

    assert two_pair(tpranks) == (9, 5)
    assert two_pair([10, 10, 5, 5, 2]) == (10, 5)    

    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False
    
    # Sjekker at sf er en flush
    assert flush(sf) == True
    # Sjekker at fk ikke er en flush
    assert flush(fk) == False

    return 'Testene er gjennomført uten feil'
    
#Alle de forskjellige typene hender
hand_names = [
    'High Card',
    'Pair',
    '2 Pair',
    '3 Kind',
    'Straight',
    'Flush',
    'Full House',
    '4 Kind',
    'Straight Flush',
    ]
def hand_percentages(n = 700*1000):
    "Sample n random hands and print a table of percentages for each type of hand"
    # Lager n antall hender og tester de for å lage en tabell med prosentandel for hver hånd
    counts = [0]*9
    for i in range(n/10):
        for hand in deal(10):
            ranking = hand_rank(hand)[0]
            counts[ranking] += 1
    for i in reversed(range(9)):
        print('%14s: %6.3f'%(hand_names[i], 100.*counts[i]/n))
        
def all_hand_percentages():
    "Print an exhaustive table of frequencies for each type of hand"
    counts = [0]*9
    n = 0
    deck = [r+s for r in '23456789TJQKA' for s in 'SHDC']
    for hand in itertools.combinations(deck, 5):
        n += 1
        ranking = hand_rank(hand)[0]
        counts[ranking] += 1
    for i in reversed(range(9)):
        print('%14s: %7d %6.3f'%(hand_names[i], counts[i], 100.*counts[i]/n))

        # Herfra og ned er de resterende funksjonene oppgaveteksten ber oss importere fra udacity

def shuffle1(deck):
    # O(N**2)
    # incorrect distribution
    N = len(deck)
    swapped = [False] * N
    while not all(swapped):
        i, j = random.randrange(N), random.randrange(N)
        swapped[i] = swapped[j] = True
        deck[i], deck[j] = deck[j], deck[i]

def shuffle2(deck):
    # O(N**2)
    # incorrect distribution?    
    N = len(deck)
    swapped = [False] * N
    while not all(swapped):
        i, j = random.randrange(N), random.randrange(N)
        swapped[i] = True
        deck[i], deck[j] = deck[j], deck[i]

def shuffle2a(deck):
    # http://forums.udacity.com/cs212-april2012/questions/3462/better-implementation-of-shuffle2
    N = len(deck)
    swapped = [False] * N
    while not all(swapped):
        i = random.choice(filter(lambda idx: not swapped[idx], range(N)))
        j = random.choice(filter(lambda idx: not swapped[idx], range(N)))
        swapped[i] = True
        deck[i], deck[j] = deck[j], deck[i]

def shuffle3(deck):
    # O(N)
    # incorrect distribution    
    N = len(deck)
    for i in range(N):
        j = random.randrange(N)
        deck[i], deck[j] = deck[j], deck[i]

def shuffle(deck):
    # Knuth method
    n = len(deck)
    for i in range(n-1):
        j = random.randrange(i, n)
        deck[i], deck[j] = deck[j], deck[i]        

def test_shuffler(shuffler, deck='abcd', n=10000):
    counts = defaultdict(int)
    for _ in range(n):
        input = list(deck)
        shuffler(input)
        counts[''.join(input)] += 1
    e = n*1./factorial(len(deck))  ## expected count
    ok = all((0.9 <= counts[item]/e <= 1.1) for item in counts)
    name = shuffler.__name__
    print '%s(%s) %s' % (name, deck, ('ok' if ok else '*** bad ***'))
    print '    ',
    for item, count in sorted(counts.items()):
        print "%s:%4.1f" % (item, count*100./n),
    print

def test_shufflers(shufflers=[shuffle, shuffle1], decks=['abc','ab']):
    for deck in decks:
        print
        for f in shufflers:
            test_shuffler(f, deck)

def factorial(n): return 1 if (n <= 1) else n*factorial(n-1)

print test() # Kjører testen som har alle assert setningene og printer ut at den er gjennomført uten feil
