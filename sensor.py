from gpiozero import MotionSensor
from gpiozero import LED
import time
white_led=LED(17)
import requests
url1 = 'http://localhost:3001/detected' 
url2 = 'http://localhost:3001/notdetected' 
mvs= MotionSensor(4)
white_led.off()
print("start")
while True:
        mvs.wait_for_motion()
        print("Motion detected")
        r1=requests.post(url1)     
        print(r1)     
        white_led.on()
        time.sleep(30)
        mvs.wait_for_no_motion()
        white_led.off()
        print("No motion detected")
        r2=requests.post(url2)     
        print(r2) 

# def motion():
#     print("Motion detected")
#     r1=requests.post(url1)     
#     print(r1)     
# motion()
# def nomotion():
#     print("no Motion detected")
#     r2=requests.post(url2)     
#     print(r2)     
# nomotion()
 
 
