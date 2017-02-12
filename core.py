# a 4x4 button matrix
# plays a sound and prints the button id for each button

import RPi.GPIO as GPIO
import pygame.mixer
from time import sleep
from sys import exit
import sounds

# comment this out to run script
#EndScript()

GPIO.setmode(GPIO.BCM)

ButtonIDs = [ [1,2,3,4],
           [5,6,7,8],
           [9,10,11,12],
           [13,14,15,16] ]

# gpio inputs for rows
RowPins = [12,16,20,21]

# gpio outputs for columns
ColumnPins = [17,4,3,2]

# gpio outputs for LEDs
LEDPins = [27,22,10,9]

# set maximum number of channels to 5
pygame.mixer.set_num_channels(6)

# define four inputs with pull up resistor
for i in range(len(RowPins)):
    GPIO.setup(RowPins[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)

# define four outputs and set to high
for j in range(len(ColumnPins)):
    GPIO.setup(ColumnPins[j], GPIO.OUT)
    GPIO.output(ColumnPins[j], 1)

# define four outputs
for k in range(len(LEDPins)):
    GPIO.setup(LEDPins[k], GPIO.OUT)

def ActivateButton(rowPin, colPin):
    sndIndex = ButtonIDs[rowPin][colPin] - 1
    PlaySound(sounds.SoundsList[sndIndex])
    print(sndIndex + 1)
    sleep(.3)

def PlaySound(sound):
    nextAvailableChannel = pygame.mixer.find_channel(True) # get next available channel
    if nextAvailableChannel != None and nextAvailableChannel.get_busy() == False:
        nextAvailableChannel.play(sound) # play sound on that channel
       
def EndScript():
    GPIO.cleanup()
    exit()

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
    EndScript()
