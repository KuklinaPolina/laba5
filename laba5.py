import random


def a51():
    A = random.randint(0,100)
    B = random.randint(0, 100)
    C = random.randint(0, 100)
    D = random.randint(0, 100)
    E = random.randint(0, 100)
    S = [A, B, C, D, E]
    N = int(input("Vvedite chislo dla sravnenia"))
    if N in S:
        print("Posdravlay, vi ygadali chislo")
        print("Vashe chislo: ", N, ", spisok: ", S)
    else:
        print("Net takogo chisla")
        print("Vashe chislo: ", N, ", spisok: ", S)
def b52():
    A = random.randint(1, 5)
    B = random.randint(1, 5)
    C = random.randint(1, 5)
    D = random.randint(1, 5)
    E = random.randint(1, 5)
    S = [A, B, C, D, E]
    N = {x for x in S if S.count(x)>1}
    print("Spisok: ", S)
    if N == 0:
        print("Povtoraetsa chislo:", N)
    else:
        print("Chisla ne povtoraytsa")
def c53():
    A = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")
    B = int(input("Ckolko vixodnix vi xotite? "))
    if B == 1:
        print("Vi ne otdixaete")
        print("Vashi rabochie dni: ", A[0], A[1], A[2], A[3], A[4], A[5], A[6])
    if B == 1:
        print("Vashi vixodnie dni: ", A[6])
        print("Vashi rabochie dni: ", A[0], A[1], A[2], A[3], A[4], A[5])
    if B == 2:
        print("Vashi vixodnie dni: ", A[5], A[6])
        print("Vashi rabochie dni: ", A[0], A[1], A[2], A[3], A[4])
    if B == 3:
        print("Vashi vixodnie dni: ", A[4], A[5], A[6])
        print("Vashi rabochie dni: ", A[0], A[1], A[2], A[3])
    if B == 4:
        print("Vashi vixodnie dni: ", A[3], A[4], A[5], A[6])
        print("Vashi rabochie dni: ", A[0], A[1], A[2])
    if B == 5:
        print("Vashi vixodnie dni: ", A[2], A[3], A[4], A[5], A[6])
        print("Vashi rabochie dni: ", A[0], A[1])
    if B == 6:
        print("Vashi vixodnie dni: ", A[1], A[2], A[3], A[4], A[5], A[6])
        print("Vashi rabochie dni: ", A[0])
    if B == 6:
        print("Vashi vixodnie dni: ", A[0], A[1], A[2], A[3], A[4], A[5], A[6])
        print("Vi ne rabotaete")
def d54():
    a = ("Krishtal", "Ponomarenko", "Larionova", "Chikurova", "Korolyova", "Ivanov", "Melnikov", "Kuklina","Epifanova", "Kalinin")
    b = ("Ivanov", "Ivanov", "Cirov", "Xarov", "Susoev", "Petrov", "Lebedev", "Zverev", "Farudi", "Polikova")
    c = tuple(a[:5]+b[:5])
    print("Spisok pervoi grup: ", a)
    print("Spisok vtoroi grup: ", b)
    print("Spisok sport komandi: ", c)
    d = len(c)
    print("Kollichestvo igrokov: ", d)
    e = sorted(c)
    print("Spisok po alfavitu: ", e)
    f = c.count("Ivanov")
    if f != 0:
        print("V komande ", f, "chelovek c familiei Ivanov")
    else:
        print("V komande net ni odnogo Ivanova")
