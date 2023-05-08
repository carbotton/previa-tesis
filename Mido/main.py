import mido

# Load the MIDI file
mid = mido.MidiFile('C:/Users/majoc/OneDrive/Documents/Processing/sketch_230508c/billyjean.mid')

# Select the instrument (program) you want to use
program = 22  # 0 Piano ; 22 Harmonica

# Iterate over all messages in all tracks
for i, track in enumerate(mid.tracks):
    for msg in track:
        # Check if the message is a program change message
        if msg.type == 'program_change':
            # Set the new program (instrument)
            msg.program = program

# Play the modified MIDI file
outport = mido.open_output()
for message in mid.play():
    outport.send(message)

