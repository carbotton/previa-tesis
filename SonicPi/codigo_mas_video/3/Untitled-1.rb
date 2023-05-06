live_loop :foo do
  use_real_time
  a, b, c = sync "/osc*/trigger/prophet"
  synth :kalimba, note: a, cutoff: b, sustain: c
  with_fx :reverb, mix: 0.5 do
    g, h, i = sync "/osc*/trigger/fm"
    synth :dull_bell, note: g, cutoff: h, sustain: i
  end
end