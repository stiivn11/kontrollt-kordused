
n = int(input("Sisesta number 1-9 "))
if 1 <= n <= 9:
    for i in range(n):
        print(" Ä ")
        print(" / \\ ")  
        print(" | | ")
        print("  __")
        if i != n - 1:
            print()
else:
    print("Viga Number peab olema vahemikus 1 kuni 9.")


import random

k = 12  
total_summa = 0
count = 0

for kuud in range(k):
    kulu = random.randint(5, 20)
    total_summa += kulu
    count += 1

keskmine = total_summa / count
print("Aastane keskmine kulusumma", keskmine)


M = int(input("Sisesta materjali pikkus meetrites: "))
jääk = M
while True:
    pikkus = int(input("Sisesta tükikese pikkus või 0 lõpetamiseks: "))
    if pikkus == 0:
        break
    if pikkus > jääk:
        print("Materjali ei ole piisavalt.")
    else:
        jääk -= pikkus
        print("Ülejäänud materjal:", jääk)


L = int(input("Sisesta L väärtus: "))
H = int(input("Sisesta H väärtus: "))

i = 0
while i < L:
    j = 0
    rida = ""
    while j < H:
        arv = random.randint(0, 100)
        rida += str(arv) + " "
        j += 1
    print(rida)
    i += 1  


n = int(input("Sisesta töötajate arv "))
A = int(input("Sisesta palk piirmäär eurodes "))

i = 0
pensioniealised = 0
while i < n:
    palk = random.randint(300, 2000)
    vanus = random.randint(20, 70)
    if palk > A and vanus >= 60:
        pensioniealised += 1
    i += 1

print("Töötajate arv, kelle palk ületab", A, "ja kes on pensioniealised", pensioniealised)