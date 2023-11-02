import network
import time
from machine import Timer
from umqtt.simple import MQTTClient

temporiza = Timer(0)                    
prev_weather = 0


MQTT_CLIENT_ID = ""

MQTT_BROKER    = "" # El broker
MQTT_USER      = ""
MQTT_PASSWORD  = ""
topic_pub     = "nicolas/moneditas" # Eltopic donde vas a publicar
topic_sub      = 'nicolas/moneditas' # El topic al que te vas a suscribir



def conectar(red, contra):
    global mired
    
    mired = network.WLAN(network.STA_IF)
    
    if not mired.isconnected():
        mired.active(True)
        mired.connect(red, contra)
        print(f'Conectando a la red {red} ...')
        timeout = time.time()
        
        while not mired.isconnected():
            if (time.ticks_diff (time.time(), timeout) > 10):
                return False
            
    return True

if conectar(' ', ' '):
    print('Conexion exitosa!')
    print(f'Datos de la red  (ip/netmask/gw/dns): {mired.ifconfig()}') 
 

    def sub_cb(topic, msg):
        print(f"llego el topic: {topic} con el valor {msg}")


    print("Connecting to MQTT server... ", end="")
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, user=MQTT_USER, password=MQTT_PASSWORD)

    client.set_callback(sub_cb)

    client.connect()

    client.subscribe(topic_sub)

    print(f'Connected to {MQTT_BROKER} MQTT broker, subscribed to {topic_sub} topic')
    print("Connected!")
    prev_weather = ""


    def desborde (Timer):   
        global prev_weather
        numMon = "8"  
    
        message = numMon
        if message != prev_weather:
            print(f"valor publicado en el topic {topic_pub}: {message}")
            client.publish("nicolas/moneditas", message)
            prev_weather = message


    temporiza.init(period=1000,mode=Timer.PERIODIC,callback=desborde)

    while True:
        print ("esperando") 
        client.wait_msg() 
    