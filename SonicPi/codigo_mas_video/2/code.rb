live_loop :foo do
  use_real_time
  #g, h, i = sync "/osc*/trigger/pulse"
  #synth :pulse, note: g, cutoff: h, sustain: i, pan: 1
  a, b, c = sync "/osc*/trigger/prophet"
  synth :prophet, note: a, cutoff: b, sustain: c, amp:0.5
  #d, e, f = sync "/osc*/trigger/saw"
  #synth :saw, note: d, cutoff: e, sustain: f
  #sleep 0.5
  #g, h, i = sync "/osc*/trigger/tb303"
  #synth :tb303, note: g, cutoff: h, sustain: i
  #sleep 0.5
  #g, h, i = sync "/osc*/trigger/dsaw"
  #synth :dsaw, note: g, cutoff: h, sustain: i
  g, h, i = sync "/osc*/trigger/fm"
  synth :fm, note: g, cutoff: h, sustain: i
end