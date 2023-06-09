import mediapipe as mp  # for hand tracking
import cv2  # for image processing


class Camera:
    def __init__(self, name):
        self.name = name

    def setup_hand_tracking(self):
        mp_drawing = mp.solutions.drawing_utils
        mp_hands = mp.solutions.hands
        hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)
        return mp_drawing, mp_hands, hands

    def get_camera_frame(self, cap):
        overlay_img = cv2.imread('source/imgs/mandelbrot.jpg', cv2.IMREAD_UNCHANGED)
        ret, frame = cap.read()  # ret:bool indicates whether a frame was successfully read. frame: actual image data.
        frame = cv2.flip(frame, 1)  # flip frame horizontally
        overlay_img = cv2.resize(overlay_img, (frame.shape[1], frame.shape[0])) # because sizes were (720, 1280, 3) and (480, 640, 3) and this caused error in cv2.addWeighted()
        return ret, frame

    def setup_webcam(self):
        cap = cv2.VideoCapture(0)  # set up computer's webcam as video source for hand tracking
        return cap

    def get_index_finger_position(self, frame, hand_landmarks, mp_hands):
        """
        Get the position of the index finger tip.

        Args:
            frame: The input frame or image.
            hand_landmarks: Hand landmarks obtained from hand tracking.
            mp_hands: mediapipe Hands module.

        Returns:
            x: x-coordinate of the index finger tip.
            y: y-coordinate of the index finger tip.
        """
        index_finger_landmark = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
        x, y = int(index_finger_landmark.x * frame.shape[1]), int(index_finger_landmark.y * frame.shape[0])
        return x, y

    def draw_index_finger_circle(self, frame, x, y, overlay_img):
        """
        Draw a circle around the index finger tip.

        Args:
            frame: The input frame or image.
            x: x-coordinate of the index finger tip.
            y: y-coordinate of the index finger tip.
            overlay_img: The overlay image used for color.

        Returns:
            overlay_color: The color of the overlay at the index finger tip.
        """
        overlay_color = tuple(map(int, overlay_img[y, x]))
        cv2.circle(frame, (x, y), 5, overlay_color, -1)
        return overlay_color

    def draw_hand_landmarks(self, frame, hand_landmarks, mp_drawing, mp_hands):
        """
        Draw hand landmarks on the frame.

        Args:
            frame: The input frame or image.
            hand_landmarks: Hand landmarks obtained from hand tracking.
            mp_drawing: mediapipe Drawing module.
            mp_hands: mediapipe Hands module.
        """
        mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    def label_index_finger(self, frame, x, y):
        """
        Label the index finger on the frame.

        Args:
            frame: The input frame or image.
            x: x-coordinate of the index finger tip.
            y: y-coordinate of the index finger tip.
        """
        cv2.putText(frame, 'Index finger', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA)
