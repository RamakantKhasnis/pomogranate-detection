import cv2
import numpy as np

# Load 
image_path = "/Users/ramakantk/Documents/pomegranate_counter/images (6).jpeg"
image = cv2.imread(image_path)
if image is None:
    print("Error loading image.")
    exit()

# Resize 
image = cv2.resize(image, (800, 600))

#  HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Broaden the red/orange/brown range
lower1 = np.array([0, 60, 30])
upper1 = np.array([20, 255, 255])
lower2 = np.array([160, 40, 30])
upper2 = np.array([180, 255, 255])

mask1 = cv2.inRange(hsv, lower1, upper1)
mask2 = cv2.inRange(hsv, lower2, upper2)
mask = cv2.bitwise_or(mask1, mask2)

# Morphological cleanup
kernel = np.ones((9, 9), np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

# Optional: improve contrast
mask = cv2.GaussianBlur(mask, (7, 7), 0)

#  contours
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

count = 0
for c in contours:
    area = cv2.contourArea(c)
    if area > 100:  # lower threshold for small fruits
        count += 1
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(image, str(count), (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (36, 255, 12), 2)

print(f"Detected fruits: {count}")

cv2.imshow("Detected Pomegranates", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("output_detected.jpg", image)