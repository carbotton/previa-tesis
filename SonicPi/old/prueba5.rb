source_file = "D:/ORT/Proyecto/Previa/SonicPi/prueba4.rb"

save_file = "D:/ORT/Proyecto/Previa/SonicPi/prueba4.wav"

osc_send "localhost",4557, "/start-recording","myGUID"

sleep 0.5 #lead in time

run_file source_file #add line cue :finish at end of each source file

sync :finish

sleep 0.5 #lead_out time

osc_send "localhost",4557, "/stop-recording","myGUID"

sleep 0.5

osc_send "localhost",4557, "/save-recording","myGUID",save_file

sleep 1 #allow time for the file to be saved to media
