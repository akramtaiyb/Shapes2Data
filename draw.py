import cv2
import numpy as np
import random

# Increase the canvas size
canvas = np.ones((500, 500), dtype=np.uint8) * 255
background_color = 255
line_color = 0

drawing = False
prev_point = None
shape_type = 1
shape_count = [0, 0, 0, 0]  # Counters for each shape type
line_ckness = 10

shape_names = ["Carre", "Triangle", "Rectangle", "Cercle"]

def draw(event, x, y, flags, param):
    global drawing, prev_point
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        prev_point = (x, y)
    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        cv2.line(canvas, prev_point, (x, y), line_color, line_thickness)  # Draw with a variable line thickness
        prev_point = (x, y)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        prev_point = None

def change_thickness():
    global line_thickness
    line_thickness = random.randint(10, 25)
    print(f"Line thickness changed to {line_thickness}")

def switch_background():
    global canvas, background_color, line_color
    if background_color == 255:
        background_color = 0
        line_color = 255
    else:
        background_color = 255
        line_color = 0
    canvas.fill(background_color)
    print("Background switched!")

cv2.namedWindow("Shape2Data")
cv2.setMouseCallback("Shape2Data", draw)

while True:
    canvas_copy = canvas.copy()
    instructions = [
        "'s' pour sauvegarder",
        "'q' pour quitter",
        "'r' pour reinitialiser",
        "'b': white/black en black/white",
        "1: Carre, 2: Triangle, 3: Rectangle, 4: Cercle"
    ]
    for i, instruction in enumerate(instructions[:-1]):
        cv2.putText(canvas_copy, instruction, (10, 20 + i * 20), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (line_color), 1, cv2.LINE_AA)
    
    # Draw the last instruction at the left bottom of the canvas
    last_instruction = instructions[-1]
    cv2.putText(canvas_copy, last_instruction, (10, canvas_copy.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (line_color), 1, cv2.LINE_AA)
    
    # Draw a center '+' on the canvas copy
    center_x, center_y = canvas_copy.shape[1] // 2, canvas_copy.shape[0] // 2
    cv2.line(canvas_copy, (center_x - 10, center_y), (center_x + 10, center_y), line_color, 1)
    cv2.line(canvas_copy, (center_x, center_y - 10), (center_x, center_y + 10), line_color, 1)
    
    # Display shape name and count on the top right
    shape_info = f"{shape_names[shape_type - 1]}: {shape_count[shape_type - 1]}"
    cv2.putText(canvas_copy, shape_info, (canvas_copy.shape[1] - 100, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (line_color), 1, cv2.LINE_AA)
    
    cv2.imshow("Shape2Data", canvas_copy)
    
    key = cv2.waitKey(1) & 0xFF
    if key == ord("s"):  # Press 's' to save
        shape_count[shape_type - 1] += 1
        filename = f"images/{shape_type}-{shape_count[shape_type - 1]}.png"
        resized_canvas = cv2.resize(canvas, (64, 64), interpolation=cv2.INTER_AREA)
        cv2.imwrite(filename, resized_canvas)
        print(f"Saved as {filename}!")
        canvas.fill(background_color)
        prev_point = None  # Reset prev_point
        change_thickness()
    elif key == ord("q") or cv2.getWindowProperty("Shape2Data", cv2.WND_PROP_VISIBLE) < 1:  # Press 'q' to quit
        break
    elif key == ord("r"):  # Press 'r' to reset the canvas
        canvas.fill(background_color)
        prev_point = None  # Reset prev_point
        print("Canvas reset!")
        change_thickness()
    elif key == ord("b"):  # Press 'b' to switch background
        switch_background()
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
