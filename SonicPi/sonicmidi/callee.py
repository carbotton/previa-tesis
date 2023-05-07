from pythonosc import udp_client
import mido
import time
import sys
import os
"""
# Get the three parameters
synth = sys.argv[1]
sample = sys.argv[2]
scale = sys.argv[3]
synth_options = sys.argv[4]



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

client = udp_client.SimpleUDPClient('127.0.0.1', 4560)

# Open the MIDI file and print some information about it
midi_file = "D:\ORT\Proyecto\Previa\midis\Michael_Jackson_-_Billie_Jean.mid"
mid = mido.MidiFile(midi_file)
tpb = mid.ticks_per_beat
bpm = 120
seconds_per_tick = 60.0 / (bpm * tpb)

"""while True:
    # Iterate over each track in the MIDI file
    for i, track in enumerate(mid.tracks):
        #print(f'Track {i}: {track.name}')
        # Iterate over each message in the track
        for msg in track:
            # If the message is a note_on message, print the note number
            if msg.type == 'note_on':
                note = msg.note
                #client.send_message('/trigger/note', [note, seconds_per_tick])
                print(note)
                print(tpb)
                print(seconds_per_tick)
    time.sleep(2)
"""

# Iterate over all MIDI messages in the file
time = 0
for msg in mid.play():
    if msg.type == 'note_on':
        print(f"Note: {msg.note} - Start Time: {time:.3f}")
        client.send_message('/trigger/note', msg.note)
    time += seconds_per_tick * msg.time

