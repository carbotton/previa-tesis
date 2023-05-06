#use_debug false # if code is slow
with_fx :record, buffer: :my_recording do
  synth :sound_in
  
  #live_loop :foo do
  #  use_real_time
  #  a, b, c = sync "/osc*/trigger/prophet"
  #  synth :prophet, note: a, cutoff: b, sustain: c
  #end
  
  live_loop :foo2 do
    x, y, z = sync "/osc*/trigger/majorpenta"
    use_synth :pulse
    play_pattern [45,48,50] # sleep = 1
    
    use_synth :fm
    play_pattern_timed [45,48,50,52,52], [1,1,1,2,2] # sleep != 1
    
    use_synth :piano
    play_chord [60,64,67]
    sleep 0.5
    play_chord [67,71,62]
    sleep 0.5
    play_chord [69,72,76]
    sleep 0.5
    play_chord [65,69,60,72]
  end
end

#saves to C:\Users\majoc\.sonic-pi\store\default\cached_samples
live_loop :a_loop do
  sample buffer[:my_recording4]
  sleep 1
end