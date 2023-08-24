from machine import Pin,PWM
import utime

FLF = Pin(6,Pin.OUT)
FLB = Pin(7,Pin.OUT)
FRF = Pin(27,Pin.OUT)
FRB = Pin(26,Pin.OUT)

RLF = Pin(8,Pin.OUT)
RLB = Pin(9,Pin.OUT)
RRF = Pin(21,Pin.OUT)
RRB = Pin(20,Pin.OUT)

FLD = PWM(Pin(2))
FLD.freq(50)

FRD = PWM(Pin(5))
FRD.freq(50)

RLD = PWM(Pin(3))
RLD.freq(50)

RRD = PWM(Pin(4))
RRD.freq(50)

def servo(deg):
  if ((deg>=0)&(deg<=180)):
    return(1500+ int(deg*36.11111))

motors = [FLF,FLB,FRF,FRB,RLF,RLB,RRF,RRB]

while True:
  for i in range(0,8,1):
    motors[i].high()
    utime.sleep(2)
    motors[i].low()
  print("Cycle is completed")
