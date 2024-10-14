from gpiozero import Button, LED
from signal import pause
from picamera2 import Picamera2
from libcamera import controls
import time
from datetime import datetime

# Initialize Picamera2
picam2 = Picamera2()

# Configure camera for the highest quality settings
camera_config = picam2.create_still_configuration(main={"size": picam2.sensor_resolution})
picam2.configure(camera_config)

# Initialize the buttons and LED
button_take_picture = Button(2)  # BCM GPIO2 (Physical Pin 3)

def set_focus(position):
    print(f"Setting focus to lens position {position}")
    picam2.set_controls({"AfMode": controls.AfModeEnum.Manual, "LensPosition": 0.0})
    led.on()
    time.sleep(0.5)
    led.off()

def start_focus():
    print("Button pressed! Preparing to take picture...")

def take_picture():
    print("Button released! Taking picture...")
    picam2.start()  # Start the camera

    # Get the current date and time
    now = datetime.now()
    filename = now.strftime("%H-%M-%S_%d-%m-%Y.jpg")

    # Capture the image
    picam2.capture_file(f"/home/ausman/{filename}")
    print(f"Picture taken and saved as /home/ausman/{filename}")
    
    picam2.stop()  # Stop the camera

# Assign button actions
button_take_picture.when_pressed = start_focus
button_take_picture.when_released = take_picture

pause()
