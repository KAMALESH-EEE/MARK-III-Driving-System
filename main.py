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

fmotors = [FLF,RLF,FRF,RRF]
rmotors = [FLB,RLB,FRB,RRB]

def direction(deg):
  de=int(deg/2)
  FLD.duty_u16(servo(90-deg))
  RLD.duty_u16(servo(90-de))
  FRD.duty_u16(servo(90+deg))
  RRD.duty_u16(servo(90+de))

def forward():
  for m in fmotors:
    m.high()
  for m in rmotors:
    m.low()

def reverse():
  for m in rmotors:
    m.high()
  for m in fmotors:
    m.low()
  

while True:
  direction(60)
  forward()
  utime.sleep(5)
  direction(-60)
  reverse()
  utime.sleep(5)
