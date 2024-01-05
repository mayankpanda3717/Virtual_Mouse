import mediapipe as mp
import cv2
import numpy as np
from mediapipe.framework.formats import landmark_pb2
import time
from math import sqrt
import win32api
import pyautogui
 
 
 
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
click=0
 
video = cv2.VideoCapture(0)
 
with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands: 
    while video.isOpened():
        _, frame = video.read()
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
         
        image = cv2.flip(image, 1)
 
        imageHeight, imageWidth, _ = image.shape
 
        results = hands.process(image)
   
 
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
  
        if results.multi_hand_landmarks:
            for num, hand in enumerate(results.multi_hand_landmarks):
                mp_drawing.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS, 
                                        mp_drawing.DrawingSpec(color=(255, 36, 0), thickness=4, circle_radius=2))
 
        if results.multi_hand_landmarks != None:
          for handLandmarks in results.multi_hand_landmarks:
            for point in mp_hands.HandLandmark:
 
    
                normalizedLandmark = handLandmarks.landmark[point]
                pixelCoordinatesLandmark = mp_drawing._normalized_to_pixel_coordinates(normalizedLandmark.x, normalizedLandmark.y, imageWidth, imageHeight)
    
                point=str(point)
                
                
 
 
                if point=='HandLandmark.INDEX_FINGER_TIP':
                 try:
                    indexfingertip_x=pixelCoordinatesLandmark[0]
                    indexfingertip_y=pixelCoordinatesLandmark[1]
                    
                   
 
                 except:
                    pass
                
                elif point=='HandLandmark.MIDDLE_FINGER_TIP':
                 try:
                    middlefingertip_x=pixelCoordinatesLandmark[0]
                    middlefingertip_y=pixelCoordinatesLandmark[1]
                   
                   
 
                 except:
                    pass
 
                elif point=='HandLandmark.PINKY_TIP':
                 try:
                    pinkytip_x=pixelCoordinatesLandmark[0]
                    pinkytip_y=pixelCoordinatesLandmark[1]
                    win32api.SetCursorPos((pinkytip_x*4,pinkytip_y*5))
                   
                   
 
                 except:
                    pass
                
                
                try:
                    
                    Distance_x= int(sqrt((middlefingertip_x-indexfingertip_x)**2 + (middlefingertip_x-indexfingertip_x)**2))
                    Distance_y= int(sqrt((middlefingertip_y-indexfingertip_y)**2 + (middlefingertip_y-indexfingertip_y)**2))
                    if Distance_x<4 or Distance_x<-6:
                        if Distance_y<4 or Distance_y<-4:
                            click=click+1
                            if click%5==0:
                                print("single click")
                                pyautogui.click()                            
 
                except:
                    pass
 
        cv2.imshow('Hand Tracking', image)
 
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
 
video.release()