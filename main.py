import time
import board
from digitalio import DigitalInOut, Direction

digital_in = DigitalInOut(board.D7)
led = DigitalInOut(board.D2)
led.direction = Direction.OUTPUT
noise_count = 0
current_value = 0
old_value = 0

def get_voltage(pin):
    return pin.value#* 3.3) / 65536

#while True:
    #print((get_voltage(digital_in),))
    #time.sleep(0.1)

THRESHOLD = 3000
DELAY_SECONDS = 0.05
TOTAL_RECORD_TIME = 10.0
elapsedTime = 0.0
oldTime = time.monotonic()
data = []


def readDigitalPin():
    return digital_in.value

def thresholdValue(value):
    if(value > THRESHOLD):
        return 1
    else:
        return 0


while (elapsedTime < TOTAL_RECORD_TIME):
    currentTime = time.monotonic()
    pinValue = readDigitalPin()
    recordValue = pinValue#thresholdValue(pinValue)

    #print("{0},{1}".format(elapsedTime, recordValue))
    data.append([elapsedTime,recordValue])

    time.sleep(DELAY_SECONDS)
    elapsedTime += currentTime - oldTime
    oldTime = currentTime

    #led.value = not led.value
for row in data:
    #print("{0},{1}".format(row[0], row[1]))
    current_value = str(row[1])
        
    if old_value == "False" and current_value == "True":
        noise_count += 1
    old_value = current_value

print(f'Counted {noise_count} noises.')
if noise_count >= 3:
    led.value = True
    time.sleep(2.0)
    led.value = False
