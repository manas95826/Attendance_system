# Attendance System with Face Recognition

This is a Python-based attendance system that uses face recognition to mark attendance. The system captures video frames from a webcam, detects faces in the frames, and marks the attendance of recognized individuals.

## Features

- Face detection and recognition using Haar Cascade Classifier
- Overlaying the detected person's name on the video feed
- Displaying attendance information
- Saving the marked attendance in an image

## Usage

1. Clone the repository to your local machine:

    ```bash
    git clone [<repository-url>](https://github.com/manas95826/Attendance_system)
    ```

2. Install the required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the system:

    ```bash
    python app.py
    ```

4. The system will display the video feed from your webcam. After 3 seconds, it will start recognizing faces and mark attendance.

5. Press 'q' to quit the system.

## Configuration

- You can configure the attendance system by modifying the code in `attendance_system.py`.
- Adjust the Haar Cascade Classifier and other parameters for face detection as needed.
- Customize the attendance information displayed on the video feed.

## Author

- Manas Chopra

## License

This project is licensed under the [License Name] License - see the [LICENSE](LICENSE) file for details.
