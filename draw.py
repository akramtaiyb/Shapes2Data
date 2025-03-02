import cv2
import numpy as np
import random

# Increase the canvas size
canvas = np.ones((256, 256), dtype=np.uint8) * 255

drawing = False
prev_point = None
shape_type = 1
shape_count = [0, 0, 0, 0]  # Counters for each shape type
line_thickness = 4

def draw(event, x, y, flags, param):
    global drawing, prev_point
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        prev_point = (x, y)
    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        cv2.line(canvas, prev_point, (x, y), 0, line_thickness)  # Draw in black with a variable line thickness
        prev_point = (x, y)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        prev_point = None

def change_thickness():
    global line_thickness
    line_thickness = random.randint(1, 14)
    print(f"Line thickness changed to {line_thickness}")

cv2.namedWindow("Draw")
cv2.setMouseCallback("Draw", draw)

while True:
    cv2.imshow("Draw", canvas)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("s"):  # Press 's' to save
        shape_count[shape_type - 1] += 1
        filename = f"images/{shape_type}-{shape_count[shape_type - 1]}.png"
        resized_canvas = cv2.resize(canvas, (64, 64), interpolation=cv2.INTER_AREA)
        cv2.imwrite(filename, resized_canvas)
        print(f"Saved as {filename}!")
        change_thickness()
    elif key == ord("q"):  # Press 'q' to quit
        break
    elif key == ord("r"):  # Press 'r' to reset the canvas
        canvas.fill(255)
        print("Canvas reset!")
        change_thickness()
    elif key == ord("1"):  # Press '1' for Carré
        shape_type = 1
        print("Shape type set to Carré")
    elif key == ord("2"):  # Press '2' for Triangle
        shape_type = 2
        print("Shape type set to Triangle")
    elif key == ord("3"):  # Press '3' for Rectangle
        shape_type = 3
        print("Shape type set to Rectangle")
    elif key == ord("4"):  # Press '4' for Cercle
        shape_type = 4
        print("Shape type set to Cercle")

cv2.destroyAllWindows()
