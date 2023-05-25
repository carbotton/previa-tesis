import mediapipe as mp  # for hand tracking
import numpy as np
import pyaudio
import cv2  # for image processing
import mido

def map_to_a_minor(pitch):
    pitch_class = (pitch - 21) % 12
    scale = [0, 2, 3, 5, 7, 8, 10]
    scale_pitch_class = min(scale, key=lambda x: abs(x - pitch_class))
    pitch_in_scale = ((pitch - pitch_class) - 21) + scale_pitch_class
    return pitch_in_scale

def map_to_midi_range(value):
    return int((value/2000)*127)

def setup_audio_stream():
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=True)
    return p, stream

def setup_hand_tracking():
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)
    return mp_drawing, mp_hands, hands

def get_camera_frame(cap):
    ret, frame = cap.read()  # ret:bool indicates whether a frame was successfully read. frame: actual image data.
    frame = cv2.flip(frame, 1)  # flip frame horizontally
    return ret, frame

def setup_webcam():
    cap = cv2.VideoCapture(0)  # set up computer's webcam as video source for hand tracking
    return cap

def setup_midi_port():
    print(mido.get_output_names())
    outport = mido.open_output('loopmidi 1')
    return outport

def process_hand_landmarks(frame, hand_landmarks, mp_drawing, mp_hands, overlay_img, outport):
    index_finger_landmark = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    x, y = int(index_finger_landmark.x * frame.shape[1]), int(index_finger_landmark.y * frame.shape[0])

    overlay_color = tuple(map(int, overlay_img[y, x]))
    cv2.circle(frame, (x, y), 5, overlay_color, -1)

    r, g, b,  = overlay_color
    hue = (r + g + b) / 3  # average hue value of overlay color
    new_pitch = int(np.interp(hue, [0, 255], [100, 2000]))
    new_pitch = map_to_a_minor(new_pitch)
    outport.send(mido.Message('note_on', note=map_to_midi_range(new_pitch), velocity=64))

    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    cv2.putText(frame, 'Index finger', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA)

def cleanup(cap, hands, stream, p, outport):
    cap.release()
    hands.close()
    stream.stop_stream()
    stream.close()
    p.terminate()
    cv2.destroyAllWindows()
    outport.close()

def main():
    p, stream = setup_audio_stream()
    mp_drawing, mp_hands, hands = setup_hand_tracking()
    cap = setup_webcam()
    outport = setup_midi_port()
    overlay_img = cv2.imread('source/imgs/mandelbrot.jpg', cv2.IMREAD_UNCHANGED)
    overlay_img = cv2.resize(overlay_img, (1280, 720))

    while True:
        ret, frame = get_camera_frame(cap)
        if not ret:
            break

        results = hands.process(frame)
        if results.multi_hand_landmarks:
            hand_landmarks = results.multi_hand_landmarks[0]  # first hand is selected
            process_hand_landmarks(frame, hand_landmarks, mp_drawing, mp_hands, overlay_img, outport)

        overlay_img = cv2.resize(overlay_img, (frame.shape[1], frame.shape[0])) # because sizes were (720, 1280, 3) and (480, 640, 3) and this caused error in cv2.addWeighted()

        alpha = 0.5
        cv2.addWeighted(overlay_img, alpha, frame, 1 - alpha, 0, frame)  # blends 2 images; result stored in frame
        cv2.imshow('Hand Tracking', frame)  # display frame image in a window titled Hand Tracking
        if cv2.waitKey(1) & 0xFF == ord('q'):  # wait for key press for 1 second. If 'q' is pressed, programm exits.
            break

    cleanup(cap, hands, stream, p, outport)

if __name__ == "__main__":
    main()