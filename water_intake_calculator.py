""" Arstid soovitavad juua päevas 2 liitrit vett.
Kirjuta programm, mis küsib kasutajalt, kui palju klaase vett ta juba joonud on. Oletame, et üks klaas = 250 ml.
Programm arvutab, mitu protsenti päevanormist on täidetud, ja annab tagasisidet:
Kui protsent < 50: väljasta: „Joo rohkem vett, keha vajab seda!“
Kui protsent < 100: väljasta: „Tubli, jätka samas vaimus!“
Kui protsent ≥ 100: väljasta: „Suurepärane, oled oma päevase eesmärgi täitnud!“ """

klaasid = int(input("Mitu klaasi vett oled täna joonud? "))

paevane_eesmark = 2000
klaasi_suurus = 250

joodud_vesi = klaasid * klaasi_suurus
protsent = joodud_vesi / paevane_eesmark * 100

print("Oled täitnud", protsent, "% päevasest eesmärgist.")

if protsent < 50:
    print("Joo rohkem vett, keha vajab seda!")
elif protsent < 100:
    print("Tubli, jätka samas vaimus!")
else:
    print("Suurepärane, oled oma päevase eesmärgi täitnud!")
