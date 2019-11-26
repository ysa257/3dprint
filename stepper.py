import RPi.GPIO as GPIO
import time

def move_two_motors(out1, out2, out3, out4, out5, out6, out7, out8, speedracer, t, asd):
    i = 0
    positive = 0
    negative = 0
    y = 0
    start = time.time()
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(out1, GPIO.OUT)
    GPIO.setup(out2, GPIO.OUT)
    GPIO.setup(out3, GPIO.OUT)
    GPIO.setup(out4, GPIO.OUT)
    GPIO.setup(out5, GPIO.OUT)
    GPIO.setup(out6, GPIO.OUT)
    GPIO.setup(out7, GPIO.OUT)
    GPIO.setup(out8, GPIO.OUT)


    print("First calibrate by giving some +ve and -ve values.....")

    try:
        while (1) and (time.time()-start<t):
            GPIO.output(out1, GPIO.LOW)
            GPIO.output(out2, GPIO.LOW)
            GPIO.output(out3, GPIO.LOW)
            GPIO.output(out4, GPIO.LOW)
            GPIO.output(out5, GPIO.LOW)
            GPIO.output(out6, GPIO.LOW)
            GPIO.output(out7, GPIO.LOW)
            GPIO.output(out8, GPIO.LOW)

            x = asd*80  # input()
            if x > 0 and x <= 400:
                for y in range(x, 0, -1):
                    if negative == 1:
                        if i == 7:
                            i = 0
                        else:
                            i = i + 1
                        y = y + 2
                        negative = 0
                    positive = 1
                    # print((x+1)-y)
                    if i == 0:
                        GPIO.output(out1, GPIO.HIGH)
                        GPIO.output(out2, GPIO.LOW)
                        GPIO.output(out3, GPIO.LOW)
                        GPIO.output(out4, GPIO.LOW)
                        GPIO.output(out5, GPIO.HIGH)
                        GPIO.output(out6, GPIO.LOW)
                        GPIO.output(out7, GPIO.LOW)
                        GPIO.output(out8, GPIO.LOW)

                        time.sleep(speedracer)
                        # time.sleep(1)
                    elif i == 1:
                        GPIO.output(out1, GPIO.HIGH)
                        GPIO.output(out2, GPIO.HIGH)
                        GPIO.output(out3, GPIO.LOW)
                        GPIO.output(out4, GPIO.LOW)
                        GPIO.output(out5, GPIO.HIGH)
                        GPIO.output(out6, GPIO.HIGH)
                        GPIO.output(out7, GPIO.LOW)
                        GPIO.output(out8, GPIO.LOW)

                        time.sleep(speedracer)
                        # time.sleep(1)
                    elif i == 2:
                        GPIO.output(out1, GPIO.LOW)
                        GPIO.output(out2, GPIO.HIGH)
                        GPIO.output(out3, GPIO.LOW)
                        GPIO.output(out4, GPIO.LOW)
                        GPIO.output(out5, GPIO.LOW)
                        GPIO.output(out6, GPIO.HIGH)
                        GPIO.output(out7, GPIO.LOW)
                        GPIO.output(out8, GPIO.LOW)

                        time.sleep(speedracer)
                        # time.sleep(1)
                    elif i == 3:
                        GPIO.output(out1, GPIO.LOW)
                        GPIO.output(out2, GPIO.HIGH)
                        GPIO.output(out3, GPIO.HIGH)
                        GPIO.output(out4, GPIO.LOW)
                        GPIO.output(out5, GPIO.LOW)
                        GPIO.output(out6, GPIO.HIGH)
                        GPIO.output(out7, GPIO.HIGH)
                        GPIO.output(out8, GPIO.LOW)

                        time.sleep(speedracer)
                        # time.sleep(1)
                    elif i == 4:
                        GPIO.output(out1, GPIO.LOW)
                        GPIO.output(out2, GPIO.LOW)
                        GPIO.output(out3, GPIO.HIGH)
                        GPIO.output(out4, GPIO.LOW)
                        GPIO.output(out5, GPIO.LOW)
                        GPIO.output(out6, GPIO.LOW)
                        GPIO.output(out7, GPIO.HIGH)
                        GPIO.output(out8, GPIO.LOW)

                        time.sleep(speedracer)
                        # time.sleep(1)
                    elif i == 5:
                        GPIO.output(out1, GPIO.LOW)
                        GPIO.output(out2, GPIO.LOW)
                        GPIO.output(out3, GPIO.HIGH)
                        GPIO.output(out4, GPIO.HIGH)
                        GPIO.output(out5, GPIO.LOW)
                        GPIO.output(out6, GPIO.LOW)
                        GPIO.output(out7, GPIO.HIGH)
                        GPIO.output(out8, GPIO.HIGH)

                        time.sleep(speedracer)
                        # time.sleep(1)
                    elif i == 6:
                        GPIO.output(out1, GPIO.LOW)
                        GPIO.output(out2, GPIO.LOW)
                        GPIO.output(out3, GPIO.LOW)
                        GPIO.output(out4, GPIO.HIGH)
                        GPIO.output(out5, GPIO.LOW)
                        GPIO.output(out6, GPIO.LOW)
                        GPIO.output(out7, GPIO.LOW)
                        GPIO.output(out8, GPIO.HIGH)

                        time.sleep(speedracer)
                        # time.sleep(1)
                    elif i == 7:
                        GPIO.output(out1, GPIO.HIGH)
                        GPIO.output(out2, GPIO.LOW)
                        GPIO.output(out3, GPIO.LOW)
                        GPIO.output(out4, GPIO.HIGH)
                        GPIO.output(out5, GPIO.HIGH)
                        GPIO.output(out6, GPIO.LOW)
                        GPIO.output(out7, GPIO.LOW)
                        GPIO.output(out8, GPIO.HIGH)

                        time.sleep(speedracer)
                        # time.sleep(1)
                    if i == 7:
                        i = 0
                        continue
                    i = i + 1


            elif x < 0 and x >= -400:
                x = x * -1
                for y in range(x, 0, -1):
                    if positive == 1:
                        if i == 0:
                            i = 7
                        else:
                            i = i - 1
                        y = y + 3
                        positive = 0
                    negative = 1
                    # print((x+1)-y)
                    if i == 0:
                        GPIO.output(out1, GPIO.HIGH)
                        GPIO.output(out2, GPIO.LOW)
                        GPIO.output(out3, GPIO.LOW)
                        GPIO.output(out4, GPIO.LOW)
                        GPIO.output(out5, GPIO.HIGH)
                        GPIO.output(out6, GPIO.LOW)
                        GPIO.output(out7, GPIO.LOW)
                        GPIO.output(out8, GPIO.LOW)

                        time.sleep(speedracer)
                        # time.sleep(1)
                    elif i == 1:
                        GPIO.output(out1, GPIO.HIGH)
                        GPIO.output(out2, GPIO.HIGH)
                        GPIO.output(out3, GPIO.LOW)
                        GPIO.output(out4, GPIO.LOW)
                        GPIO.output(out5, GPIO.HIGH)
                        GPIO.output(out6, GPIO.HIGH)
                        GPIO.output(out7, GPIO.LOW)
                        GPIO.output(out8, GPIO.LOW)

                        time.sleep(speedracer)
                        # time.sleep(1)
                    elif i == 2:
                        GPIO.output(out1, GPIO.LOW)
                        GPIO.output(out2, GPIO.HIGH)
                        GPIO.output(out3, GPIO.LOW)
                        GPIO.output(out4, GPIO.LOW)
                        GPIO.output(out5, GPIO.LOW)
                        GPIO.output(out6, GPIO.HIGH)
                        GPIO.output(out7, GPIO.LOW)
                        GPIO.output(out8, GPIO.LOW)

                        time.sleep(speedracer)
                        # time.sleep(1)
                    elif i == 3:
                        GPIO.output(out1, GPIO.LOW)
                        GPIO.output(out2, GPIO.HIGH)
                        GPIO.output(out3, GPIO.HIGH)
                        GPIO.output(out4, GPIO.LOW)
                        GPIO.output(out5, GPIO.LOW)
                        GPIO.output(out6, GPIO.HIGH)
                        GPIO.output(out7, GPIO.HIGH)
                        GPIO.output(out8, GPIO.LOW)

                        time.sleep(speedracer)
                        # time.sleep(1)
                    elif i == 4:
                        GPIO.output(out1, GPIO.LOW)
                        GPIO.output(out2, GPIO.LOW)
                        GPIO.output(out3, GPIO.HIGH)
                        GPIO.output(out4, GPIO.LOW)
                        GPIO.output(out5, GPIO.LOW)
                        GPIO.output(out6, GPIO.LOW)
                        GPIO.output(out7, GPIO.HIGH)
                        GPIO.output(out8, GPIO.LOW)

                        time.sleep(speedracer)
                        # time.sleep(1)
                    elif i == 5:
                        GPIO.output(out1, GPIO.LOW)
                        GPIO.output(out2, GPIO.LOW)
                        GPIO.output(out3, GPIO.HIGH)
                        GPIO.output(out4, GPIO.HIGH)
                        GPIO.output(out5, GPIO.LOW)
                        GPIO.output(out6, GPIO.LOW)
                        GPIO.output(out7, GPIO.HIGH)
                        GPIO.output(out8, GPIO.HIGH)

                        time.sleep(speedracer)
                        # time.sleep()
                    elif i == 6:
                        GPIO.output(out1, GPIO.LOW)
                        GPIO.output(out2, GPIO.LOW)
                        GPIO.output(out3, GPIO.LOW)
                        GPIO.output(out4, GPIO.HIGH)
                        GPIO.output(out5, GPIO.LOW)
                        GPIO.output(out6, GPIO.LOW)
                        GPIO.output(out7, GPIO.LOW)
                        GPIO.output(out8, GPIO.HIGH)

                        time.sleep(speedracer)
                        # time.sleep(1)
                    elif i == 7:
                        GPIO.output(out1, GPIO.HIGH)
                        GPIO.output(out2, GPIO.LOW)
                        GPIO.output(out3, GPIO.LOW)
                        GPIO.output(out4, GPIO.HIGH)
                        GPIO.output(out5, GPIO.HIGH)
                        GPIO.output(out6, GPIO.LOW)
                        GPIO.output(out7, GPIO.LOW)
                        GPIO.output(out8, GPIO.HIGH)

                        time.sleep(speedracer)
                        # time.sleep(1)
                    if i == 0:
                        i = 7
                        continue
                    i = i - 1


    except KeyboardInterrupt:
        GPIO.cleanup()

def move_all_motors(out1, out2, out3, out4, out5, out6, out7, out8, out9, out10, out11, out12, speedracer, t, asd):

    # out1 = 13
    # out2 = 11
    # out3 = 15
    # out4 = 12
    # out5 = 5
    # out6 = 10
    # out7 = 3
    # out8 = 7
    # out9 = 16
    # out10 = 22
    # out11 = 8
    # out12 = 18


    # speedracer = 0.015
    
    i = 0
    positive = 0
    negative = 0
    y = 0
    start = time.time()
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(out1, GPIO.OUT)
    GPIO.setup(out2, GPIO.OUT)
    GPIO.setup(out3, GPIO.OUT)
    GPIO.setup(out4, GPIO.OUT)
    GPIO.setup(out5, GPIO.OUT)
    GPIO.setup(out6, GPIO.OUT)
    GPIO.setup(out7, GPIO.OUT)
    GPIO.setup(out8, GPIO.OUT)
    GPIO.setup(out9, GPIO.OUT)
    GPIO.setup(out10, GPIO.OUT)
    GPIO.setup(out11, GPIO.OUT)
    GPIO.setup(out12, GPIO.OUT)

    print("First calibrate by giving some +ve and -ve values.....")

    try:
        while (1) and (time.time()-start<t):
            GPIO.output(out1, GPIO.LOW)
            GPIO.output(out2, GPIO.LOW)
            GPIO.output(out3, GPIO.LOW)
            GPIO.output(out4, GPIO.LOW)
            GPIO.output(out5, GPIO.LOW)
            GPIO.output(out6, GPIO.LOW)
            GPIO.output(out7, GPIO.LOW)
            GPIO.output(out8, GPIO.LOW)
            GPIO.output(out9, GPIO.LOW)
            GPIO.output(out10, GPIO.LOW)
            GPIO.output(out11, GPIO.LOW)
            GPIO.output(out12, GPIO.LOW)
            x = asd*80  # input()
            if x > 0 and x <= 400:
                for y in range(x, 0, -1):
                    if negative == 1:
                        if i == 7:
                            i = 0
                        else:
                            i = i + 1
                        y = y + 2
                        negative = 0
                    positive = 1
                    # print((x+1)-y)
                    if i == 0:
                        GPIO.output(out1, GPIO.HIGH)
                        GPIO.output(out2, GPIO.LOW)
                        GPIO.output(out3, GPIO.LOW)
                        GPIO.output(out4, GPIO.LOW)
                        GPIO.output(out5, GPIO.HIGH)
                        GPIO.output(out6, GPIO.LOW)
                        GPIO.output(out7, GPIO.LOW)
                        GPIO.output(out8, GPIO.LOW)
                        GPIO.output(out9, GPIO.HIGH)
                        GPIO.output(out10, GPIO.LOW)
                        GPIO.output(out11, GPIO.LOW)
                        GPIO.output(out12, GPIO.LOW)
                        time.sleep(speedracer)
                        # time.sleep(1)
                    elif i == 1:
                        GPIO.output(out1, GPIO.HIGH)
                        GPIO.output(out2, GPIO.HIGH)
                        GPIO.output(out3, GPIO.LOW)
                        GPIO.output(out4, GPIO.LOW)
                        GPIO.output(out5, GPIO.HIGH)
                        GPIO.output(out6, GPIO.HIGH)
                        GPIO.output(out7, GPIO.LOW)
                        GPIO.output(out8, GPIO.LOW)
                        GPIO.output(out9, GPIO.HIGH)
                        GPIO.output(out10, GPIO.HIGH)
                        GPIO.output(out11, GPIO.LOW)
                        GPIO.output(out12, GPIO.LOW)
                        time.sleep(speedracer)
                        # time.sleep(1)
                    elif i == 2:
                        GPIO.output(out1, GPIO.LOW)
                        GPIO.output(out2, GPIO.HIGH)
                        GPIO.output(out3, GPIO.LOW)
                        GPIO.output(out4, GPIO.LOW)
                        GPIO.output(out5, GPIO.LOW)
                        GPIO.output(out6, GPIO.HIGH)
                        GPIO.output(out7, GPIO.LOW)
                        GPIO.output(out8, GPIO.LOW)
                        GPIO.output(out9, GPIO.LOW)
                        GPIO.output(out10, GPIO.HIGH)
                        GPIO.output(out11, GPIO.LOW)
                        GPIO.output(out12, GPIO.LOW)
                        time.sleep(speedracer)
                        # time.sleep(1)
                    elif i == 3:
                        GPIO.output(out1, GPIO.LOW)
                        GPIO.output(out2, GPIO.HIGH)
                        GPIO.output(out3, GPIO.HIGH)
                        GPIO.output(out4, GPIO.LOW)
                        GPIO.output(out5, GPIO.LOW)
                        GPIO.output(out6, GPIO.HIGH)
                        GPIO.output(out7, GPIO.HIGH)
                        GPIO.output(out8, GPIO.LOW)
                        GPIO.output(out9, GPIO.LOW)
                        GPIO.output(out10, GPIO.HIGH)
                        GPIO.output(out11, GPIO.HIGH)
                        GPIO.output(out12, GPIO.LOW)
                        time.sleep(speedracer)
                        # time.sleep(1)
                    elif i == 4:
                        GPIO.output(out1, GPIO.LOW)
                        GPIO.output(out2, GPIO.LOW)
                        GPIO.output(out3, GPIO.HIGH)
                        GPIO.output(out4, GPIO.LOW)
                        GPIO.output(out5, GPIO.LOW)
                        GPIO.output(out6, GPIO.LOW)
                        GPIO.output(out7, GPIO.HIGH)
                        GPIO.output(out8, GPIO.LOW)
                        GPIO.output(out9, GPIO.LOW)
                        GPIO.output(out10, GPIO.LOW)
                        GPIO.output(out11, GPIO.HIGH)
                        GPIO.output(out12, GPIO.LOW)
                        time.sleep(speedracer)
                        # time.sleep(1)
                    elif i == 5:
                        GPIO.output(out1, GPIO.LOW)
                        GPIO.output(out2, GPIO.LOW)
                        GPIO.output(out3, GPIO.HIGH)
                        GPIO.output(out4, GPIO.HIGH)
                        GPIO.output(out5, GPIO.LOW)
                        GPIO.output(out6, GPIO.LOW)
                        GPIO.output(out7, GPIO.HIGH)
                        GPIO.output(out8, GPIO.HIGH)
                        GPIO.output(out9, GPIO.LOW)
                        GPIO.output(out10, GPIO.LOW)
                        GPIO.output(out11, GPIO.HIGH)
                        GPIO.output(out12, GPIO.HIGH)
                        time.sleep(speedracer)
                        # time.sleep(1)
                    elif i == 6:
                        GPIO.output(out1, GPIO.LOW)
                        GPIO.output(out2, GPIO.LOW)
                        GPIO.output(out3, GPIO.LOW)
                        GPIO.output(out4, GPIO.HIGH)
                        GPIO.output(out5, GPIO.LOW)
                        GPIO.output(out6, GPIO.LOW)
                        GPIO.output(out7, GPIO.LOW)
                        GPIO.output(out8, GPIO.HIGH)
                        GPIO.output(out9, GPIO.LOW)
                        GPIO.output(out10, GPIO.LOW)
                        GPIO.output(out11, GPIO.LOW)
                        GPIO.output(out12, GPIO.HIGH)
                        time.sleep(speedracer)
                        # time.sleep(1)
                    elif i == 7:
                        GPIO.output(out1, GPIO.HIGH)
                        GPIO.output(out2, GPIO.LOW)
                        GPIO.output(out3, GPIO.LOW)
                        GPIO.output(out4, GPIO.HIGH)
                        GPIO.output(out5, GPIO.HIGH)
                        GPIO.output(out6, GPIO.LOW)
                        GPIO.output(out7, GPIO.LOW)
                        GPIO.output(out8, GPIO.HIGH)
                        GPIO.output(out9, GPIO.HIGH)
                        GPIO.output(out10, GPIO.LOW)
                        GPIO.output(out11, GPIO.LOW)
                        GPIO.output(out12, GPIO.HIGH)
                        time.sleep(speedracer)
                        # time.sleep(1)
                    if i == 7:
                        i = 0
                        continue
                    i = i + 1


            elif x < 0 and x >= -400:
                x = x * -1
                for y in range(x, 0, -1):
                    if positive == 1:
                        if i == 0:
                            i = 7
                        else:
                            i = i - 1
                        y = y + 3
                        positive = 0
                    negative = 1
                    # print((x+1)-y)
                    if i == 0:
                        GPIO.output(out1, GPIO.HIGH)
                        GPIO.output(out2, GPIO.LOW)
                        GPIO.output(out3, GPIO.LOW)
                        GPIO.output(out4, GPIO.LOW)
                        GPIO.output(out5, GPIO.HIGH)
                        GPIO.output(out6, GPIO.LOW)
                        GPIO.output(out7, GPIO.LOW)
                        GPIO.output(out8, GPIO.LOW)
                        GPIO.output(out9, GPIO.HIGH)
                        GPIO.output(out10, GPIO.LOW)
                        GPIO.output(out11, GPIO.LOW)
                        GPIO.output(out12, GPIO.LOW)
                        time.sleep(speedracer)
                        # time.sleep(1)
                    elif i == 1:
                        GPIO.output(out1, GPIO.HIGH)
                        GPIO.output(out2, GPIO.HIGH)
                        GPIO.output(out3, GPIO.LOW)
                        GPIO.output(out4, GPIO.LOW)
                        GPIO.output(out5, GPIO.HIGH)
                        GPIO.output(out6, GPIO.HIGH)
                        GPIO.output(out7, GPIO.LOW)
                        GPIO.output(out8, GPIO.LOW)
                        GPIO.output(out9, GPIO.HIGH)
                        GPIO.output(out10, GPIO.HIGH)
                        GPIO.output(out11, GPIO.LOW)
                        GPIO.output(out12, GPIO.LOW)
                        time.sleep(speedracer)
                        # time.sleep(1)
                    elif i == 2:
                        GPIO.output(out1, GPIO.LOW)
                        GPIO.output(out2, GPIO.HIGH)
                        GPIO.output(out3, GPIO.LOW)
                        GPIO.output(out4, GPIO.LOW)
                        GPIO.output(out5, GPIO.LOW)
                        GPIO.output(out6, GPIO.HIGH)
                        GPIO.output(out7, GPIO.LOW)
                        GPIO.output(out8, GPIO.LOW)
                        GPIO.output(out9, GPIO.LOW)
                        GPIO.output(out10, GPIO.HIGH)
                        GPIO.output(out11, GPIO.LOW)
                        GPIO.output(out12, GPIO.LOW)
                        time.sleep(speedracer)
                        # time.sleep(1)
                    elif i == 3:
                        GPIO.output(out1, GPIO.LOW)
                        GPIO.output(out2, GPIO.HIGH)
                        GPIO.output(out3, GPIO.HIGH)
                        GPIO.output(out4, GPIO.LOW)
                        GPIO.output(out5, GPIO.LOW)
                        GPIO.output(out6, GPIO.HIGH)
                        GPIO.output(out7, GPIO.HIGH)
                        GPIO.output(out8, GPIO.LOW)
                        GPIO.output(out9, GPIO.LOW)
                        GPIO.output(out10, GPIO.HIGH)
                        GPIO.output(out11, GPIO.HIGH)
                        GPIO.output(out12, GPIO.LOW)
                        time.sleep(speedracer)
                        # time.sleep(1)
                    elif i == 4:
                        GPIO.output(out1, GPIO.LOW)
                        GPIO.output(out2, GPIO.LOW)
                        GPIO.output(out3, GPIO.HIGH)
                        GPIO.output(out4, GPIO.LOW)
                        GPIO.output(out5, GPIO.LOW)
                        GPIO.output(out6, GPIO.LOW)
                        GPIO.output(out7, GPIO.HIGH)
                        GPIO.output(out8, GPIO.LOW)
                        GPIO.output(out9, GPIO.LOW)
                        GPIO.output(out10, GPIO.LOW)
                        GPIO.output(out11, GPIO.HIGH)
                        GPIO.output(out12, GPIO.LOW)
                        time.sleep(speedracer)
                        # time.sleep(1)
                    elif i == 5:
                        GPIO.output(out1, GPIO.LOW)
                        GPIO.output(out2, GPIO.LOW)
                        GPIO.output(out3, GPIO.HIGH)
                        GPIO.output(out4, GPIO.HIGH)
                        GPIO.output(out5, GPIO.LOW)
                        GPIO.output(out6, GPIO.LOW)
                        GPIO.output(out7, GPIO.HIGH)
                        GPIO.output(out8, GPIO.HIGH)
                        GPIO.output(out9, GPIO.LOW)
                        GPIO.output(out10, GPIO.LOW)
                        GPIO.output(out11, GPIO.HIGH)
                        GPIO.output(out12, GPIO.HIGH)
                        time.sleep(speedracer)
                        # time.sleep()
                    elif i == 6:
                        GPIO.output(out1, GPIO.LOW)
                        GPIO.output(out2, GPIO.LOW)
                        GPIO.output(out3, GPIO.LOW)
                        GPIO.output(out4, GPIO.HIGH)
                        GPIO.output(out5, GPIO.LOW)
                        GPIO.output(out6, GPIO.LOW)
                        GPIO.output(out7, GPIO.LOW)
                        GPIO.output(out8, GPIO.HIGH)
                        GPIO.output(out9, GPIO.LOW)
                        GPIO.output(out10, GPIO.LOW)
                        GPIO.output(out11, GPIO.LOW)
                        GPIO.output(out12, GPIO.HIGH)
                        time.sleep(speedracer)
                        # time.sleep(1)
                    elif i == 7:
                        GPIO.output(out1, GPIO.HIGH)
                        GPIO.output(out2, GPIO.LOW)
                        GPIO.output(out3, GPIO.LOW)
                        GPIO.output(out4, GPIO.HIGH)
                        GPIO.output(out5, GPIO.HIGH)
                        GPIO.output(out6, GPIO.LOW)
                        GPIO.output(out7, GPIO.LOW)
                        GPIO.output(out8, GPIO.HIGH)
                        GPIO.output(out9, GPIO.HIGH)
                        GPIO.output(out10, GPIO.LOW)
                        GPIO.output(out11, GPIO.LOW)
                        GPIO.output(out12, GPIO.HIGH)
                        time.sleep(speedracer)
                        # time.sleep(1)
                    if i == 0:
                        i = 7
                        continue
                    i = i - 1


    except KeyboardInterrupt:
        GPIO.cleanup()

def move_motor(out1,out2,out3,out4,speedracer,t, asd):

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(out1, GPIO.OUT)
    GPIO.setup(out2, GPIO.OUT)
    GPIO.setup(out3, GPIO.OUT)
    GPIO.setup(out4, GPIO.OUT)

    i = 0
    start = time.time()
    positive = 0
    negative = 0
    y = 0

    print("First calibrate by giving some +ve and -ve values.....")

    try:
        while (1) and (time.time()-start<t):
            GPIO.output(out1, GPIO.LOW)
            GPIO.output(out2, GPIO.LOW)
            GPIO.output(out3, GPIO.LOW)
            GPIO.output(out4, GPIO.LOW)
            x = 80*asd  # input()
            if x > 0 and x <= 400:
                for y in range(x, 0, -1):
                    if negative == 1:
                        if i == 7:
                            i = 0
                        else:
                            i = i + 1
                        y = y + 2
                        negative = 0
                    positive = 1
                    # print((x+1)-y)
                    if i == 0:
                        GPIO.output(out1, GPIO.HIGH)
                        GPIO.output(out2, GPIO.LOW)
                        GPIO.output(out3, GPIO.LOW)
                        GPIO.output(out4, GPIO.LOW)
                        time.sleep(speedracer)
                        # time.sleep(1)
                    elif i == 1:
                        GPIO.output(out1, GPIO.HIGH)
                        GPIO.output(out2, GPIO.HIGH)
                        GPIO.output(out3, GPIO.LOW)
                        GPIO.output(out4, GPIO.LOW)
                        time.sleep(speedracer)
                        # time.sleep(1)
                    elif i == 2:
                        GPIO.output(out1, GPIO.LOW)
                        GPIO.output(out2, GPIO.HIGH)
                        GPIO.output(out3, GPIO.LOW)
                        GPIO.output(out4, GPIO.LOW)
                        time.sleep(speedracer)
                        # time.sleep(1)
                    elif i == 3:
                        GPIO.output(out1, GPIO.LOW)
                        GPIO.output(out2, GPIO.HIGH)
                        GPIO.output(out3, GPIO.HIGH)
                        GPIO.output(out4, GPIO.LOW)
                        time.sleep(speedracer)
                        # time.sleep(1)
                    elif i == 4:
                        GPIO.output(out1, GPIO.LOW)
                        GPIO.output(out2, GPIO.LOW)
                        GPIO.output(out3, GPIO.HIGH)
                        GPIO.output(out4, GPIO.LOW)
                        time.sleep(speedracer)
                        # time.sleep(1)
                    elif i == 5:
                        GPIO.output(out1, GPIO.LOW)
                        GPIO.output(out2, GPIO.LOW)
                        GPIO.output(out3, GPIO.HIGH)
                        GPIO.output(out4, GPIO.HIGH)
                        time.sleep(speedracer)
                        # time.sleep(1)
                    elif i == 6:
                        GPIO.output(out1, GPIO.LOW)
                        GPIO.output(out2, GPIO.LOW)
                        GPIO.output(out3, GPIO.LOW)
                        GPIO.output(out4, GPIO.HIGH)
                        time.sleep(speedracer)
                        # time.sleep(1)
                    elif i == 7:
                        GPIO.output(out1, GPIO.HIGH)
                        GPIO.output(out2, GPIO.LOW)
                        GPIO.output(out3, GPIO.LOW)
                        GPIO.output(out4, GPIO.HIGH)
                        time.sleep(speedracer)
                        # time.sleep(1)
                    if i == 7:
                        i = 0
                        continue
                    i = i + 1


            elif x < 0 and x >= -400:
                x = x * -1
                for y in range(x, 0, -1):
                    if positive == 1:
                        if i == 0:
                            i = 7
                        else:
                            i = i - 1
                        y = y + 3
                        positive = 0
                    negative = 1
                    # print((x+1)-y)
                    if i == 0:
                        GPIO.output(out1, GPIO.HIGH)
                        GPIO.output(out2, GPIO.LOW)
                        GPIO.output(out3, GPIO.LOW)
                        GPIO.output(out4, GPIO.LOW)
                        time.sleep(speedracer)
                        # time.sleep(1)
                    elif i == 1:
                        GPIO.output(out1, GPIO.HIGH)
                        GPIO.output(out2, GPIO.HIGH)
                        GPIO.output(out3, GPIO.LOW)
                        GPIO.output(out4, GPIO.LOW)
                        time.sleep(speedracer)
                        # time.sleep(1)
                    elif i == 2:
                        GPIO.output(out1, GPIO.LOW)
                        GPIO.output(out2, GPIO.HIGH)
                        GPIO.output(out3, GPIO.LOW)
                        GPIO.output(out4, GPIO.LOW)
                        time.sleep(speedracer)
                        # time.sleep(1)
                    elif i == 3:
                        GPIO.output(out1, GPIO.LOW)
                        GPIO.output(out2, GPIO.HIGH)
                        GPIO.output(out3, GPIO.HIGH)
                        GPIO.output(out4, GPIO.LOW)
                        time.sleep(speedracer)
                        # time.sleep(1)
                    elif i == 4:
                        GPIO.output(out1, GPIO.LOW)
                        GPIO.output(out2, GPIO.LOW)
                        GPIO.output(out3, GPIO.HIGH)
                        GPIO.output(out4, GPIO.LOW)
                        time.sleep(speedracer)
                        # time.sleep(1)
                    elif i == 5:
                        GPIO.output(out1, GPIO.LOW)
                        GPIO.output(out2, GPIO.LOW)
                        GPIO.output(out3, GPIO.HIGH)
                        GPIO.output(out4, GPIO.HIGH)
                        time.sleep(speedracer)
                        # time.sleep()
                    elif i == 6:
                        GPIO.output(out1, GPIO.LOW)
                        GPIO.output(out2, GPIO.LOW)
                        GPIO.output(out3, GPIO.LOW)
                        GPIO.output(out4, GPIO.HIGH)
                        time.sleep(speedracer)
                        # time.sleep(1)
                    elif i == 7:
                        GPIO.output(out1, GPIO.HIGH)
                        GPIO.output(out2, GPIO.LOW)
                        GPIO.output(out3, GPIO.LOW)
                        GPIO.output(out4, GPIO.HIGH)
                        time.sleep(speedracer)
                        # time.sleep(1)
                    if i == 0:
                        i = 7
                        continue
                    i = i - 1


    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="run stepper", description='Runs motors to desired position')

    parser.add_argument('--x_motor',default=0, type=int)
    parser.add_argument('--x_motor_direction',default=0, type=int)
    parser.add_argument('--x_motor_duration',default=0, type=int)
    parser.add_argument('--y_motor', default=0, type=int)
    parser.add_argument('--y_motor_direction',default=0, type=int)
    parser.add_argument('--y_motor_duration',default=0, type=int)
    parser.add_argument('--E_motor', default=0,type=int)
    parser.add_argument('--E_motor_direction',default=0, type=int)
    parser.add_argument('--E_motor_duration',default=0, type=int)

    args = parser.parse_args()

    # Running the motors
    x = args.x_motor
    x_dir = args.x_motor_direction
    x_dur = args.x_motor_duration
    y = args.y_motor
    y_dir = args.y_motor_direction
    y_dur = args.y_motor_duration
    E = args.E_motor
    E_dir = args.E_motor_direction
    E_dur = args.E_motor_duration

    # directions are  specified in conditionals of lines 28-36
    # durations are specified in line 19 of xy_movement.py (currently 1s)
    # speeds are specified below

    speedracer_x = 0.2
    speedracer_y = 0.2
    speedracer_E = 0.6

    command = "python3 "


    count = 0
    if x:
        command = command + "run_x.py --dir=" + str(x_dir) + " --t=" + str(x_dur) + " --v=" + str(speedracer_x)

        count += 1

    if y:
        if count == 0:
            command = command + "run_y.py --dir=" + str(y_dir) + " --t=" + str(y_dur) + " --v=" + str(speedracer_y)

        else:
            command = command + " & python3 run_y.py --dir=" + str(y_dir) + " --t=" + str(y_dur) + " --v=" + str(speedracer_y)

        count += 1

    if E:
        if count == 0:
            command = command + "run_E.py --dir=" + str(E_dir) + " --t=" + str(E_dur) + " --v=" + str(speedracer_E)

        else:
            command = command + " & python3 run_E.py --dir=" + str(E_dir) + " --t=" + str(E_dur) + " --v=" + str(speedracer_E)

        count += 1

    os.run(command)