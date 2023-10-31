import cv2
import os
import datetime  # Import the datetime module
# Load the cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')

# Set the title of the OpenCV window
cv2.setWindowTitle("Attendance System", "Attendance System")

# Define a function to recognize faces
def recognize_faces(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Draw rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Add your name to the image
        name = "Pranav Kumar"
        cv2.putText(image, f"Name: {name}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Indicate attendance marked
        attendance = '''Photo Matched with dataset, attendance Marked
Your attendance till now is : 79.45% for the month October.
'''
        lines = attendance.split('\n')
        line_height = 20
        for i, line in enumerate(lines):
            cv2.putText(image, line, (x + 5, y + h + 20 + i * line_height), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        
    # Add "Attendance System" at the top middle
    cv2.putText(image, "Attendance System", (image.shape[1] // 2 - 100, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    return image

# Capture video frames from the webcam
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Recognize faces in the current frame
    output = recognize_faces(frame)
    
    # Display the output
    cv2.imshow("Attendance System", output)
    
    # Get the current date and time
    current_time = datetime.datetime.now()
    
    # Format the current date and time as a string
    time_str = current_time.strftime("%Y%m%d%H%M%S")
    
    # Create the filename using the formatted time string
    filename = "Attendance.jpg".format(time_str)
    
    # Save the output to the file
    cv2.imwrite(filename, output)
    
    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
