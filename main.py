# two bed with shared bathroom main.py

from mqtt_as import MQTTClient
from mqtt_local import wifi_led, blue_led, config
import uasyncio as asyncio
from machine import Pin, PWM
import utime
import network
from ota import OTAUpdater
from secrets import wifi_ssid, wifi_pw

room_num = '03'
bathroom1 = '01'
bathroom2 = '03'

# this is a comment
#  this has fix for touchpad call lights and network ip address.

TOPIC = f'Room {room_num}'
outages = 0
LED1 = PWM(Pin(0))
LED2 = PWM(Pin(15))
buzzer = PWM(Pin(22)) #New PCB rev. 3 uses Pin(28)

bed1_btn = Pin(1,Pin.IN,Pin.PULL_DOWN)
bed1_prev_state = bed1_btn.value()
bed2_btn = Pin(14,Pin.IN,Pin.PULL_DOWN)
bed2_prev_state = bed2_btn.value()
bed3_btn = Pin(27,Pin.IN,Pin.PULL_DOWN)
bed3_prev_state = bed3_btn.value()
bed4_btn = Pin(17,Pin.IN,Pin.PULL_DOWN)
bed4_prev_state = bed4_btn.value()
bth_btn = Pin(21,Pin.IN,Pin.PULL_DOWN)
bth_prev_state = bth_btn.value()
off_btn = Pin(4,Pin.IN,Pin.PULL_DOWN)
off_prev_state = off_btn.value()

# network
wlan = network.WLAN(network.STA_IF)
wlan_ip = wlan.ifconfig()
#  Button Handlers
async def bed1_handler():
    while True:
        await asyncio.sleep_ms(10)
        global bed1_prev_state
        if (bed1_btn.value() == True) and (bed1_prev_state == False):
            utime.sleep_ms(250)
            if (bed1_btn.value() == True) and (bed1_prev_state == False):
                bed1_prev_state = True
                LED1.freq(800)
                LED1.duty_u16(30000)
                buzzer.freq(300)
                buzzer.duty_u16(64000)
                print("Bed 1 has been pressed")
                
        elif (bed1_btn.value() == False) and (bed1_prev_state == True):
            bed1_prev_state = False
            await asyncio.sleep_ms(10)
            
        
async def bed1_pb_handler():
    while True:
        await asyncio.sleep_ms(10)
        global bed1_prev_state
        if bed1_prev_state == 1:
            print("It's a no go!1")
            await client.publish(f'{room_num}-1', f'Room {room_num}-1 has been pressed', qos = 1)

        
async def bed2_handler():
    while True:
        await asyncio.sleep_ms(10)
        global bed2_prev_state
        if (bed2_btn.value() == True) and (bed2_prev_state == False):
            utime.sleep_ms(250)
            if (bed2_btn.value() == True) and (bed2_prev_state == False):
                bed2_prev_state = True
                LED1.freq(800)
                LED1.duty_u16(30000)
                buzzer.freq(200)
                buzzer.duty_u16(60000)
                print("Bed 2 has been pressed")
                
        elif (bed2_btn.value() == False) and (bed2_prev_state == True):
            bed2_prev_state = False
            await asyncio.sleep_ms(10)
            
        
async def bed2_pb_handler():
    while True:
        await asyncio.sleep_ms(10)
        global bed2_prev_state
        if bed2_prev_state == 1:
            print("It's a go go!1")
            await client.publish(f'{room_num}-1', f'Room {room_num}-2 has been pressed', qos = 1)
            
async def bed3_handler():
    while True:
        await asyncio.sleep_ms(10)
        global bed3_prev_state
        if (bed3_btn.value() == True) and (bed3_prev_state == False):
            utime.sleep_ms(250)
            if (bed3_btn.value() == True) and (bed3_prev_state == False):
                bed3_prev_state = True
                LED1.freq(800)
                LED1.duty_u16(30000)
                buzzer.freq(300)
                buzzer.duty_u16(60000)
                print("Bed 2 has been pressed")
                
        elif (bed3_btn.value() == False) and (bed3_prev_state == True):
            bed3_prev_state = False
            await asyncio.sleep_ms(10)
             
         
async def bed3_pb_handler():
    while True:
        await asyncio.sleep_ms(10)
        global bed3_prev_state
        if bed3_prev_state == 1:
            print("It's a go go!1")
            await client.publish(f'{room_num}-1', f'Room {room_num}-3 has been pressed', qos = 1)
            
async def bed4_handler():
    while True:
        await asyncio.sleep_ms(10)
        global bed4_prev_state
        if (bed4_btn.value() == True) and (bed4_prev_state == False):
            utime.sleep_ms(250)
            if (bed4_btn.value() == True) and (bed4_prev_state == False):
                bed4_prev_state = True
                LED1.freq(800)
                LED1.duty_u16(30000)
                buzzer.freq(300)
                buzzer.duty_u16(60000)
                print("Bed 2 has been pressed")
                
        elif (bed4_btn.value() == False) and (bed4_prev_state == True):
            bed4_prev_state = False
            await asyncio.sleep_ms(10)
            
        
async def bed4_pb_handler():
    while True:
        await asyncio.sleep_ms(10)
        global bed4_prev_state
        if bed4_prev_state == 1:
            print("It's a go go!1")
            await client.publish(f'{room_num}-1', f'Room {room_num}-4 has been pressed', qos = 1)
    
async def bth_handler():
    while True:
        await asyncio.sleep_ms(10)
        global bth_prev_state
        if (bth_btn.value() == True) and (bth_prev_state == False):
            utime.sleep_ms(250)
            if (bth_btn.value() == True) and (bth_prev_state == False):
                bth_prev_state = True
                LED1.freq(800)
                LED1.duty_u16(30000)
                buzzer.freq(300)
                buzzer.duty_u16(60000)
                print(f'Bathroom {bathroom1} & {bathroom2} has been pressed')
                
        elif (bth_btn.value() == False) and (bth_prev_state == True):
            bth_prev_state = False
            await asyncio.sleep_ms(10)
            
        
async def bth_pb_handler():
    while True:
        await asyncio.sleep_ms(10)
        global bth_prev_state
        if bth_prev_state == 1:
            print("It's a go go!1")
            await client.publish(f'Bathroom {bathroom1}', f'Bathroom {bathroom1} & {bathroom2} has been pressed', qos = 1)

async def off_handler():
    while True:
        await asyncio.sleep_ms(10)
        global off_prev_state
        global bed1_prev_state
        if (off_btn.value() == True) and (off_prev_state == False):
            utime.sleep_ms(250)
            if (off_btn.value() == True) and (off_prev_state == False):
                off_prev_state = True
                LED1.duty_u16(0)
                LED2.duty_u16(0)
                buzzer.duty_u16(0)
                await asyncio.sleep_ms(10)
                if bed1_prev_state == True: #this checks if bed1 is still pressed. If it is, the light and sound turn back on.
                    LED1.freq(800)
                    LED1.duty_u16(30000)
                    buzzer.freq(300)
                    buzzer.duty_u16(60000)
                    await asyncio.sleep_ms(10)
                if bed2_prev_state == True:
                    LED1.freq(800)
                    LED1.duty_u16(30000)
                    buzzer.freq(300)
                    buzzer.duty_u16(60000)
                    await asyncio.sleep_ms(10)
                if bth_prev_state == True:
                    LED2.freq(800)
                    LED2.duty_u16(30000)
                    buzzer.freq(300)
                    buzzer.duty_u16(60000)
                    await asyncio.sleep_ms(10)
                    
                
        elif (off_btn.value() == False) and (off_prev_state == True):
            off_prev_state = False
            await asyncio.sleep_ms(10)

async def off_pb_handler():
    while True:
        await asyncio.sleep_ms(10)
        global off_prev_state
        if off_prev_state == 1:
            print("It's a go go!")
            await client.publish(f'{room_num}-Off', f'Room {room_num} has been answered', qos = 1)
            await asyncio.sleep_ms(250)


async def messages(client):
    async for topic, msg, retained in client.queue:
        print(f'Topic: "{topic.decode()}" Message: "{msg.decode()}" Retained: {retained}')
        msg = msg.decode('utf-8')
        print(msg)
        if msg == f'Room {room_num}-1 has been pressed':
            LED1.freq(800)
            LED1.duty_u16(30000)
            buzzer.freq(300)
            buzzer.duty_u16(60000)
        if msg == f'Room {room_num}-2 has been pressed':
            LED1.freq(800)
            LED1.duty_u16(30000)
            buzzer.freq(300)
            buzzer.duty_u16(60000)
        if msg == f'Room {room_num}-3 has been pressed':
            LED1.freq(800)
            LED1.duty_u16(30000)
            buzzer.freq(300)
            buzzer.duty_u16(60000)
        if msg == f'Room {room_num}-4 has been pressed':
            LED1.freq(800)
            LED1.duty_u16(30000)
            buzzer.freq(300)
            buzzer.duty_u16(60000)
        if msg == f'Bathroom {bathroom1} & {bathroom2} has been pressed':
            LED2.freq(800)
            LED2.duty_u16(30000)
            buzzer.freq(300)
            buzzer.duty_u16(60000)
        if msg == f'Room {room_num} reset':
            machine.reset()
        elif msg == f'Room {room_num} has been answered':
            LED1.duty_u16(0)
            LED2.duty_u16(0)
            buzzer.duty_u16(0)
            buzzer.duty_u16(0)
            await asyncio.sleep_ms(10)
            
async def down(client):
    global outages
    while True:
        await client.down.wait()  # Pause until connectivity changes
        client.down.clear()
        wifi_led(False)
        outages += 1
        print('WiFi or broker is down.')

async def up(client):
    while True:
        await client.up.wait()
        client.up.clear()
        wifi_led(True)
        print('We are connected to broker.')
        print(wlan.ifconfig())
        await client.subscribe(f'Room {room_num}', 1)
        
async def room_status():
    while True:
        await asyncio.sleep_ms(20)
        await client.publish(f"Room {room_num}", f"Room {room_num} connected!", qos = 1)
        await client.publish(f'Room {room_num}', str(wlan.ifconfig()), qos = 1)
        await asyncio.sleep(480)
        
async def check_for_updates():
    while True:
        await asyncio.sleep(20)
        firmware_url = "https://raw.githubusercontent.com/axeldelaguardia/ota_test/main/"
        ota_updated = OTAUpdater(wifi_ssid, wifi_pw, firmware_url, "main.py")
        ota_updated.download_and_install_update_if_available()
        
        
async def main(client):
    asyncio.create_task(bed1_handler())
    asyncio.create_task(bed1_pb_handler())

    
    asyncio.create_task(bed2_handler())
    asyncio.create_task(bed2_pb_handler())
  
    asyncio.create_task(bed3_handler())
    asyncio.create_task(bed3_pb_handler())
    
    asyncio.create_task(bed4_handler())
    asyncio.create_task(bed4_pb_handler())
       
    asyncio.create_task(bth_handler())
    asyncio.create_task(bth_pb_handler())

    
    asyncio.create_task(off_handler())
    asyncio.create_task(off_pb_handler())
  
    asyncio.create_task(room_status())
    
    asyncio.create_task(check_for_updates())


    try:
        await client.connect()
    except OSError:
        print('Connection failed.')
    
    for task in (up, down, messages):
        asyncio.create_task(task(client))
        
    n = 0
    
    while True:


        await asyncio.sleep_ms(10)


#  Define configuration
config['will'] = (TOPIC, f'Room {room_num} connected!', False, 0)
config['keepalive'] = 120
config["queue_len"] = 1  # Use event interface with default queue

#  Set up client. Enable optional debug statements.
MQTTClient.DEBUG = True
client = MQTTClient(config)

try:
    asyncio.run(main(client))
finally: # Prevent LmacRxBlk:1 errors.
  client.close()
  blue_led(True)
  asyncio.new_event_loop()