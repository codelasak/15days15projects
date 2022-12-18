import random
tahmin= random.randint(0, 9)
num = int (input("guess a number between 1 and 10: "))

while num != tahmin:
    tahmin= random.randint(0, 9)
    print (tahmin)
    if tahmin == num:
        print("congratulations! you won!")
        
    else:
        print("nope, sorry. try again!") 

        


