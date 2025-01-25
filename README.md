Face and Hand Landmarks Detection

This project uses MediaPipe and OpenCV to detect face and hand landmarks in real time. The landmarks can be used for various computer vision applications, such as gesture control, sign language recognition, and drowsiness detection.


Features:

1.Detects 468 face landmarks.

2.Detects 21 landmarks each for the left and right hands.

3.Displays the landmarks in real-time on a webcam feed.

4.Calculates and shows the frames per second (FPS).

--------------------------------------------------------
Requirements->

.Python 3.6 or higher

-------------------------------------------------------
Libraries:

1.mediapipe

2.opencv-python

3.msvc-runtime

-----------------------------------------------------
Installation->

pip install mediapipe opencv-python msvc-runtime

----------------------------------------------------
How It Works->

1.MediaPipe Holistic Model: Detects and tracks face and hand landmarks.

2.OpenCV: Handles webcam input and output display.

3.Real-time Processing: Detects and draws landmarks at a calculated FPS.




-------------------------------------------------------------------------------
Example Output->

When you run the script, you will see:

1.Face landmarks (468 points).

2.Hand landmarks (21 points each for left and right hands).

3.FPS displayed on the screen.



--------------------------------------------------------------------------

Applications->

1.Sign language detection

2.Gesture-based controls

3.Drowsiness or emotion detection




------------------------------------------------------------------------
Notes->

.Ensure your webcam is connected and working.

.For better performance, ensure proper lighting.
