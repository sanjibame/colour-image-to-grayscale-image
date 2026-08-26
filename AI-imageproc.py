import cv2
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("1.jpeg")

# Convert BGR to Grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur to reduce noise
blurred = cv2.GaussianBlur(gray_img, (5, 5), 0)

# Perform Canny Edge Detection
edges = cv2.Canny(blurred, 100, 200)

# Save or display output
cv2.imwrite("output_edges.jpg", edges)
