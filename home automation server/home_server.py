import requests
import json
import time

while (True):
    time.sleep(1)
    print("Asking F2 for values")
    value = requests.get("http://127.0.0.1:5000/get_values", timeout=5)
    value = json.loads(value.content)
    if value['led'] == 'on':
        print("TELLING NODE MCU TO SWITCH ON LED")
    if value['led'] == 'off':
        print("TELLING NODE MCU TO SWITCH OFF LED")
    if value['door'] == 'open':
        print("tell to open door")
    if value['door'] == 'close':
        print("telling to close door")
    # if value['ldr'] == 'on':
    #   print('telling mcu to on ldr')
    # if value['ldr'] == 'off':
    #   print('telling to off ldr')
    if value['dht'] == 'on':
        print('telling mcu to on dht')
    if value['dht'] == 'off':
        print('telling node mcu to off dht')
    if value['buzzer'] == 'on':
        print('telling node mcu to on buzzer')
    if value['buzzer'] == 'off':
        print('telling node mcu to off buzzer')
    if value['gas_detector'] == 'on':
        print('telling node mcu to on gas detector')
    if value['gas_detector'] == 'off':
        print('telling node mcu to off gas detector')