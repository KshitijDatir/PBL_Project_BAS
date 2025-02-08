Markdown

# 🚀 Face Recognition System Using OpenCV



This project implements a real-time face recognition system using OpenCV. It allows users to detect faces, enroll new individuals, and train a model to recognize them.

## ✨ Features

*   **Real-time face detection:** Utilizes OpenCV for accurate and efficient face detection.
*   **User enrollment:** Easily enroll new individuals by capturing multiple images.
*   **Trainable model:** Train a face recognition model with the enrolled images for personalized recognition.
*   **Live camera feed:** Continuous face detection and recognition from your camera.
*   **Simple and intuitive:** Easy-to-use interface with clear instructions.

## 📂 Project Structure

```text
├── main.py        # Main script to run the system
├── main_detector.py # Face detection module
├── main_enroll.py  # Image enrollment module
├── main_train.py   # Training module
├── Image_DB/      # Directory to store enrolled user images
├── DB_File/People  # Text file storing enrolled user names
└── README.md      # This file
```
## 🛠 Requirements

*   Python 3.x
*   OpenCV (cv2)
*   NumPy

## 📦 Installation

1.  **Clone the repository:** (Optional - if you have the code in a repo)
    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git)  # Replace with your repo link
    cd Face-Recognition-OpenCV # Go to the project directory
    ```
2.  **Install dependencies:**
    ```bash
    pip install opencv-python numpy
    ```

## 📸 How to Use

1.  **Run the Main Script:**
    ```bash
    python main.py
    ```

2.  **Enrollment Mode:**
    *   Press `e` to enter enrollment mode.
    *   Enter the user's name when prompted.
    *   Capture images by pressing `s`.
    *   Press `q` to stop capturing and start training.

3.  **Training:**
    *   The system automatically trains on the enrolled images.
    *   New users are saved in `DB_File/People`.

4.  **Face Detection:**
    *   The live camera feed runs by default.
    *   The system attempts to recognize known faces.
    *   Press `Esc` to exit.

## 🚀 Future Enhancements

*   **Improved Accuracy:** Explore deep learning models like FaceNet or dlib for higher recognition accuracy.
*   **Database Integration:** Implement a database (e.g., SQLite) for more robust data storage instead of text files.
*   **Graphical User Interface (GUI):** Develop a GUI using Tkinter, PyQt, or similar libraries for a more user-friendly experience.
*   **Performance Optimization:** Optimize the code for faster processing and better real-time performance.
*   **Liveness Detection:** Add liveness detection to prevent spoofing attacks using photos or videos.

## 📜 License

This project is for educational purposes and is open-source. Feel free to modify and improve it!  (You can add a specific license like MIT or Apache here if you wish)

## **👥 Contributors**
This project wouldn't be possible without the help of the following contributors:

- **[Sojo06 (Soham Joshi)](https://github.com/Sojo06)**
- **[KshitijDatir (Kshitij Datir)](https://github.com/KshitijDatir)**


