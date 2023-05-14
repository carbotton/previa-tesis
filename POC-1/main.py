import mediapipe as mp
import numpy as np
import pyaudio
import cv2


def map_to_a_minor(pitch):
    # Calculate pitch class
    pitch_class = (pitch - 21) % 12

    # Map pitch class to A minor scale
    scale = [0, 2, 3, 5, 7, 8, 10]
    scale_pitch_class = min(scale, key=lambda x: abs(x - pitch_class))

    # Calculate pitch in A minor scale
    pitch_in_scale = ((pitch - pitch_class) - 21) + scale_pitch_class

    return pitch_in_scale


# Setup audio stream
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=True)

# Setup hand tracking
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)

# Setup sine wave parameters
frequency = 440  # starting frequency
sample_rate = 44100
duration = 1  # duration of each sine wave sample in seconds
t = np.linspace(0, duration, int(sample_rate * duration), False)

# Setup webcam
cap = cv2.VideoCapture(0)

# Load image to overlay
overlay_img = cv2.imread('source/mandelbrot.jpg', cv2.IMREAD_UNCHANGED)
overlay_img = cv2.resize(overlay_img, (1280, 720))

while True:
    # Get camera frame
    ret, frame = cap.read()
    if not ret:
        break

    # Get hand landmarks
    results = hands.process(frame)
    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]

        # Get position of index finger
        index_finger_landmark = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
        x, y = int(index_finger_landmark.x * frame.shape[1]), int(index_finger_landmark.y * frame.shape[0])

        # Map finger position to color
        overlay_color = tuple(map(int, overlay_img[y, x]))
        cv2.circle(frame, (x, y), 5, overlay_color, -1)

        # Map color to pitch
        r, g, b,  = overlay_color
        hue = (r + g + b) / 3
        pitch = int(np.interp(hue, [0, 255], [100, 2000]))
        pitch=map_to_a_minor(pitch)
        # Generate sine wave
        frequency = 440 * (2 ** ((pitch - 1000) / 1200))  # convert pitch to frequency
        sine_wave = np.sin(2 * np.pi * frequency * t).astype(np.float32)

        # Play sine wave
        stream.write(sine_wave)

        # Draw finger position and overlay image on frame
        mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        cv2.putText(frame, 'Index finger', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA)

    alpha = 0.5

    # print(overlay_img.shape)  # should be (height, width, num_channels)
    # print(frame.shape)  # should be (height, width, num_channels)
    overlay_img = cv2.resize(overlay_img, (frame.shape[1], frame.shape[0])) # esta linea es porque los sizes daban (720, 1280, 3) y (480, 640, 3) y eso daba error en cv2.addWeighted()

    cv2.addWeighted(overlay_img, alpha, frame, 1 - alpha, 0, frame)
    cv2.imshow('Hand Tracking', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# Clean up
cap.release()
hands.close()
stream.stop_stream()
stream.close()
p.terminate()
cv2.destroyAllWindows()

