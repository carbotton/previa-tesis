use_bpm 120

# Play the melody
live_loop :melody do
  use_real_time
  note = sync "/osc*/trigger/note"

end


