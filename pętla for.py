from turtle import *
from time import *

odpowiedz = input("Aby uruchomić pętle napisz tak")

#Wyjście z pętli
while odpowiedz == "tak":
    print("i")
    if odpowiedz == "tak":
        break

#Narysowanie trójkątu
for i in range(3):
    forward(100)
    right(120)

sleep(5)

#Wypisanie co 2 liczbyt od 2 do 10
for i in range(2, 11, 2):
    print(i, end=" ")