# Welcome to Sonic Pi
in_thread do
  loop do
    sample :loop_amen
    sleep 1.753
  end
end

in_thread do
  16.times do
    play 75
    sleep 1.753
    play 74
    sleep 0.25
  end
end
