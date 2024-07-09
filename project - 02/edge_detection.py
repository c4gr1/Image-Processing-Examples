import cv2
import numpy as np

# Görüntüyü yükle
image = cv2.imread('test_image_2.jpg', cv2.IMREAD_GRAYSCALE)  # Kenar tespiti için gri tonlama tercih edilir

# Gürültüyü azaltmak için Gaussian Blur uygula
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# Canny kenar dedektörünü uygula
edges = cv2.Canny(blurred_image, threshold1=30, threshold2=100)

# Sonuçları göster
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
