import random

kurs = ("Python fundamentals")
print (kurs)


a= 10
b= 5
print (a + b)

rezultat_sabiranja = a + b
print (rezultat_sabiranja)
print("oduzimanje:", a - b)
print ("mnozenje:", a*b)
print ("deljenje:", a/b)
print ("deljenje:", int(a/b))

print ("celobrojno deljenje:", a//b)
print (10//3)
print (10/3)

print (a ** 2) # a*a
print (a **3) # a*a*a

print (10 % 3)
print (8 % 2)

print (-a)


godine = 25
print (godine + 1)

godine = godine + 1
print (godine)

godine += 1
print (godine)

godine -= 5
print (godine)

godine *= 2
print (godine)

godine /= 2
print (godine)










#broj1 = 15
#broj2 = 20
#print ("Zbir:", broj1 + broj2)


# broj1 = int(input("Unesite prvi broj: " ))
# print (broj1)

# broj2 = int(input("Unesite drugi broj: "))
# print (broj2)

# print ("Rezultat:", broj1 + broj2)


# poluprecnik = float(input("Unesite poluprecnk: "))
# pi = 3.14
# povrsina = poluprecnik ** 2 * pi
# print ("Povrsina kruga je:", povrsina)


stara_kilaza = 80
nova_kilaza = 99
print (stara_kilaza > nova_kilaza)
print (stara_kilaza < nova_kilaza)
print (nova_kilaza == 100)
print (nova_kilaza !=100)
print (stara_kilaza >= 80)
print (stara_kilaza <= 80)


username = "Test"
password = "abc123"

print (username == "Test")
print (password == "ABC123")



# broj = int(input("Unesite broj" ))
# provera = broj % 2
# print ("Paran je:", provera ==0)



# korisnik = int(input("Unesite broj: "))
# racunar = random.randint (1, 10)

# print ("Korisnik:", korisnik)
# print ("Racunar:", racunar)
# print ("Pogodak:", korisnik == racunar)



# automobil = 0
# cilj = 50
# print (automobil >= cilj)

# automobil += 10
# print (automobil >= cilj)

# automobil += 10
# automobil += 20
# automobil += 25
# print (automobil >= cilj)



provera_imena = True
provera_sifre = True
print (provera_imena and provera_sifre)

provera_imena1 = True
provera_sifre1 = False
print (provera_imena1 and provera_sifre1)

print (provera_imena1 or provera_sifre1)

lepo_vreme = True
print (not lepo_vreme)



kurs = input("Unesite kurs: ")
generacija = int(input("Generacija: "))

Odobreno = kurs == "python" and generacija == 2022
print (Odobreno)

