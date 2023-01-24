# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 22:10:16 2023

@author: saida
"""

# %%

"""
Problem: 
    Linki verilen videoda renkli toplar hareket etmektedir. 
    Senden bu videoyu input olarak alan ve videonun sol yarısındaki top sayısı 3’ü aştığında bizi uyaran bir script yazmanı istiyoruz. 
    Bu uyarı, terminale sol yarıdaki kırmızı top sayısının yazılması şeklinde olabilir.

"""

# Kütüphanelerin içe aktarılması görüntü işleme için OpenCv, matris işlemleri için numpy

import cv2
import numpy as np

video=cv2.VideoCapture("C:/Users/saida/OneDrive/Masaüstü/saidakca/video.mp4")

# HSV renk değer öğrenme
red_color = np.uint8([[[255, 0, 0]]])
hsv_red = cv2.cvtColor(red_color, cv2.COLOR_BGR2HSV)
print(hsv_red)

while True:
    ret, frame = video.read()
    if not ret:
        break

    # Hsv renk uzayına çevirme.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Yukarıda (while döngüsü üstünde) bulduğumuz renk değerini ve alt limit değerlerini giriyoruz
    min=np.array([0,50,50])
    red = np.array([120,255,255])

    # Sadece kırmızı renkleri yakalamak için threshold yapılır
    mask = cv2.inRange(hsv,min,red)

    # Soruda sol tarafı istediği için video 2 parçaya böleriz
    height, width = mask.shape[:2]
    left_screen = mask[0:height, 0:width//2]
    right_screen = mask[0:height, width//2:width]

    # Aynı anda 3 kırmızı top olunca uyarı vereceği için kırmızı top sayaç oluşturulur
    red_balls_left = cv2.countNonZero(left_screen)
    if red_balls_left > 3:
        print("Ekran 3 veya daha fazla kırmızı top bulunmaktadır !!!")

    cv2.imshow("Kirmizi Top Sayar", frame)
    cv2.waitKey(1)

video.release()
cv2.destroyAllWindows()


