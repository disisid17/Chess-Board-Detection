import time
from pigtest import angler
import RPi.GPIO as GPIO
from uites import coord_Move as cords
# Pin configuration
# SERVO_PINz = {16,23,24,18}  # Replace with the GPIO pin connected to the servo
# freq=50
# # GPIO setup
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(SERVO_PINz, GPIO.OUT)
# piv = GPIO.PWM(16, freq)  # 50Hz frequency
# piv.start(7)
# #time.sleep(0.3)
# big = GPIO.PWM(24, freq)  # 50Hz frequency
# big.start(8.11)
# #time.sleep(0.3)
# small = GPIO.PWM(23, freq)  # 50Hz frequency
# small.start(8.11)
# #time.sleep(0.3)
# grip = GPIO.PWM(18, freq)  # 50Hz frequency
# grip.start(4.222)
# #time.sleep(0.3)


#     #GPIO.output(pin, False)

# def SetAngle(angle,pin):
#     # Convert angle to duty cycle (0-100%)
#     duty = angle / 18 + 2
#     match pin:
#       case 16:
#         piv.ChangeDutyCycle(duty)
#       case 24:
#         big.ChangeDutyCycle(duty)
#       case 23:
#         small.ChangeDutyCycle(duty)
#       case 18:
#         grip.ChangeDutyCycle(duty)
      
   
    #pwm.ChangeDutyCycle(duty)
    #time.sleep(0.2)
    #GPIO.output(pin, False)
    #pwm.ChangeDutyCycle(0)
    #pwm.stop()
# Initialize PWM
  # Center position (1.5ms pulse)
def pivot(ang):
    angler(min(max(2*ang+90,0),180),0)
def open():
   angler(60,3)#gripper
    # Turn servo 40 degrees from center
def close():
    angler(5,3)#gripper
    # Turn servo 40 degrees from center
def fanc(ang,pinz,time):
    pass
  # 1 degree = ~0.055 duty cycle
#SetAngle(140,16)#base
# pivot(-90)#small arm
# time.sleep(1)
# pivot(90)# big arm
# time.sleep(1)
# pivot(0)#gripper
# open()
# time.sleep(1)
# SetAngle(160,24)# big arm
# SetAngle(110,23)#small arm
# time.sleep(0.5)
# close()
# # 8 inches
# time.sleep(3)
# SetAngle(140,24)
# SetAngle(100,23)#small arm
# # 6.5 inches
# time.sleep(3)
# SetAngle(130,24)
# SetAngle(100,23)#small arm
#4.5 inches
#pivot(0)
# open()
# time.sleep(1)
# close()
# for i in range(0,160):
#     angler(160-i/2,2)
#     angler(100-i/6,1)
#     time.sleep(0.005)
# time.sleep(1)
# open()
# time.sleep(1)
# angler(160,2)
# angler(100,1)
# time.sleep(1)

# close()

while True:
    inits,sec = input("cords: ").split(",")
    cords(int(inits),int(sec))
# open()#base
# time.sleep(2)
# close()#base
time.sleep(1)
#SetAngle(0,18)#gripper

