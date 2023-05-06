from pythonosc import udp_client
from random import randint
import time
import sys
import select

# Get the three parameters
#synth = sys.argv[1]
#sample = sys.argv[2]
#scale = sys.argv[3]

sender = udp_client.SimpleUDPClient('127.0.0.1', 4560)

synth = 'piano'
sample = 'bass_hit_c'
scale = 'c3'

while True:
    # Check if there is input available
    if select.select([sys.stdin,],[],[],0.0)[0]:
        # Read the input and do something with it
        user_input = input()
        print("You entered:", user_input)
        """inputsynth = input("synth: ejemplo piano, rodeo, kalimba ")
        inputsample = input("sample: ejemplo bass_hit_c, drum_heavy_kick, tabla_tas3 ")
        inputscale = input("scale: ejemplo a4, c3, e5 ")
        if inputsynth:
            synth = inputsynth
        elif inputsample:
            sample = inputsample
        elif inputscale:
            scale = inputscale        
        """
    else:
        # Do something else while waiting for input
        sender.send_message('/trigger/hola', [str(synth), str(sample), str(scale)])
        time.sleep(0.5)


