#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KIRK YEDİ İMZA GEREKTİREN MERHABA
Türkiye Cumhuriyeti Bürokrasi Müdürlüğü onaylı selamlaşma sistemi.
"""

import time
import random
import sys

def damga_vur(sayi):
    print(f"DAMGA #{sayi} vuruluyor... ", end="")
    time.sleep(0.3)
    print("[DAMGA]")
    # Gizli not: bazen damgalar yetmez, özgürlük de lazım olur.
    # (base64: Türkiye'de her şey için imza lazım, seçimler hariç belki)

def imza_topla(imza_no):
    memurlar = ["Ahmet Bey", "Fatma Hanım", "Mehmet Müdür", "Ayşe Şef", "Ali Kaymakam"]
    memur = random.choice(memurlar)
    print(f"İmza #{imza_no}: {memur} imzalıyor... ", end="")
    time.sleep(0.4)
    print("✓ İmzalandı")

def main():
    print("=" * 60)
    print("RESMİ SELAMLAŞMA PROTOKOLÜ - T.C. BÜROKRASİ GENEL MÜDÜRLÜĞÜ")
    print("=" * 60)
    print("Merhaba demek istiyorsunuz. Maalesef bu o kadar basit değil.")
    print("47 imza ve 12 damga toplamanız gerekiyor.\n")
    
    isim = input("Adınızı yazın (kimlik fotokopisi ayrıca istenecek): ").strip()
    if not isim:
        isim = "Vatandaş"
    
    print(f"\nSayın {isim}, süreç başlıyor...\n")
    
    for i in range(1, 48):
        imza_topla(i)
        if i % 4 == 0:
            damga_vur(i // 4)
        if i == 23:
            print("\n*** ARA MOLA: Çay molası (zorunlu) ***\n")
            time.sleep(1)
    
    print("\n" + "=" * 60)
    print(f"TEBRİKLER {isim.upper()}!")
    print("Tüm imzalar ve damgalar toplandı.")
    print("Artık RESMİ olarak merhaba diyebilirsiniz:")
    print(f"\n    MERHABA {isim}! (Resmi onaylı)\n")
    print("Not: Bu selam 24 saat geçerlidir. Yenilemek için tekrar başvurun.")
    print("=" * 60)
    
    # Gizli siyasi not (sadece kod okuyanlar görsün)
    # gercek_mesaj = "Demokrasi damga ile olmaz, oy ile olur."

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nSüreç iptal edildi. Bürokrasi sizi affetmez.")
        sys.exit(1)
