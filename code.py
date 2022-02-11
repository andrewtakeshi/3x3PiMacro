import time
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
import board
import digitalio

btn1_pin = board.GP0
btn2_pin = board.GP1
btn3_pin = board.GP2
btn4_pin = board.GP3
btn5_pin = board.GP4
btn6_pin = board.GP5
btn7_pin = board.GP6
btn8_pin = board.GP7
btn9_pin = board.GP8

btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN

btn4 = digitalio.DigitalInOut(btn4_pin)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.DOWN

btn5 = digitalio.DigitalInOut(btn5_pin)
btn5.direction = digitalio.Direction.INPUT
btn5.pull = digitalio.Pull.DOWN

btn6 = digitalio.DigitalInOut(btn6_pin)
btn6.direction = digitalio.Direction.INPUT
btn6.pull = digitalio.Pull.DOWN

btn7 = digitalio.DigitalInOut(btn7_pin)
btn7.direction = digitalio.Direction.INPUT
btn7.pull = digitalio.Pull.DOWN

btn8 = digitalio.DigitalInOut(btn8_pin)
btn8.direction = digitalio.Direction.INPUT
btn8.pull = digitalio.Pull.DOWN

btn9 = digitalio.DigitalInOut(btn9_pin)
btn9.direction = digitalio.Direction.INPUT
btn9.pull = digitalio.Pull.DOWN

keyboard = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)


while True:
    # Discord deafen
    if btn1.value:
        keyboard.send(Keycode.CONTROL, Keycode.F1)
        time.sleep(0.25)
    # Audio toggle
    if btn2.value:
        keyboard.send(Keycode.CONTROL, Keycode.F2)
        time.sleep(0.25)
    # Volume down
    if btn3.value:
        cc.press(ConsumerControlCode.VOLUME_DECREMENT)
        while btn3.value:
            pass
        cc.release()
    # Adjust screen resolution
    if btn4.value:
        keyboard.send(Keycode.CONTROL, Keycode.F4)
        time.sleep(0.25)
    # Pin window to top (powertoys)
    if btn5.value:
        keyboard.send(Keycode.CONTROL, Keycode.F5)
        time.sleep(0.25)
    # Volume up
    if btn6.value:
        cc.press(ConsumerControlCode.VOLUME_INCREMENT)
        while btn6.value:
            pass
        cc.release()
    # Previous track
    if btn7.value:
        cc.send(ConsumerControlCode.SCAN_PREVIOUS_TRACK)
        time.sleep(0.25)
    # Play/pause
    if btn8.value:
        cc.send(ConsumerControlCode.PLAY_PAUSE)
        time.sleep(0.25)
    # Next track
    if btn9.value:
        cc.send(ConsumerControlCode.SCAN_NEXT_TRACK)
        time.sleep(0.25)
    time.sleep(0.1)
