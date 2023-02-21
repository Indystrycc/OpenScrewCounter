from machine import Pin, ADC, Timer, PWM
from time import sleep
import time

motor = PWM(Pin(16))
motor.freq(1000)

buzzer = Pin(2, Pin.OUT)

DIS_A = Pin(19, Pin.OUT)
DIS_B = Pin(10, Pin.OUT)
DIS_C = Pin(12, Pin.OUT)
DIS_D = Pin(14, Pin.OUT)
DIS_E = Pin(15, Pin.OUT)
DIS_F = Pin(20, Pin.OUT)
DIS_G = Pin(11, Pin.OUT)
DIS_DP = Pin(13, Pin.OUT)

DIS_DIG_1 = Pin(18, Pin.OUT)
DIS_DIG_2 = Pin(21, Pin.OUT)
DIS_DIG_3 = Pin(22, Pin.OUT)

dis_value = 0

all_segments = [DIS_A, DIS_B, DIS_C, DIS_D, DIS_E, DIS_F, DIS_G, DIS_DP]
segments = {
    0: [DIS_A, DIS_B, DIS_C, DIS_D, DIS_E, DIS_F],
    1: [DIS_B, DIS_C],
    2: [DIS_A, DIS_B, DIS_G, DIS_E, DIS_D],
    3: [DIS_A, DIS_B, DIS_C, DIS_D, DIS_G],
    4: [DIS_F, DIS_G, DIS_B, DIS_C],
    5: [DIS_A, DIS_F, DIS_G, DIS_C, DIS_D],
    6: [DIS_A, DIS_F, DIS_E, DIS_D, DIS_C, DIS_G],
    7: [DIS_A, DIS_B, DIS_C],
    8: [DIS_A, DIS_B, DIS_C, DIS_D, DIS_E, DIS_F, DIS_G],
    9: [DIS_A, DIS_B, DIS_C, DIS_D, DIS_F, DIS_G]
}

def pad_with_zeros(number, length=3):
    number_str = str(number)
    while len(number_str) < length:
        number_str = '0' + number_str
    return number_str

def display_number(number):
    # Convert the number to a string and pad it with leading zeros if necessary
    number_str = pad_with_zeros(number)
    # Loop through each digit
    for i in range(3):
        # Activate the appropriate digit pin
        if i == 0:
            DIS_DIG_1.value(1)
            DIS_DIG_2.value(0)
            DIS_DIG_3.value(0)
        elif i == 1:
            DIS_DIG_1.value(0)
            DIS_DIG_2.value(1)
            DIS_DIG_3.value(0)
        else:
            DIS_DIG_1.value(0)
            DIS_DIG_2.value(0)
            DIS_DIG_3.value(1)
        # Get the segments for the current digit
        segments_for_digit = segments[int(number_str[i])]
        # Turn on the segments for the current digit
        for segment in segments_for_digit:
            segment.value(0)
        # Wait for a short time to allow the human eye to see the digits
        sleep(0.002)
        # Turn off the segments for the current digit
        for segment in all_segments:
            segment.value(1)
            
def timer_callback(timer):
    display_number(dis_value)


led = Pin(25, Pin.OUT)
sen = machine.ADC(26)
print('ready')
timer= Timer(mode=Timer.PERIODIC, period=5, callback=timer_callback)


def motorOn():
    motor.duty_u16(50000)


def motorOff():
    motor.duty_u16(0)


def countOneScrew():
    motorOn()
    while(sen.read_u16() < 13000):
        pass
    motorOff()
    sleep(0.02)
    return True

        
def countScrews(amount):
    global dis_value
    counter = 0
    for x in range(amount):
        countOneScrew()
        counter += 1
        dis_value = counter
        
def beep():
    for x in range(2):
        buzzer.on()
        sleep(0.1)
        buzzer.off()
        sleep(0.05)

while(1):
    dis_value = 0
    countScrews(10)
    sleep(0.3)
    beep()
    sleep(3)
