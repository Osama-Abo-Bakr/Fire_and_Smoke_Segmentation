# --------------- Fire_and_Smoke_Segmentation Detection -------------------

from ultralytics import YOLO
import cv2
import pandas as pd
import pygame

path_alarm = r"C:\Users\osama\OneDrive\Desktop\Moahmmed Upwork\mixkit-facility-alarm-sound-999.wav"
pygame.init()
pygame.mixer.music.load(path_alarm)

# video = cv2.VideoCapture(0)
video = cv2.VideoCapture(r'D:\Pycharm\Computer Vision Project\Fire and Smoke Segmentation\video1.mp4')
model = YOLO(r'D:\Pycharm\Computer Vision Project\Fire and Smoke Segmentation\Fire and Smoke Segmentation.pt')
class_list = {0: 'fire', 1: 'smoke'}

while True:
    _, image = video.read()
    if image is None:  # Break the loop if the video ends
        break

    image_copy = image.copy()
    h, w, c = image.shape

    image = cv2.flip(image, 1)
    result = model.predict(image)

    a = result[0].boxes.data
    px = pd.DataFrame(a).astype(float)

    fire_detected = False
    smoke_detected = False

    for index, row in px.iterrows():
        x1, y1, x2, y2 = int(row[0]), int(row[1]), int(row[2]), int(row[3])
        cls = class_list[int(row[5])]
        confidence = row[4]

        if cls == 'fire':
            fire_detected = True
        elif cls == 'smoke':
            smoke_detected = True

        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 0, 255), 2)
        cv2.rectangle(image, (x1, y1 - 25), (x1 + 200, y1), (0, 165, 255), -1)

        cv2.putText(image, f'id:{index}', (x1, y1 - 10), cv2.FONT_ITALIC, 0.7, (0, 0, 0), 1)
        cv2.putText(image, f'{cls}', (x1 + 55, y1 - 10), cv2.FONT_ITALIC, 0.7, (0, 0, 0), 1)
        cv2.putText(image, f'{round(confidence, 2)}', (x1 + 150, y1 - 10), cv2.FONT_ITALIC, 0.7, (0, 0, 0), 1)

    if fire_detected or smoke_detected:
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play()
    else:
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()

    cv2.imshow('image', image)
    if cv2.waitKey(1) == ord('o'):
        break

cv2.destroyAllWindows()
video.release()