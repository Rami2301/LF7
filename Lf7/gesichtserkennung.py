import face_recognition
import os
import cv2
import numpy as np
import bluetooth

# Ordner für Gesichter
bekannte_gesichter = '/home/pi/LF7/data'

# Hier würde die Bluetooth Adresse vom Schloss eingetragen werden
target_address = "XX:XX:XX:XX:XX:XX" 

# Lade bekannte Gesichter
def lade_bekannte_gesichter():
    bekannte_gesichter = []

    # Bereite bekannte Gesichter vor
    for filename in os.listdir(bekannte_gesichter):
        if filename.endswith('.jpg') :
            image_path = os.path.join(bekannte_gesichter, filename)
            image = face_recognition.load_image_file(image_path)
            encoding = face_recognition.face_encodings(image)[0]  
            bekannte_gesichter.append(encoding)  

    return bekannte_gesichter

# Wenn Gesicht erkannt
def tuer_event(target_address):  

      
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

        sock.connect((target_address, 1))

        message = "OPEN_LOCK"  
        sock.send(message)

    finally:
        sock.close() 

# Gesichtserkennung
def erkenne_gesichter(bekannte_gesichter):
    video_capture = cv2.VideoCapture(0)

    while True:
        ret, frame = video_capture.read()
        rgb_frame = frame[:, :, ::-1]

        # Erkenne Gesichter im Bild
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        # Überprüfe jedes gefundene Gesicht
        for face_encoding in face_encodings:
            # Vergleiche das Gesicht mit den bekannten Gesichtern
            matches = face_recognition.compare_faces(bekannte_gesichter, face_encoding)

            if True in matches:
                tuer_event_event(target_address)  

    video_capture.release()
    cv2.destroyAllWindows()

# Hauptprogramm
if __name__ == "__main__":
    bekannte_gesichter = lade_bekannte_gesichter()
    erkenne_gesichter(bekannte_gesichter)
