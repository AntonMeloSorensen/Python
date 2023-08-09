# Spøgelses spil
from random import randint
print("spøgelsesspil")
foeler_sig_modig = True
score = 0
while foeler_sig_modig:
    spoegelsesdoer = randint(1, 3)
    print("Der er træ døre forand dig...")
    print("Et spøgelse bag en af dem.")
    print ("hvilken dør åbner du?")
    doer_num = input ("1, 2 eller 3?")
    doer_num = int (doer_num)
    if doer_num == spoegelsesdoer:
        print("Spøgelse")
        foeler_sig_modig = False
    else:
        print("intet spøgelse")
        print("du går ind i næste rum")
        score = score + 1
print("løb væk!")
print("Spillet er slut! Du scorede", score)
 
