import mido
import time

# Set up MIDI output port
output = mido.open_output()

# Load MIDI file
#mid = mido.MidiFile('C:/Users/majoc/OneDrive/Documents/Processing/sketch_230508c/billyjean.mid')
mid = mido.MidiFile("magenta_2023-03-19_212732_009.mid")

# Define instruments
piano = 0
accordion = 21

# Set initial instrument
current_instrument = piano

# Define timer variables
interval = 2  # Time in seconds between instrument changes
last_time = time.time()

# Iterate through MIDI file
for msg in mid.play():

    # Check if it's time to switch instruments
    if time.time() - last_time >= interval:
        last_time = time.time()

        # Switch instrument
        if current_instrument == piano:
            current_instrument = accordion
        else:
            current_instrument = piano

        # Send program change message to MIDI output
        output.send(mido.Message('program_change', program=current_instrument))

    # Send MIDI message to output
    output.send(msg)


