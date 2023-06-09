from camera import Camera
from midi import Midi
import multiprocessing


def camera_process():
    # Create an instance of the Camera class
    camera = Camera()
    # Call the method you want to run
    camera.start()
    mp_drawing, mp_hands, hands = camera.setup_hand_tracking()
    cap = camera.setup_webcam()

def midi_process():
    # Create an instance of the MIDISender class
    midi_base = Midi()
    midi_finger = Midi()
    outport_base = midi_base.setup_midi_port()


if __name__ == '__main__':
    camera_proc = multiprocessing.Process(target=camera_process)
    midi_proc = multiprocessing.Process(target=midi_process)

    camera_proc.start()
    midi_proc.start()
