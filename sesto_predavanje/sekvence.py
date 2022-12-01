osoba = ["Sofija", 20, "plava", True]
print (osoba)

print (osoba [0])
print ("Godine: ", osoba [1])

automobili = ["Opel", "Citroen", "Mercedes"]
print (automobili [1])


for x in range (10, 2, -1):
    print (x, end = "")
print ()

kurs = "pajton"
print (kurs [0])
print (kurs [1])
print (kurs [2])

for x in range (6):
    print (kurs [x])

for x in range (len(kurs)):
    print (kurs [x])


ustanova = "IT academy"
for indeks in range (len(ustanova)):
    print (ustanova[indeks])


primer = "Zadatak1"
for y in range (len(primer)):
    print(primer [y], end ="")
print()

broj_karaktera = len(primer)
print(broj_karaktera)
indeks = 0

while indeks < broj_karaktera:
    print (primer[indeks])
    indeks += 1


korisnicko_ime = "admin"
uneto_kor_ime = input("Unesite koricnicko ime: ")
if korisnicko_ime == uneto_kor_ime.lower():
    print ("Dobro dosli")
else:
    print ("Pogresni podaci")
