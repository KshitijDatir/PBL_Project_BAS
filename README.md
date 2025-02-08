#Face Recognition System Using OpenCV

This project implements a real-time face recognition system using OpenCV. It allows users to detect faces, enroll new individuals, and train a model to recognize them.

🚀 Features

Real-time face detection using OpenCV.

Enroll new users by capturing images.

Train a face recognition model with enrolled images.

Live camera feed for continuous detection.

📂 Project Structure

├── main.py                # Main script to run the system
├── main_detector.py       # Face detection module
├── main_enroll.py         # Image enrollment module
├── main_train.py          # Training module
├── Image_DB/             # Directory to store enrolled user images
├── DB_File/People        # Text file storing enrolled user names
└── README.md             # Project documentation

🛠 Requirements

Python 3.x

OpenCV (cv2)

NumPy

Install Dependencies

Run the following command:

pip install opencv-python numpy

📸 How to Use

1️⃣ Run the Main Script

python main.py

2️⃣ Enrollment Mode

Press e to enter enrollment mode.

Enter the user's name when prompted.

Capture images by pressing s.

Press q to stop capturing and start training.

3️⃣ Training

The system automatically trains on enrolled images.

New users are saved in DB_File/People.

4️⃣ Face Detection

The live camera feed runs by default.

The system attempts to recognize known faces.

Press Esc to exit.

🏗 Future Enhancements

Improve accuracy using deep learning (e.g., FaceNet, dlib).

Implement database storage instead of text files.

Add GUI for easier interaction.

📜 License

This project is for educational purposes and is open-source. Feel free to modify and improve it!

