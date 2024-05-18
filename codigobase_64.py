import camera
from time import sleep
import machine
import ubinascii

while True:
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
        print(encoded_img)
        
        sleep(10)

    except Exception as err:
        print("Error:", str(err))
        sleep(2)