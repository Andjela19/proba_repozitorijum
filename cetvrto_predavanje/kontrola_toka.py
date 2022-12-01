import random




x = 10

if x > 0:
    print ("Broj x je pozitivan.")

print ("Izvrsava se u svakom slucaju")


vozilo_u_pokretu = True
brzina = 60

if vozilo_u_pokretu == True:
    print ("Vozilo se krece")
    print ("Proverite i brzinu")
    if brzina > 50:
        print("Prekoracena brzina")
    print("Ovo izvrsavam kolika god da je brzina")
    if brzina <= 50:
        print("Brzina je ok")

if vozilo_u_pokretu == False:
    print("Vozilo se ne krece")


#1 - prikaz, 2 - kupovina, 3 - izlaz
proizvod = "Duks"
cena = 3000

# komanda = int(input("Unesite komandu: "))

# if komanda == 1:
#     print("Prikazi proizvod")
#     print("Proizvod:", proizvod, "Cena:", cena)
# if komanda == 2:
#     print("Kupovina")
#     stanje = int(input("Unesite stanje na racunu: "))
#     if stanje >= cena:
#         print("Uspesna kupovina")
#     if stanje < cena:
#         print("Neuspesna kupovina")
# if komanda ==3:
#     print("Izlaz")




broj = 5
if broj > 0:
    print("Broj je veci od 0")
else:
    print("Broj je 0 ili manji od 0")


marija = False
ksenija = False
katarina = False


devojka_na_dejtu = ""
if marija:
    devojka_na_dejtu = "marija"
elif ksenija:
    devojka_na_dejtu = "ksenija"
elif katarina:
    devojka_na_dejtu = "katarina"
else:
    devojka_na_dejtu = "sofija"

print("Izlazi sa mnom: ", devojka_na_dejtu)




automobil_polovan = False
godiste = 2021
boja = "crna"

if (automobil_polovan == True or godiste > 2017) and boja == "bela":
    print("Kupujem")
else:
    print("Nema na stanju")

if not automobil_polovan == True:
    print("Automobil je nov.")


prisutan = False
smer = "python"
if not prisutan and smer == "python":
    print("Polaznik je na casu")
if prisutan:
    print("Na casu je")
if not prisutan:
    print("Nije na casu")



# trenutni_rezultat = random.randint (1, 100)
# novi_rezultat = int(input("Unesite novi broj ( od 1 do 100): "))
# if novi_rezultat > 100 or novi_rezultat < 1:
#     print("Proverite broj.")
# else:
#     print("Trenutni rezultat:", trenutni_rezultat)
#     if novi_rezultat > trenutni_rezultat:
#         print("Pobedili ste")
#     elif novi_rezultat == trenutni_rezultat:
#         print("Rezultat je identican")
#     else:
#         print("Izgubili ste")



#Ternarni operator

pol = "m"
poruka = ""


if pol == "m":
    poruka = "Hey mister"
else:
    poruka = "Hey miss"

poruka = "Hey mister" if pol == "m" else "Hey miss"
print(poruka)

popularan_proizvod = ""
jesen = False
popularan_proizvod = "ajvar" if jesen  else "sladoled"
print(popularan_proizvod)