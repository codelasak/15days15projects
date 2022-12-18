import random
tahmin = None
num = random.randint(0, 9)
kere =0
while num != tahmin:
    kere +=1
    tahmin= int (input("guess a number between 1 and 10: "))
    if tahmin == num:
        
        print("congratulations! you won!")
        print(kere)
    else:
        print("nope, sorry. try again!") 

        


