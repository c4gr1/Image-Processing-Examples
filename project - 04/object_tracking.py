import cv2

# Videoyu yükle veya kamera kullan
cap = cv2.VideoCapture(0)  # 0, varsayılan kamerayı kullanır

# Tracker'ı seç ve başlat
tracker = cv2.TrackerKCF_create()  # KCF (Kernelized Correlation Filters) algoritmasını kullanarak bir tracker oluşturur
ret, frame = cap.read()  # Kameradan ilk kareyi alır
roi = cv2.selectROI("Frame", frame, fromCenter=False, showCrosshair=True)  # Kullanıcıdan ROI'yi seçmesini ister
tracker.init(frame, roi)  # Seçilen ROI'yi kullanarak tracker'ı başlatır

while True:
    ret, frame = cap.read()  # Bir sonraki kareyi kameradan alır
    if not ret:  # Eğer kare alınamazsa döngüyü kırar
        break

    # Tracker'ı güncelle
    success, box = tracker.update(frame)  # Tracker'ı günceller ve yeni nesnenin konumunu döndürür
    if success:  # Tracker başarıyla güncellendiyse
        (x, y, w, h) = [int(v) for v in box]  # Dikdörtgenin koordinatlarını ve boyutlarını alır
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)  # Takip edilen nesnenin etrafına bir dikdörtgen çizer

    cv2.imshow("Tracking", frame)  # Takip edilen görüntüyü gösterir
    if cv2.waitKey(1) & 0xFF == ord('q'):  # 'q' tuşuna basıldığında döngüyü kırar
        break

cap.release()  # Kamerayı serbest bırakır
cv2.destroyAllWindows()  # Tüm pencereleri kapatır
