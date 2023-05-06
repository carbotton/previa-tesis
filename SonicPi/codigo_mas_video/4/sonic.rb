use_bpm 120

# Play the melody
live_loop :melody do
  use_real_time
  new_synth, b, c = sync "/osc*/trigger/hola"
  
  use_synth new_synth
  sample :tabla_tas1
  
  # Define the scale
  s = scale(:a2, :major)
  # Define the rhythm
  r = [0.5, 0.25, 0.25, 1, 0.5, 0.25, 0.25, 1]
  # Define the melody
  m = [s[0], s[1], s[2], s[3], s[2], s[1], s[0], s[2]]
  
  idx = tick % m.length
  play m[idx], release: r[idx]
  sleep r[idx]
end