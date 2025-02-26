#!/bin/python3

import random
import sys

if len(sys.argv) > 1:
    atilanZar = sys.argv[1]
else:
    print("Lütfen bir zar türü girin! (Örn: d20)")
    sys.exit(1)

def zar_kontrol(zar):
    match zar:
        case "d20":
            sonuc = random.randint(1, 20)
            print("d20:", sonuc)
        case "d4":
            sonuc = random.randint(1, 4)
            print("d4:", sonuc)
        case "d6":
            sonuc = random.randint(1, 6)
            print("d6:", sonuc)
        case "d8":
            sonuc = random.randint(1, 8)
            print("d8:", sonuc)
        case "d10":
            sonuc = random.randint(1, 10)
            print("d10:", sonuc)
        case "d12":
            sonuc = random.randint(1, 12)
            print("d12:", sonuc)
        case "d100":
            sonuc = random.randint(1, 100)
            print("d100:", sonuc)
        case "yardim":
            print('Kullanımı: roll zar (d20, d4, d6, d8, d10, d12, d100)')
        case _:
            print("Böyle bir zar yok.")

zar_kontrol(atilanZar)