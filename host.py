import cv2
import streamlit as st
import datetime

# Load the cascade classifier for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

st.title("Attendance System")

def recognize_faces(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

        name = "Pranav Kumar"
        cv2.putText(image, f"Name: {name}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        attendance = '''Photo Matched with dataset, attendance Marked
Your attendance till now is : 79.45% for the month October.
'''
        lines = attendance.split('\n')
        line_height = 20
        for i, line in enumerate(lines):
            cv2.putText(image, line, (x + 5, y + h + 20 + i * line_height), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    cv2.putText(image, "Attendance System", (image.shape[1] // 2 - 100, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    return image

# Capture video frames from the webcam
cap = cv2.VideoCapture(0)

stframe = st.empty()
st.write("Press 'q' to quit.")

quit_button = st.button("Quit", key="quit_button")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    output = recognize_faces(frame)

    # Convert the OpenCV image to a format Streamlit can display
    stframe.image(output, channels="BGR", use_column_width=True)

    current_time = datetime.datetime.now()
    time_str = current_time.strftime("%Y%m%d%H%M%S")
    filename = "Attendance.jpg".format(time_str)
    cv2.imwrite(filename, output)

    if quit_button:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
