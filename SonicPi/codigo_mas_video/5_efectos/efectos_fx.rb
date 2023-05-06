with_fx :reverb do
  sample :guit_e_fifths
end

sleep 3

with_fx :reverb do
  with_fx :distortion do
    sample :guit_e_fifths
  end
end

sleep 3

with_fx :wobble do
  sample :guit_e_fifths
end