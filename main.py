#alusta programmi
#Küsi kasutajalt : ,,Mis päev on homme? (tööpäev/puhkepäev)"
#Salvesta vastus muutujasse day.
#Kui day on võrdne sõnaga ,,tööpäev", siis väljasta ekraanile : ,,Veel üks osa Netflixist".

""" day = input("mis päev on homme? (tööpäev/puhkepäev):")

if day == "tööpäev":
    print("Ma lähen magama, head ööd!")
elif day == "puhkepäev":
    print("Veel üks osa Netflixist!")
else:
    print("Vale väärtus")
 """

#Finantsnõustaja
""" Sa tahad osta endale uue iPhone 17 Pro, aga sa oled otsustanud, et krediiti sa ei võta. Selle asemel oled sa palkanud range ja vastutustundliku finantsnõustaja programmi kujul.
See programm:
-küsib, kui palju sul on praegu raha,
-võrdleb seda iPhone 17 Pro hinnaga (näiteks 2500€)
-ja annab sulle täiesti ratsionaalse, emotsioonideta soovituse. """

""" print("Tere tulemast programmi 'Finantsnõustaja'!")
print("Sinu isiklik nõustaja ei tee emotsionaalseid oste.")

money = int(input ("Kui palju raha sul on praegu?"))


if money < 2500:
    print("Sul pole veel piisavalt raha. Ole kannatlik ja kogu edasi!")
elif money == 2500:
    print("Palju õnne, saad osta uue iPhone 17 Pro sularahas!")
else:
    print("Saad osta iPhone 17 Pro ja veel jääb raha üle.") """


#Sammulugeja
""" Sul on eesmärk teha iga päev 10000 sammu. Programm küsib kasutajalt, mitu sammu ta on juba teinud, arvutab täitmise protsendi ja annab tagasisidet.
-Kui protsent < 50: ,,Alles poolel teel, liigu edasi!"
-Kui Protsent > 75: ,,Tubli, oled peaegu kohal!"
-Kui protsent >= 100: ,,Palju õnne, oled oma eesmärgi täitnud!" """

goal = 10000
steps = int(input("Mitu sammu oled juba teinud?:"))

percent = (steps/goal) * 100

print(f"{percent}%")

if percent < 50:
    print("Alles poolel teel, liigu edasi!")
elif percent < 75:
    print("Tubli, oled peaegu kohal!")
elif percent < 100:
    print("Suurepärane, oled peaegu kohal!")
else: 
    print("Palju õnne, oled oma eesmärgi täitnud!")


