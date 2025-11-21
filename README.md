# 🍎 Automated Pomegranate Fruit Counting System

This project is an **Automated Pomegranate Fruit Counting System** developed using **Python** and **OpenCV**. It accurately detects and counts pomegranates in images using classical computer vision methods, making it highly useful for **agricultural analytics, yield estimation, and farm automation**.

---

## 📌 How It Works

### 1️⃣ Image Loading & Preprocessing  
The system loads the input image and converts it from **BGR to HSV**, as HSV is more reliable for color-based segmentation.

### 2️⃣ Color Segmentation  
Two HSV color ranges (red/orange/brown tones) are applied to isolate pomegranate regions.  
This improves detection accuracy under different lighting conditions.

### 3️⃣ Mask Refinement  
A binary mask is generated and cleaned using:
- **Morphological Closing** → fills small gaps  
- **Morphological Opening** → removes noise  
- **Gaussian Blur** → smoothens edges  

### 4️⃣ Contour Detection  
Contours are extracted from the mask.  
Small or irrelevant shapes are removed using **area thresholding**.

### 5️⃣ Counting & Visualization  
Each detected fruit is:
- Enclosed in a **green bounding box**  
- Assigned a unique number  
- Counted for the final output  

The processed image displays all detections clearly.

---

## ✅ Key Features
- Accurate fruit counting  
- Works using classical image processing (no ML model needed)  
- Robust to lighting variations  
- Simple and fast to run  

---

## 🚀 Technologies Used
- **Python**
- **OpenCV (cv2)**
- **NumPy**

---

## 📷 Example Output
Bounding boxes and numbers appear around each detected fruit, along with the total count.

---

## 📄 Summary
This project showcases strong knowledge of **image segmentation**, **contour analysis**, and **object detection**, making it ideal for agricultural automation and computer vision applications.

---
