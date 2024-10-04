import RPi.GPIO as GPIO
import time
import os
from datetime import datetime

# Pin nummer
BUTTON_PIN_1 = 18 

# Speicherordner für Bilder
OUTPUT_FOLDER = '/home/pi/LF7/data' 

# Funktion um Bilder zu erstellen
def bilder_erstellen():
    
   for i in range(15):
        # Aktuelles Datum und Uhrzeit für den Dateinamen
        timestamp = datetime.now().strftime('%Y-%m-%d%H-%M-%S')
        image_path = os.path.join(OUTPUT_FOLDER, f'image{timestamp}_{i+1}.jpg')

        #Befehl ausführen  Bild aufnehmen
        fswebcam_command = f'fswebcam -r 1280x720 --no-banner {image_path}'
        subprocess.run(fswebcam_command, shell=True) 

        print(f"Bild {i+1} gespeichert: {image_path}")
        time.sleep(10)  # 10 Sekunden warten

# Setup für Button Events
def setup_buttons():
    GPIO.setmode(GPIO.BCM)  
    GPIO.setup(BUTTON_PIN_1, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
    

    GPIO.add_event_detect(BUTTON_PIN_1, GPIO.FALLING, callback=lambda x: button_pressed(BUTTON_PIN_1), bouncetime=300)

# Funktion die beim Drücken eines Buttons ausgelöst wird
def button_pressed(channel):
    if channel == BUTTON_PIN_1:
        bilder_erstellen() 

if __name__ == "__main__":
    try:
        setup_buttons()  
        print("Warte auf Button-Events...")
        
        while True:
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("Beende Programm...")
    finally:
        GPIO.cleanup()  # GPIO-Pins zurücksetzen