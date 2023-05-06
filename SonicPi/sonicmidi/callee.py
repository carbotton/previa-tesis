from pythonosc import udp_client
import time
import sys
import os
"""
# Get the three parameters
synth = sys.argv[1]
sample = sys.argv[2]
scale = sys.argv[3]
synth_options = sys.argv[4]

client = udp_client.SimpleUDPClient('127.0.0.1', 4560)

midi_file = "D:\ORT\Proyecto\Previa\midis\Michael_Jackson_-_Billie_Jean.mid"

while True:
    # Send the MIDI file to Sonic Pi and assign the synth
    client.send_message('/load_midi', os.path.abspath(midi_file))
    client.send_message('/midi_synth', synth)
    client.send_message('/midi_synth_options', synth_options)
    client.send_message('/midi_sample', sample)
    client.send_message('/midi_scale', scale)
    time.sleep(0.5)
"""
import random
import time
client = udp_client.SimpleUDPClient('127.0.0.1', 4560)
while True:
    note = random.randint(60, 69)
    client.send_message('/trigger/note', note)
    time.sleep(1)

