# PiZero2WCam
Repo for a Pi Zero 2 W cam using a Pi Cam v3 and a hardware button to take images.


# PRE-REQUISITES

For adding and expanding the code I recommend looking at the official Documentation of the PiCam2 libery 
```
https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf
```
# Installation

Save the File on your Raspberry Pi Zero 2 W, I recommend using the latest Pi OS Lite

Use an editor to edit the Camera file to add a path where it should save the Images.


# Dependencies

```
sudo apt install -y python3-picamera2
```

# Build

Connect the Pi Camera to the Raspberry Pi with the camera cable.
Connect a button to GPIO2 (Physical Pin 3).
