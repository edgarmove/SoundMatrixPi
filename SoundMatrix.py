import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

MATRIX = [ [1,2,3,4],
           [5,6,7,8],
           [9,10,11,12],
           [13,14,15,16] ]

#gpio pin numbers
#input rows
ROW = [12,16,20,21]
#output columns
COL = [18,23,24,25]

#define four outputs and set to high
for j in range(4):
    GPIO.setup(COL[j], GPIO.OUT)
    GPIO.output(COL[j], 1)

#define four inputs with pull up resistor
for i in range(4):
    GPIO.setup(ROW[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)



try:
    while(True):
        for j in range(4):
            #set each output pin to low
            GPIO.output(COL[j],0)
            for i in range(4):
                if GPIO.input(ROW[i]) == 0:
                    print MATRIX[i][j]
                    while(GPIO.input(ROW[i]) == 0):
                        pass
            #return each output pin to high
            GPIO.output(COL[j],1)
except KeyboardInterrupt:
    GPIO.cleanup()
