from adafruit_servokit import ServoKit
import time
kit = ServoKit(channels=16)
def angler(angle,pin):
    kit.servo[pin].angle = angle
    #time.sleep(0.05)
    #print("Moved"),




if __name__ == "__main__":
    while True:
        angler(0,0)
        angler(0,1)
        time.sleep(1)
        angler(90,0)
        angler(90,1)
        time.sleep(1)
        angler(180,0)
        angler(180,1)
        time.sleep(1)
        angler(90,0)
        angler(90,1)
        time.sleep(1)

        print("Moved")