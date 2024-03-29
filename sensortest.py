import time
import RPi.GPIO as GPIO

def calculate_distance(echo_pin,trigger_pin):
    # Use BCM GPIO references
    # instead of physical pin numbers
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    # Define GPIO to use on Pi
    GPIO_TRIGGER = trigger_pin
    GPIO_ECHO    = echo_pin



    # Set pins as output and input
    GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
    GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

    # Set trigger to False (Low)
    GPIO.output(GPIO_TRIGGER, False)

    #print("Ultrasonic Measurement")

    # Allow module to settle
    time.sleep(1)

    # Send 10us pulse to trigger
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.0001)
    GPIO.output(GPIO_TRIGGER, False)
    start = time.time()

    while GPIO.input(GPIO_ECHO)==0:
      start = time.time()

    while GPIO.input(GPIO_ECHO)==1:
      stop = time.time()

    # Calculate pulse length
    elapsed = stop-start

    # Distance pulse travelled in that time is time
    # multiplied by the speed of sound (cm/s)
    distancet = elapsed * 34300

    # That was the distance there and back so halve the value
    distance = distancet / 2

    #print("Distance :", distance)

    #print("Elaspsed time :", elapsed)

    #print("Total distance :", distancet)

    
    return distance

def calculate_distance_5_times(echo_pin,trigger_pin):
    sum = 0
    for i in range(0,5):
        add = calculate_distance(echo_pin,trigger_pin)
        sum += add
        print(add)
    return (sum/5)
