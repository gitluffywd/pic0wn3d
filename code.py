import socketpool
import wifi
import board
import digitalio
import time
import storage
import usb_hid
from duck import exe
from adafruit_httpserver import Server, Request, JSONResponse, POST, Response

# AP INIT
SSID = "QUANTUM_REALM"
PASSWORD = "tailoredaccessoperations_69"


# GPIO INIT
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
jumper = digitalio.DigitalInOut(board.GP15)
jumper.switch_to_input(pull=digitalio.Pull.UP)

print("[*] Checking startup mode...")
time.sleep(1)

if not jumper.value:  
    mode = 2
    print("[!] AGGRO MODE: ON!")
else:
    mode = 1
    print("[*] Normal mode!")   

try:
    wifi.radio.start_ap(SSID, PASSWORD)
    print(f"[+] AP Started: {SSID}")
    ap_success = True
except Exception as e:
    print(f"[-] Failed to start AP: {e}")
    ap_success = False

if mode == 2:
    print("[*] Executing Payload from payload.dd...")
    try:
        with open("payload.dd", "r") as f:
            payload = f.readlines()
        exe(payload)
        print("[+] Payload execution completed!")
    except Exception as e:
        print(f"[ERROR] Failed to execute payload: {e}")

pool = socketpool.SocketPool(wifi.radio)
server = Server(pool, "/static", debug=True)
client_connected = False  
last_connect_time = time.monotonic()

@server.route("/")
def base(request: Request):
    global client_connected, last_connect_time
    last_connect_time = time.monotonic()
    client_connected = True
    with open("index.html", "r") as file:
        html_content = file.read()
    headers = {"Content-Type": "text/html"}
    return Response(request, html_content, headers=headers)

@server.route("/api", POST, append_slash=True)
def api(request: Request):
    global client_connected
    last_connect_time = time.monotonic()
    client_connected = True
    req = request.json()
    payload = req["content"]
    payload = payload.splitlines()
    try:
        exe(payload)
        return JSONResponse(request, {"message": "Done"})
    except Exception as e:
        return JSONResponse(request, {"error": str(e)}, status=500)

server.start("192.168.4.1", 80)
last_blink = time.monotonic()
led_state = False

while True:
    current_time = time.monotonic()

    if client_connected and current_time - last_connect_time > 60:
        client_connected = False

    if not ap_success:
        if current_time - last_blink >= 1:
            led_state = not led_state
            led.value = led_state
            last_blink = current_time

    elif client_connected:
        led.value = True
    else:
        if current_time - last_blink >= 0.2:
            led_state = not led_state
            led.value = led_state
            last_blink = current_time

    server.poll()
