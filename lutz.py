# -*- coding: utf-8 -*-
#!/usr/bin/python

# I) Lade Code für Zufallsauswahl
from random import choice

# II) Definiere die im Programm verwendeten Wörter
subjekt = [['GRAF', 0], ['FREMDE', 1], ['BLICK',0],['KIRCHE',1], ['SCHLOSS',2], ['BILD',2], ['AUGE',2], ['DORF',2], ['TURM',0], ['BAUER',0], ['WEG',0], ['GAST',0], ['TAG',0], ['HAUS',2], ['TISCH',0], ['KNECHT',0]]	
adjektiv = ['OFFEN', 'STILL', 'STARK', 'GUT', 'SCHMAL', 'NAH', 'NEU', 'LEISE', 'FERN', 'TIEF', 'SPÄT', 'DUNKEL', 'FREI', 'GROSS', 'ALT', 'WÜTEND']
konjunktion = [' UND', ' ODER', ' SO GILT', '.', '.', '.', '.', '.']
operator = [['EIN', 'EINE', 'EIN'], ['JEDER', 'JEDE', 'JEDES'], ['KEIN', 'KEINE', 'KEIN'], ['NICHT JEDER', 'NICHT JEDE', 'NICHT JEDES']]
  
# III) Erstelle eine Funktion, die wiederholt aufgerufen werden kann, um einen Rumpfsatz zu bilden
def rumpf(): 
    wahl_subjekt = choice(subjekt) 
    wahl_operator = choice(operator)
    wahl_operator = wahl_operator[wahl_subjekt[1]]
    wahl_subjekt = wahl_subjekt[0]
    text = wahl_operator + ' ' + wahl_subjekt 
    return text + ' IST'

# IV) Bilde den Rumpfsatz, hänge ein Prädikat, eine Konjunktion und dann erneut den Rumpfsatz an. Dies soll 71-fach untereinander geschehen und als Programmoutput ausgegeben werden.

for i in range(71):
    print((rumpf() + ' ' + choice(adjektiv) + choice(konjunktion) + ' ' +  	rumpf() + ' ' +  choice(adjektiv) + '.')) 