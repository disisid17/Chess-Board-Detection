from adafruit_servokit import ServoKit
import time
speed1 = 0.001
speed2 = 0.001
kit = ServoKit(channels=16)
def sprin(top,t2=None):
    print(top,t2)
    return t2
def angler(angl,pin,ang2=None,pi2=None):
    if ang2==None and pi2 == None:
        # sta= int(kit.servo[pin].angle)
        # angl= int(angl)
        # #print(sta,angl)
        # if angl>sta:
        #     for i in range(sta, angl):
        #         #print(i)
        #         kit.servo[pin].angle = i
        #         time.sleep(0.01)
        # elif angl<sta:
        #     for i in range(0, sta-angl):
        #         #print(sta-i)
        #         kit.servo[pin].angle = sta-i
        #         time.sleep(0.01)
        sta= int(kit.servo[pin].angle)
        angl= int(angl)
        while angl != sta:
            if angl > sta:
                sta += 1
            elif angl < sta:
                sta -= 1
            kit.servo[pin].angle = sta
            time.sleep(0.01)
    else:
            sta= int(kit.servo[pin].angle)
            st2 = int(kit.servo[pi2].angle)
            angl= int(angl)
            ang2 = int(ang2)

            while sta != angl or st2 != ang2:
                

                if sta != angl:
                    if sta < angl:
                        sta += 1
                    elif sta > angl:
                        sta -= 1
                    kit.servo[pin].angle = sta

                if st2 != ang2:
                    
                    if st2 < ang2:
                        st2 += 1
                    elif st2 > ang2:
                        st2 -= 1
                    kit.servo[pi2].angle = st2

                time.sleep(0.005)

    
    
    #time.sleep(0.05)
    #print("Moved"),




if __name__ == "__main__":
    while True:
        angler(0,0)
        #angler(0,1)
        time.sleep(1)
        angler(90,0)
        #angler(90,1)
        time.sleep(1)
        angler(180,0)
        #angler(180,1)
        time.sleep(1)
        angler(90,0)
        #angler(90,1)
        time.sleep(1)

        print("Moved")