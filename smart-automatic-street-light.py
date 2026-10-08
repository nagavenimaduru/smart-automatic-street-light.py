mport RPi.GPIO as GPIO
import time

# GPIO pin configuration
LDR_PIN = 17
RELAY_PIN = 27

# GPIO setup
GPIO.setmode(GPIO.BCM)

GPIO.setup(LDR_PIN, GPIO.IN)
GPIO.setup(RELAY_PIN, GPIO.OUT)

# Initially turn light OFF
GPIO.output(RELAY_PIN, GPIO.LOW)

print("===================================")
print(" SMART AUTOMATIC STREET LIGHT")
print("===================================")
print("System is running...")
print("Press Ctrl+C to stop.\n")

try:
    while True:

        # Read LDR sensor
        light = GPIO.input(LDR_PIN)

        if light == GPIO.LOW:
            # Darkness detected
            GPIO.output(RELAY_PIN, GPIO.HIGH)
            print("🌙 DARKNESS DETECTED - STREET LIGHT ON")

        else:
            # Light detected
            GPIO.output(RELAY_PIN, GPIO.LOW)
            print("☀️ DAYLIGHT DETECTED - STREET LIGHT OFF")

        time.sleep(1)

except KeyboardInterrupt:
    print("\nProgram stopped.")

finally:
    GPIO.output(RELAY_PIN, GPIO.LOW)
    GPIO.cleanup()
