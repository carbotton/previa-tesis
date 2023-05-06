use_bpm 120

notes = [60, 62, 64, 65, 67, 69, 71, 72]

in_thread do
  loop do
    midi_note = sync "/osc*/note"
    play notes[midi_note[0]], release: 0.5
  end
end

# Wait for input
sleep 1

# Generate sequence based on input values
seq = []
in_thread do
  loop do
    seq << sync("/osc*/value").to_f
  end
end

# Play sequence
seq.each do |n|
  play notes[n], release: 0.5
end

# Save output as .wav file
sample :guit_e_fifths, amp: 0.5, rate: 0.5, sustain: seq.length / 2.0
save_wav("output.wav")