from machine import Pin
from time import sleep

dig1 = Pin(2, Pin.OUT)
dig2 = Pin(3, Pin.OUT)
dig3 = Pin(4, Pin.OUT)

digits = [dig1, dig2, dig3]

A = Pin(5, Pin.OUT)
B = Pin(6, Pin.OUT)
C = Pin(7, Pin.OUT)
D = Pin(8, Pin.OUT)
E = Pin(9, Pin.OUT)
F = Pin(10, Pin.OUT)
G = Pin(11, Pin.OUT)
elements = [A, B, C, D, E, F, G]

buz = Pin(12, Pin.OUT)

dig1.value(1)
dig2.value(1)
dig3.value(1)

while True:
        for e in elements:
            e.value(0)
            sleep(0.1)
        sleep(1)
        for e in elements:
            e.value(1)
        buz.value(1)
        sleep(0.1)
        buz.value(0)
        sleep(0.1)
        buz.value(1)
        sleep(0.1)
        buz.value(0)
        sleep(0.1)
        buz.value(1)
        sleep(0.1)
        buz.value(0)
        sleep(0.1)