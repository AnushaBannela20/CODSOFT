import cv2

# -------- Step 1: Load Haar Cascade face detector --------
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# -------- Step 2: Load known face image --------
# Convert to grayscale for Haar Cascade
known_img = cv2.imread("sharukhkhan.jpg")
known_gray = cv2.cvtColor(known_img, cv2.COLOR_BGR2GRAY)
known_faces = face_cascade.detectMultiScale(known_gray, 1.3, 5)

# Take first detected face region as "known"
(x, y, w, h) = known_faces[0]
known_face_crop = known_gray[y:y+h, x:x+w]

# -------- Step 3: Load test image --------
test_img = cv2.imread("test.jpg")
test_gray = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)

# Detect faces in test image
faces = face_cascade.detectMultiScale(test_gray, 1.3, 5)

for (x, y, w, h) in faces:
    test_face_crop = test_gray[y:y+h, x:x+w]

    # -------- Step 4: Fake recognition using histogram comparison --------
    known_hist = cv2.calcHist([known_face_crop], [0], None, [256], [0, 256])
    test_hist = cv2.calcHist([test_face_crop], [0], None, [256], [0, 256])

    score = cv2.compareHist(known_hist, test_hist, cv2.HISTCMP_CORREL)

    label = "Unknown"
    if score > 0.9:  # Threshold for similarity
        label = "Known Person"

    # Draw box & label
    cv2.rectangle(test_img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.putText(test_img, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# -------- Step 5: Show result --------
cv2.imshow("Face Detection & Recognition", test_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
