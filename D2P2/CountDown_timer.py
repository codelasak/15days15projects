import time 
zaman = input("Sanyiye gir: ")

def zamanlayici(zaman): 
    while zaman:
        dk,s =divmod (zaman,60)
        timer= '{:02d}:{:02d}'.format(dk,s)
        print(timer,end="\r")
        time.sleep(1)
        zaman-=1
    print("Zaman bitti.")

    
zamanlayici(int(zaman))



