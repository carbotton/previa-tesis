#synth :beep by default for play
#Frère Jacque

use_synth :fm

2.times do
  #play midi_note_number
  play 60
  sleep 0.5
  play 62
  sleep 0.5
  play 64
  sleep 0.5
  play 60
  sleep 0.5
end

2.times do
  play 64
  sleep 0.5
  play 65
  sleep 0.5
  play 67
  sleep 1
end