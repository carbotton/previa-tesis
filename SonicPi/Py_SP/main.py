"""import subprocess
from pythonosc import udp_client

# ver si se puede agregar sonicpi al path desde acá?
####

# Start Sonic Pi in headless mode
subprocess.Popen(["sonic-pi", "-H"])

# Create a UDP client to send OSC messages to Sonic Pi
sender = udp_client.SimpleUDPClient('127.0.0.1', 4560)

# Send an OSC message to play a note
# sender.send_message('/play/note', [60, 0.5])

# Define a melody as a list of notes
melody = [60, 62, 64, 65, 67, 69, 71, 72]

client = udp_client.SimpleUDPClient("127.0.0.1", 4560)

# Send an OSC message to Sonic Pi's CLI to play the melody
for note in melody:
    client.send_message("/trigger/prophet", [note, 0.5])
"""

import subprocess
subprocess.Popen(["sonic-pi", "-H"])    # Start Sonic Pi in headless mode

from pythonosc import udp_client
sender = udp_client.SimpleUDPClient('127.0.0.1', 4560)
sender.send_message('/trigger/prophet', [70, 100, 8])