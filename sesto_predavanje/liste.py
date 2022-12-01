osoba = ["Sofija", 25, "plava", False]

for indeks in range (len(osoba)):
    print (osoba[indeks])

for osobina in osoba:
    print(osobina)


voce_i_povrce = ["jabuka", "beli luk", "crni luk", "banana", "mandarina", "krastavac"]

for vrednost in voce_i_povrce:
    print(vrednost)

for i in range(len(voce_i_povrce)):
    print(voce_i_povrce[i])


for indeks, vrednost in enumerate (voce_i_povrce):
    print(indeks,vrednost)


automobili = ["Citroen", "bmw", "opel", "kia", "yugo", "opel", "opel"]
#pozicija #auto #citroen

#Prvi primer
for pozicija, auto in enumerate(automobili):
    print("Pozicijja:", pozicija, "Auto:", auto)


#Drugi primer
for pozicija, auto in enumerate(automobili):
    if pozicija == 1:
        print("Kupujem")
        break
    print("Pozicija: ", pozicija, "Auto: ", auto)

#Treci primer
for pozicija, auto in enumerate(automobili):
    if auto == "opel":
        print(pozicija, auto)
    #print ("Pozicija", pozicija, "Auto", auto)

#Cetvrti primer
for pozicija, auto in enumerate(automobili):
    if len(auto) == 3:
        print(auto)


#Dodati novu vrednost u listu
automobili.append("Mercedes")

#Izmeniti vrednost
automobili[2] = "Opel corsa"
print(automobili)
automobili[3] = "Kia sportage"
print(automobili)

#Izbrisati vrednost
del automobili [3]
print(automobili)

automobili.remove ("bmw")
print(automobili)

automobili.pop (0)
print(automobili)


broj_opela =0
for indeks in range (len(automobili)):
    if automobili[indeks] == "opel":
        print("Evo ga opel")
        broj_opela += 1

print ("Imam", broj_opela, "na placu")


#Izbrisati listu
automobili.clear()
print(automobili)




automobili = ["Citroen", "bmw", "opel", "kia", "yugo", "peugeot", "audi"]
automobili_akcija = []

for i in range(len(automobili)):
    if i == 1 or i == 2 or i == 3:
        automobili_akcija.append(automobili[i])

print (automobili_akcija)

automobili_akcija = automobili [1:4]
print (automobili_akcija)



brojevi = [1, 10, 12, 7, 3, 4, 2, 5]
parni = []
neparni = []
for broj in brojevi:
    if broj % 2 == 0:
        parni.append(broj)
    else:
        neparni.append(broj)

print(parni)
print(neparni)