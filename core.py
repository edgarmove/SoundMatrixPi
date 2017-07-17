# a 4x4 button matrix
# each button plays a sound, up to 6 can play simultaneously

import RPi.GPIO as GPIO
import pygame.mixer
from time import sleep
from sys import exit
import os
import sounds

print("sound matrix is running...")

GPIO.setmode(GPIO.BCM)

ButtonIDs = [ [1,2,3,4,5,6,7],
           [8,9,10,11,12,13,14],
           [15,16,17,18,19,20,21] ]

# gpio inputs for rows
RowPins = [16,20,21]

# gpio outputs for columns
ColumnPins = [26,19,13,6,5,22,27]

# gpio input for shutdown button pin
ShutdownPin = 12

# set maximum number of channels to 5
pygame.mixer.set_num_channels(6)

# define four inputs with pull up resistor
for i in range(len(RowPins)):
    GPIO.setup(RowPins[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)

# define four outputs and set to high
for j in range(len(ColumnPins)):
    GPIO.setup(ColumnPins[j], GPIO.OUT)
    GPIO.output(ColumnPins[j], 1)

# define input for shutdown button pin
GPIO.setup(ShutdownPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def ActivateButton(rowPin, colPin):
    sndIndex = ButtonIDs[rowPin][colPin] - 1
    PlaySound(sounds.SoundsList[sndIndex])
    print(sndIndex + 1)
    # prevent button presses too close together
    sleep(.3)

def PlaySound(sound):
    # get next available sound channel
    # True arg override returns longest running
    # sound channel when none are available
    nextAvailableChannel = pygame.mixer.find_channel(True)

    # channel should techincally never be null because above arg is True
    # null checking just in case
    if nextAvailableChannel != None and nextAvailableChannel.get_busy() == False:
        nextAvailableChannel.play(sound) 
       
def EndScript():
    GPIO.cleanup()
    print("sound matrix is exiting...")
    exit()

def ShutdownSystem():
    # slowly stop pygame operations and shutdown the RPi
    sleep(1)
    pygame.mixer.stop()
    sleep(.5)
    pygame.mixer.quit()
    sleep(1)
#    os.system('shutdown now -h')

# comment this out to run script
#EndScript()

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

        # listen for shutdown button
        shutdownInputValue = GPIO.input(ShutdownPin)
        if (shutdownInputValue == False):
            ShutdownSystem()
except KeyboardInterrupt:
    EndScript()
