use_bpm ARGV[0].to_i #tempo
use_synth :piano
set :key, :C

notes = (1..8).map { rand_i(12) } #generate 8 random numbers (notes) between 0 and 11

sc = scale(:c, :major_pentatonic) #map numbers to C major pentatonic scale
notes = notes.map { |n| sc[n] }

notes.each do |n|
  play n, release: 0.5 #play for half a beat
  sleep 0.5 #sleep for half a beat
end

play scale(:C, :major).tick, release: 0.25, sustain: 0.25
sleep ARGV[1].to_f

