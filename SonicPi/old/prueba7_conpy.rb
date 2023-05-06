use_osc "127.0.0.1", 4556

live_loop :receive_note do
  # Receive an OSC message with a value and play a note with that value
  note = sync "/osc/play/note"
  play note[0]
end