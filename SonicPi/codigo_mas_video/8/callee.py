from pythonosc import udp_client
import time
import sys

# Get the three parameters
synth = sys.argv[1]
sample = sys.argv[2]
scale = sys.argv[3]

sender = udp_client.SimpleUDPClient('127.0.0.1', 4560)

while True:
    sender.send_message('/trigger/hola', [synth, sample, scale])
    time.sleep(0.5)
