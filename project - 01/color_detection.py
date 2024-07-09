import cv2
import numpy as np

# Görüntüyü yükle
image = cv2.imread('test_image.jpg')  # 'images/test_image.jpg' konumundaki dosyayı açar

# RGB'den HSV'ye dönüştür
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Mavi renk aralığı tanımla
lower_blue = np.array([100, 150, 50])
upper_blue = np.array([140, 255, 255])

# Belirlenen renk aralığında maske oluştur
mask = cv2.inRange(hsv_image, lower_blue, upper_blue)

# Maskeyi orijinal görüntü ile birleştir
result = cv2.bitwise_and(image, image, mask=mask)

# Sonuçları göster
cv2.imshow('Original Image', image)
cv2.imshow('Mask', mask)
cv2.imshow('Detected Blue Color', result)

cv2.waitKey(0)
cv2.destroyAllWindows()
