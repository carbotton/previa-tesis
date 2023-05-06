use_bpm 120 #tempo 120
use_synth :piano
set :key, :C

notes = (1..8).map { rand_i(12) } #generate 8 random numbers (notes) between 0 and 11

sc = scale(:c, :major_pentatonic) #map numbers to C major pentatonic scale
notes = notes.map { |n| sc[n] }

notes.each do |n|
  play n, release: 0.5 #play for half a beat
  sleep 0.5 #sleep for half a beat
end

use_bpm 120 #tempo 120
use_synth :beep
set :key, :C

notes = (1..8).map { rand_i(12) } #generate 8 random numbers (notes) between 0 and 11

sc = scale(:c, :major_pentatonic) #map numbers to C major pentatonic scale
notes = notes.map { |n| sc[n] }

notes.each do |n|
  play n, release: 0.5 #play for half a beat
  sleep 0.5 #sleep for half a beat
end

sample :ambi_lunar_land
sleep 4

sample :ambi_drone
sleep 1

3.times do
  play 60
  sleep 0.5
  play 62
  sleep 0.5
  play 64
  sleep 0.5
  play 60
  sleep 0.5
end

use_synth :pluck
2.times do
  play 60
  sleep 0.5
  play 62
  sleep 0.5
  play 64
  sleep 0.5
  play 60
  sleep 0.5
end


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
