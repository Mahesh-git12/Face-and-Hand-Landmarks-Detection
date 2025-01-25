import cv2
import time
import mediapipe as mp

# Initialize Mediapipe Holistic model
mp_holistic = mp.solutions.holistic
holistic_model = mp_holistic.Holistic(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Initialize Mediapipe Drawing Utilities
mp_drawing = mp.solutions.drawing_utils

# Start capturing video from the webcam
capture = cv2.VideoCapture(0)

# Initialize variables for FPS calculation
previous_time = 0

while capture.isOpened():
    ret, frame = capture.read()
    if not ret:
        break

    # Resize the frame for better visualization
    frame = cv2.resize(frame, (800, 600))

    # Convert the BGR image to RGB
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the image using the Holistic model
    image.flags.writeable = False
    results = holistic_model.process(image)
    image.flags.writeable = True

    # Convert the RGB image back to BGR for rendering
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Draw facial landmarks
    if results.face_landmarks:
        mp_drawing.draw_landmarks(
            image,
            results.face_landmarks,
            mp_holistic.FACEMESH_CONTOURS,
            mp_drawing.DrawingSpec(color=(255, 0, 255), thickness=1, circle_radius=1),
            mp_drawing.DrawingSpec(color=(0, 255, 255), thickness=1, circle_radius=1)
        )

    # Draw right hand landmarks
    if results.right_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            results.right_hand_landmarks,
            mp_holistic.HAND_CONNECTIONS
        )

    # Draw left hand landmarks
    if results.left_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            results.left_hand_landmarks,
            mp_holistic.HAND_CONNECTIONS
        )

    # Calculate and display FPS
    current_time = time.time()
    fps = 1 / (current_time - previous_time)
    previous_time = current_time
    cv2.putText(image, f"{int(fps)} FPS", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show the output image
    cv2.imshow("Facial and Hand Landmarks", image)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
capture.release()
cv2.destroyAllWindows()
