# Welcome to Sonic Pi
in_thread do
  loop do
    sample :tabla_tas3
    sleep 0.5
  end
end

in_thread do
  16.times do
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
  end
end
