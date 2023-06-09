import numpy as np
import mido


class Midi:
    def __init__(self, name):
        self.name = name

    def map_to_a_minor(self, pitch):
        pitch_class = (pitch - 21) % 12
        scale = [0, 2, 3, 5, 7, 8, 10]
        scale_pitch_class = min(scale, key=lambda x: abs(x - pitch_class))
        pitch_in_scale = ((pitch - pitch_class) - 21) + scale_pitch_class
        return pitch_in_scale

    def map_to_midi_range(self, value):
        return int((value/2000)*127)

    #def setup_audio_stream(self):
    #    p = pyaudio.PyAudio()
    #    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=True)
    #    return p, stream

    def setup_midi_port(self):
        print(mido.get_output_names())
        outport = mido.open_output('loopmidi 1')
        return outport

    def send_midi_signal(self, outport, overlay_color):
        """
        Send MIDI signal based on the overlay color.

        Args:
            outport: The MIDI output port to send the signal.
            overlay_color: The color of the overlay at the index finger tip.
        """
        r, g, b,  = overlay_color
        hue = (r + g + b) / 3  # average hue value of overlay color
        new_pitch = int(np.interp(hue, [0, 255], [100, 2000]))
        new_pitch = self.map_to_a_minor(new_pitch)
        outport.send(mido.Message('note_on', note=self.map_to_midi_range(new_pitch), velocity=64))
