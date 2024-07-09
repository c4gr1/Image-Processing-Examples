import cv2

# Yüz tanıma modelini yükle
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Görüntüyü yükle
image = cv2.imread('test_image_3.jpg')

# Görüntüyü griye çevir
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Yüzleri tespit et
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=10)

# Tespit edilen yüzlerin etrafına dikdörtgen çiz
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Sonuçları göster
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
