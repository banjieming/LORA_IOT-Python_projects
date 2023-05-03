from time import sleep
from machine import Pin
import dht,gc
sensor=dht.DHT22(Pin(16))
#sensor=dht.DHT11(Pin(16))

def do_loop(lora):
    counter=0
    sensor.measure()
    Temp = sensor.temperature()
    Humidity = sensor.humidity()
    ID = 'C100E026'
    while True:
        data ='s,'+ID1+','+str(counter)+','+str(Temp)+','+str(Humidity)+',e'
        print(data.encode())
        sendmesg(lora, data.encode())
        counter += 1
        counter = counter % 256
        sleep(2)

def sendmesg(lora, data):
    #lora.println(data.decode())
    print("LoRa Sender")
    '''
    payload = 'Hello ({0})'.format(counter)
    print("Sending packet: \n{}\n".format(payload))
    lora.println(payload)
    lora.send(payload.encode())
    print('payload is sent')
    '''
    lora.send(data)
    print('data is sent')
    print(data.decode())