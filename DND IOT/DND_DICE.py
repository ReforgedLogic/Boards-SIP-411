from m5stack import *
from m5ui import *
from uiflow import *
import time
import imu

setScreenColor(0x111111)


i = None
Key = None
n = None
Val = None
img = None

imu0 = imu.IMU()

image0 = M5Img(0, 0, "res/dndlnd2.png", True)
label1 = M5TextBox(97, 17, "00", lcd.FONT_DejaVu72, 0xacacac, rotate=90)
label0 = M5TextBox(50, 132, "Dice", lcd.FONT_DejaVu40, 0xacacac, rotate=90)

import random



def buttonB_wasReleased():
  global i, Key, n, Val, img
  i = i - 1
  wait(0.5)
  n = i % len(Key)
  label0.setText(str(Key[int(n - 1)]))
  pass
btnB.wasReleased(buttonB_wasReleased)

def buttonA_wasReleased():
  global i, Key, n, Val, img
  i = i + 1
  wait(0.5)
  n = i % len(Key)
  label0.setText(str(Key[int(n - 1)]))
  pass
btnA.wasReleased(buttonA_wasReleased)


wait(0.2)
Key = ['D3', 'D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100']
Val = [3, 4, 6, 8, 10, 12, 20, 99]
img = [None, None, None]
i = 0
while True:
  if (imu0.acceleration[0]) > 1.5:
    label1.setText(str(random.randint(1, Val[int(n - 1)])))
    M5Led.on()
    wait_ms(1)
  elif (imu0.acceleration[0]) < 1.5:
    M5Led.off()
  wait_ms(2)