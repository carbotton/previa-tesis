import javax.sound.midi.*;

MidiFileFormat midiFileFormat;
Sequence midi;
Track[] tracks;

float zoom = 1.0;
float x = -0.5;
float y = 0.0;

void setup() {
  size(800, 800);
  background(255);
  
  try {
    // Load the MIDI file
    File file = new File("C:/Users/majoc/OneDrive/Documents/Processing/sketch_230506a/data/billyjean.mid");
    midi = MidiSystem.getSequence(file);
    midiFileFormat = MidiSystem.getMidiFileFormat(file);
    
    // Get the tracks from the MIDI file
    tracks = midi.getTracks();
    
    // Print some information about the MIDI file
    println("MIDI file format type: " + midiFileFormat.getType());
    println("Number of tracks: " + tracks.length);
    
    // Start playing the MIDI file
    Sequencer sequencer = MidiSystem.getSequencer();
    sequencer.open();
    sequencer.setSequence(midi);
    sequencer.start();
  } catch (Exception e) {
    e.printStackTrace();
  }
}

void draw() {
  // Generate the mandelbrot fractal image
  loadPixels();
  for (int i = 0; i < width; i++) {
    for (int j = 0; j < height; j++) {
      float a = map(i, 0, width, x - zoom, x + zoom);
      float b = map(j, 0, height, y - zoom, y + zoom);
      float ca = a;
      float cb = b;
      int n = 0;
      while (n < 100) {
        float aa = a * a - b * b;
        float bb = 2 * a * b;
        a = aa + ca;
        b = bb + cb;
        if (abs(a + b) > 16) {
          break;
        }
        n++;
      }
      float bright = map(n, 0, 100, 0, 255);
      bright = (bright + (millis() / 4)) % 255;
      if (n == 100) {
        bright = 0;
      }
      pixels[i + j * width] = color(bright);
    }
  }
  updatePixels();
}
