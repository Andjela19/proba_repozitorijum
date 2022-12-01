pozicija_automobila = 0
pozicija_cilja = 10

pozicija_automobila += 2
print (pozicija_automobila == pozicija_cilja)

pozicija_automobila += 2
print (pozicija_automobila == pozicija_cilja)

pozicija_automobila += 2
print (pozicija_automobila == pozicija_cilja)

pozicija_automobila += 2
print (pozicija_automobila == pozicija_cilja)

pozicija_automobila += 2
print (pozicija_automobila == pozicija_cilja)



for sledeci in ["marko", "milos", "marija", "ana", "sofija"]:
    print ("Hello", sledeci)

print ("Prva sledeca linija")

for broj in [1, 2, 3, 4, 5]:
    print ("ovo je broj:", broj)


for broj in range (1, 21):
    print ("Stampanje broja:", broj)

for broj in range (5, 10, 2):
    print(broj)

for broj in range (100, 0, -10):
    print(broj)


pozicija_automobila = 0
pozicija_cilja = 10

for kretanje in range (5):
    pozicija_automobila += 2
    print (pozicija_automobila == pozicija_cilja)



start_date = 2010
end_date = 2015
for godine in range (2010, 2016):
    print (godine)

pocetna_godina = 2010
zavrsna_godina = 2016
for godina in range (pocetna_godina, zavrsna_godina):
    print (godina)


for zvezda in range (10):
    print("**", end ="")

print()


for godina in range (zavrsna_godina, pocetna_godina, -1):
    print (godina)




print("1\t2\t3\t")
print("*****************")

print(1*1, end= "\t")
print(1*2, end= "\t")
print(1*3, end= "\n")

print(2*1, end= "\t")
print(2*2, end= "\t")
print(2*3, end= "\n")

print(3*1, end= "\t")
print(3*2, end= "\t")
print(3*3, end= "\n")

#print("Ovo je kurs \"Pajton\"")


for brojac in range (1, 6):
    print (brojac * 1, end = "\t")
    print (brojac * 2, end = "\t")
    print (brojac * 3, end = "\t")
    print (brojac * 4, end = "\n")



for x in range (6):
    for y in range (6):
        print ("*", end =" ")
    print ()


for x in range (2,5):
    for y in range (6,8):
        print( x * y, end = " ")
    print ()


for x in range (6):
    for y in range (6):
        if x == y:
            print ("*", end = " ")
        else:
            print ("#", end = " ")
    print ()
#print ("*" if x == y else "#", end = " ")



for x in range (10):
    for y in range (10):
        if x == 0 or x == 9 or y == 0 or y == 9:
            print ("#", end = " ")
        else:
            print (" ", end = " ")
    print ()