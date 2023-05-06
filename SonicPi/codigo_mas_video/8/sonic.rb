use_bpm 120

# Play the melody
live_loop :melody do
  use_real_time
  new_synth, new_sample, new_scale = sync "/osc*/trigger/hola"
  
  use_synth new_synth
  
  s = scale(new_scale, :major) #scale
  
  if new_scale == 'a4'
    sample new_sample
    r = [0.5, 0.25, 0.25, 1, 0.25, 2, 1, 0.25] #rythm
    m = [s[0], s[1], s[2], s[3], s[2], s[1], s[0], s[2]] #melody
    aux = tick % m.length #tick default 0.25 seconds
    play m[aux], release: r[aux]
    sleep r[aux]
  else
    sample :drum_heavy_kick
    play_chord [:c4, :e4, :g4], release: 0.5
    sleep 0.5
  end
  
end