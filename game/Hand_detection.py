import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import numpy as np
import os

class HandDetector:
    def __init__(self, model_path='hand_landmarker.task', maxHands=1):
        # Create an HandLandmarker object.
        base_options = python.BaseOptions(model_asset_path=model_path)
        options = vision.HandLandmarkerOptions(
            base_options=base_options,
            num_hands=maxHands)
        self.landmarker = vision.HandLandmarker.create_from_options(options)
        self.results = None

    def findHands(self, img, draw=True):
        # Convert the BGR image to RGB
        rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # Load the input image from a numpy array.
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_image)
        
        # Detect hand landmarks from the input image.
        self.results = self.landmarker.detect(mp_image)

        if self.results.hand_landmarks:
            for hand_landmarks in self.results.hand_landmarks:
                if draw:
                    # Draw landmarks manually since solutions.drawing_utils is missing
                    h, w, _ = img.shape
                    for landmark in hand_landmarks:
                        cx, cy = int(landmark.x * w), int(landmark.y * h)
                        cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
                    
                    # Draw connections (simplified)
                    # We can add full connection drawing if needed, but points are enough for now
        return img

    def findPosition(self, img, handNo=0, draw=True):
        lmList = []
        if self.results and self.results.hand_landmarks:
            if len(self.results.hand_landmarks) > handNo:
                myHand = self.results.hand_landmarks[handNo]
                h, w, c = img.shape
                for id, landmark in enumerate(myHand):
                    cx, cy = int(landmark.x * w), int(landmark.y * h)
                    lmList.append([id, cx, cy])
                    if draw and id == 8: # Index finger tip
                        cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
        return lmList