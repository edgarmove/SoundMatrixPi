# a 4x4 button matrix

import RPi.GPIO as GPIO
import pygame.mixer
from time import sleep
from sys import exit

GPIO.setmode(GPIO.BCM)

pygame.mixer.init(48000, -16, 1, 1024)

soundA = pygame.mixer.sound("/home/pi/python_games/match0.wav")

soundChannelA = pygame.mixer.Channel(1)


ButtonIDs = [ [1,2,3,4],
           [5,6,7,8],
           [9,10,11,12],
           [13,14,15,16] ]

# gpio inputs for rows
RowPins = [12,16,20,21]

# gpio outputs for columns
ColumnPins = [17,4,3,2]

# define four outputs and set to high
for j in range(len(ColumnPins)):
    GPIO.setup(ColumnPins[j], GPIO.OUT)
    GPIO.output(ColumnPins[j], 1)

# define four inputs with pull up resistor
for i in range(len(RowPins)):
    GPIO.setup(RowPins[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)

def ActivateButton(rowPin, colPin):
    PlaySound(soundA, soundChannelA)
    print ButtonIDs[rowPin][colPin]
    sleep(.01)
def PlaySound(sound, soundChannel):
    soundChannel.play(sound)

try:
    while(True):
        for j in range(len(ColumnPins)):
            # set each output pin to low
            GPIO.output(ColumnPins[j],0)
            for i in range(len(RowPins)):
                if GPIO.input(RowPins[i]) == 0:
                    ActivateButton(i,j)
                    while(GPIO.input(RowPins[i]) == 0):
                        pass
            # return each output pin to high
            GPIO.output(ColumnPins[j],1)
except KeyboardInterrupt:
    GPIO.cleanup()
    exit()
