import mediapipe as mp
import cv2
import numpy as np
from mediapipe.framework.formats import landmark_pb2
import datetime
from math import sqrt
import win32api
import pyautogui
import os

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
click = 0

video = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
    while video.isOpened():
        _, frame = video.read()
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        image = cv2.flip(image, 1)

        imageHeight, imageWidth, _ = image.shape

        results = hands.process(image)

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                # Drawing the hands nodes and edges
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(250, 44, 250), thickness=2, circle_radius=2),
                                          )
                x = 10
            # print("khane kicche")
        if results.multi_hand_landmarks != None:
            for handLandmarks in results.multi_hand_landmarks:
                for point in mp_hands.HandLandmark:
                    normalizedLandmark = handLandmarks.landmark[point]
                    pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x,
                                                                                           normalizedLandmark.y,
                                                                                           imageWidth, imageHeight)
                    point = str(point)
                    # print(str(point))
                    # if point == '0' or point == '1' or point == '2' or point == '3' or point == '4' or point == '5' or point == '6' or point == '7' or point == '8' or point == '9' or point == '10' or point == '11' or point == '12' or point == '13' or point == '14' or point == '15' or point == '16' or point == '17' or point == '18' or point == '19' or point == '20' :
                    if point == '8':
                        try:
                            indexfingertip_x = pixelCoordinatesLandmark[0]
                            indexfingertip_y = pixelCoordinatesLandmark[1]
                            # x er khetre kom naile pura image side e jayga hocche na - mot kotha mouse er DPI baracchei
                            win32api.SetCursorPos(((indexfingertip_x * 6), (indexfingertip_y * 4)))
                            # Cursor er postion change hocche fingertip er theke dekhi dekhi
                            # print("Cursor position egulaa paisi")
                        except:
                            pass

                    elif point == '4':
                        try:
                            thumbfingertip_x = pixelCoordinatesLandmark[0]
                            thumbfingertip_y = pixelCoordinatesLandmark[1]

                        except:
                            pass

                    elif point == '20':
                        try:
                            pinkytip_x = pixelCoordinatesLandmark[0]
                            pinkytip_y = pixelCoordinatesLandmark[1]
                        except:
                            pass

                    try:
                        # print(f"Index x {indexfingertip_x}")
                        # print(f"Index y {indexfingertip_y}")
                        #
                        # print(f"thumb x {thumbfingertip_x}")
                        # print(f"thumb y {thumbfingertip_y}")

                        Index_thumb_Distance_x = abs(indexfingertip_x - thumbfingertip_x)
                        Index_thumb_Distance_y = abs(indexfingertip_y - thumbfingertip_y)

                        pinky_thumb_Distance_x = abs(pinkytip_x - thumbfingertip_x)
                        pinky_thumb_Distance_y = abs(pinkytip_y - thumbfingertip_y)
                        # print(f"Distance x {Distance_x}")
                        # print(f"Distance y {Distance_y}")
                        if Index_thumb_Distance_x <= 5 and Index_thumb_Distance_y <= 5:
                            x = x + 1
                            if(x % 13 == 0):
                                # z = datetime.now()
                                # print(z)
                                url = "https://www.facebook.com/mehrab.evan"
                                os.system(f"start {url}")

                        elif pinky_thumb_Distance_x <= 5 and pinky_thumb_Distance_y <= 5:
                            x = x + 1
                            if(x % 13 == 0):
                                # z = datetime.now()
                                # print(z)
                                url = "https://bd.linkedin.com/in/md-mehrab-evan-029a06197"
                                os.system(f"start {url}")

                        #     pyautogui.click()
                                # click = click + 1
                                # if click % 5 == 0:
                                #     print("single click")
                                #     pyautogui.click()

                        # MehrabStance =
                        # print(f"{indexfingertip_x}")
                        # pyautogui.moveTo(indexfingertip_x,indexfingertip_y)
                        # Distance_x = sqrt(
                        #     (indexfingertip_x - thumbfingertip_x) * 2 + (indexfingertip_x - thumbfingertip_x) * 2)
                        # Distance_y = sqrt(
                        #     (indexfingertip_y - thumbfingertip_y) * 2 + (indexfingertip_y - thumbfingertip_y) * 2)
                        # if Distance_x < 5 or Distance_x < -5:
                        # eikhane koyta click portese ta dekhtese
                        #     if Distance_y < 5 or Distance_y < -5:
                        #         click = click + 1
                        #         if click % 5 == 0:
                        #             print("single click")
                        #             pyautogui.click()

                    except:
                        pass

        cv2.imshow('MehrabCV', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

video.release()