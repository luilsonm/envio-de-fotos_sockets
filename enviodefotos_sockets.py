codigo enviar foto socket funcionando 

import camera
from time import sleep
import machine
import ubinascii
from machine import Pin
import network
import config
import socket
import _thread


wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(config.WIFI_SSID, config.WIFI_PASSWORD)

while not wifi.isconnected():
    pass

print("wifi connected")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.103.24',12341))
#s.send(b'')

def one():
    while True:
        
        #print("funtion: ONE")
        sleep(2)

_thread.start_new:thread(one,())


while True:
    data = s.recv(1024)
    print(data)
    if data == b'Hola':            
        nombre = "Cap" + ".jpg"
        print(nombre)
        try:
            camera.init(0, format=camera.JPEG, fb_location=camera.PSRAM)

            # Establecer configuraciones de la cámara
            camera.brightness(-1)
            camera.flip(0)
            camera.mirror(0)
            camera.framesize(camera.FRAME_XGA)
            camera.contrast(2)
            camera.saturation(-2)
            camera.quality(10)
            camera.speffect(camera.EFFECT_NONE)
            camera.whitebalance(camera.WB_NONE)

            # Capturar la imagen
            img = camera.capture()
            print("Tamaño de la imagen:", len(img))

            # Desactivar la cámara
            camera.deinit()

            # Codificar la imagen en Base64 y mostrarla en consola
            encoded_img= ubinascii.b2a_base64(img)
            #print(encoded_img)
            
                
            s.sendall(encoded_img)
            nombre = "Cap" + ".jpg"
            print(nombre)

#            sleep(10)

        except Exception as err:
            print("Error:", str(err))
            # Desactivar la cámara
            camera.deinit()

            sleep(2)