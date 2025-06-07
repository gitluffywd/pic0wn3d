```
         d8b                                                       888 
         Y8P                                                       888 
                                                                   888 
88888b.  888  .d8888b .d88b.  888  888  888 88888b.   .d88b.   .d88888 
888 "88b 888 d88P"   d88""88b 888  888  888 888 "88b d8P  Y8b d88" 888 
888  888 888 888     888  888 888  888  888 888  888 88888888 888  888 
888 d88P 888 Y88b.   Y88..88P Y88b 888 d88P 888  888 Y8b.     Y88b 888 
88888P"  888  "Y8888P "Y88P"   "Y8888888P"  888  888  "Y8888   "Y88888 
888                                                                    
888      You don't know the power of the DARKSIDE!!!!
888
```
# ☢️ pic0wn3d ☢️
Raspberry Pi Pico W CircuitPython Remote Control based on **[majdsassi's Pico WIFI Duck](https://github.com/majdsassi/Pico-WIFI-Duck)**.

# 💻 Requirements 💻
- Raspberry Pi Pico W or Pico 2 W (H isn't really needed but AGGRO mode wont work with it)
- CircuitPython (with adafruit_hid, adafruit_httpserver)
- _keyboard_layout_win_fi.py_ & _keycode_win_fi.py_ included in the lib directory
- USB cable (hi-speed/data transfer)
- Target
- PC/Phone for remote control via the AP...

# 💥 Features 💥
- Few ready made "scripts/payloads"
- This is setup for **Finnish language** (you need to figure out what your needs are yourself...)!
- Two modes: If jumper wire is on **GPIO15**, AGGRO mode is on (payload executed instantly) 
- LED behaviour based on status of connected clients
- 1337 h4x web layout so you can flex on noobs 💪
- Layout is also responsive CSS so usage with phone is easy 👨‍🍼

# ✍️ Installing & Usage ✍️
- Get the .uf2 and libraries (adafruit_hid, adafruit_httpserver): [CircuitPython](https://circuitpython.org/board/raspberry_pi_pico_w/)
- Initialize the Pico by plugging it while pressing BOOTSEL button
- Drag & drop the CircuitPython .uf2 on the drive
- Name it **pic0wn3d** (only needed for the premade scripts for file grabbing)
- Drag & drop files on the root of the drive..
- Use jumper wire for **GPIO15** to "AGGRO mode" (load payload instantly when plugged in)
- Connect Pico W on the PC
- Use phone (or whatever) to connect to the AP (192.168.4.1)
- Have fun........

---------------------

If you uncomment _boot.py_ (to hide the drive, you can't copy files to the device).

🚫 I am not responsible for anything anybody does with this code.

👌 If you have some nice payload scripts or any suggestions hit me up!

**[aurora.oops.wtf](https://aurora.oops.wtf)**
