import javax.sound.midi.*;

MidiFileFormat midiFileFormat;
Sequence sequence;
Track[] tracks;

float time = 0;

void setup() {
  size(400, 400);
  background(255);
  
  try {
    // Load the MIDI file
    File file = new File("C:/Users/majoc/OneDrive/Documents/Processing/sketch_230506a/data/billyjean.mid");
    sequence = MidiSystem.getSequence(file);
    midiFileFormat = MidiSystem.getMidiFileFormat(file);
    
    // Get the tracks from the MIDI file
    tracks = sequence.getTracks();
    
    // Print some information about the MIDI file
    println("MIDI file format type: " + midiFileFormat.getType());
    println("Number of tracks: " + tracks.length);
  } catch (Exception e) {
    e.printStackTrace();
  }
  
  // Start playing the MIDI file
  try {
    Sequencer sequencer = MidiSystem.getSequencer();
    sequencer.setSequence(sequence);
    sequencer.open();
    sequencer.start();
  } catch (Exception e) {
    e.printStackTrace();
  }
}

void draw() {
  background(255);
  time = map(millis(), 0, sequence.getMicrosecondLength() / 1000, 0, width);
  stroke(0);
  line(time, 0, time, height);
}
