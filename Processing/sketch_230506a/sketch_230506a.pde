import javax.sound.midi.*;
import java.io.*;

MidiFileFormat midiFileFormat;
Sequence sequence;
Track[] tracks;
Sequencer sequencer;
int dim;


void setup() {
  size(640, 360);
  dim = width/2;
  background(0);
  colorMode(HSB, 360, 100, 100);
  noStroke();
  ellipseMode(RADIUS);
  frameRate(1);

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

    // Set up the sequencer
    sequencer = MidiSystem.getSequencer();
    sequencer.setSequence(sequence);
    sequencer.open();
    sequencer.start();
  } catch (Exception e) {
    e.printStackTrace();
  }
}

void draw() {
  background(0);
  for (int x = 0; x <= width; x+=dim) {
    drawGradient(x, height/2);
  } 
}

void drawGradient(float x, float y) {
  int radius = dim/2;
  float h = random(0, 360);
  for (int r = radius; r > 0; --r) {
    fill(h, 90, 90);
    ellipse(x, y, r, r);
    h = (h + 1) % 360;
  }
}
