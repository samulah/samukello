##Author Samu Lahdenperä
##Kello

import time

def kello():
    sekunti = 0
    minuutti = 0
    tunti = 0
    while True:
        print("Kellonaika jos sekunti kestäisi 60 millisekuntia {0}:{1}:{2}".format(tunti, minuutti, sekunti))
        time.sleep(0.6)
        sekunti +=1
        if sekunti == 60:
            sekunti = 0
            minuutti += 1
            if minuutti == 100:
                minuutti = 0
                tunti += 1
                if tunti == 24:
                    tunti = 0
        ##time.sleep(60.0 - ((time.time() - starttime) % 60.0))

    return

def main():
    kello()
    return None


main()
