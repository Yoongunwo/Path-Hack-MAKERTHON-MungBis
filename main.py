import serial
import RPi.GPIO as GPIO
import time
import random
from threading import Thread

ser = serial.Serial("/dev/ttyUSB0", 115200, timeout=1)

GPIO.setmode(GPIO.BCM)

GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)

GPIO.setup(21,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)

GPIO.setup(26, GPIO.OUT)

global curLed
global past_num
global random_num

def led(t) :
    global curLed

    if t == 't' :
        ti = 3
    else :
        ti = 5

    print("led")
    curTime = 0
    while curTime < ti :
        if curLed == 20 :
            GPIO.output(16, True)
            curLed = 21
        elif curLed == 21 :
            GPIO.output(20, True)
            curLed = 16
        elif curLed == 16 :
            GPIO.output(21, True)
            curLed = 20
        curTime = curTime + 0.5
        
        time.sleep(0.5)
    
def motor_on(random_num) :
    print("motor")
    if random_num == 1 :
        GPIO.output(23, True)
        GPIO.output(5, True)
    
    elif random_num == 2 :
        GPIO.output(24, True)
        GPIO.output(6, True)
        

    elif random_num == 3 :
        GPIO.output(23, True)
        GPIO.output(6, True)
    
    elif random_num == 4 :
        GPIO.output(24, True)
        GPIO.output(5, True)
    
def motor_off() :
    GPIO.output(23, False)
    GPIO.output(24, False)
    
    GPIO.output(5, False)
    GPIO.output(6, False)

def movement(t) : 
    global past_num
    global random_num

    if t == 't' :
        ti = 3
    else :
        ti = 5

    for i in range(0, ti) :
        while past_num == random_num :
            random_num = random.randrange(1,5)
        past_num = random_num

        motor_on(random_num)
        time.sleep(1)
        motor_off()
        

def active_machine(speak) :
    if speak == 'mungmung\x1b[0m\r\n' :
        print()
        three = 't'
        th1 = Thread(target=led, args=('t'))
        th2 = Thread(target=movement, args=('t'))
        th1.start()
        th2.start()
        th1.join()
        th2.join() 

    elif speak == "walwal\x1b[0m\r\n" :
        five = 'f'
        th1 = Thread(target=led, args=('f'))
        th2 = Thread(target=movement, args=('f'))
        th1.start()
        th2.start()
        th1.join()
        th2.join() 

def command() :

    return 

if __name__ == '__main__' :
    global curLed
    global past_num
    global random_num
    curLed = 16
    past_num = -1
    random_num = -1
    
    while True :
        rx = ser.readline().decode('ascii')
        rxSplit = rx.split(' ')

        print("Receive Data: ", rxSplit[3])

        active_machine(rxSplit[3])
        '''
        if rxSplit[3] == 'mungmung\x1b[0m\r\n' :
            time.sleep(3)
        elif rxSplit[3] == 'walwal\x1b[0m\r\n' :
            time.sleep(5)
        '''


        rx = ''

        GPIO.output(curLed, False)
        GPIO.output(5, False)  
        GPIO.output(6, False)
        GPIO.output(23, False)
        GPIO.output(24, False)
