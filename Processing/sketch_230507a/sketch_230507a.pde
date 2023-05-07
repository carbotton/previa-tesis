/**
 * The Mandelbrot Set
 * by Daniel Shiffman.  
 * (slight modification by l8l)
 *
 * Simple rendering of the Mandelbrot set.
 */

size(640, 360);
noLoop();
background(255);

// Establish a range of values on the complex plane
// A different range will allow us to "zoom" in or out on the fractal

// It all starts with the width, try higher or lower values
float w = 5; //tamaño, cuanto mas grande, mas lejos queda el zoom. Original w = 4.
float h = (w * height) / width;

// Start at negative half the width and height
float xmin = -w/2;
float ymin = -h/2;

// Make sure we can write to the pixels[] array.
// Only need to do this once since we don't do any other drawing.
loadPixels();

// Maximum number of iterations for each point on the complex plane
int maxiterations = 30; //original 100. Cuanto mas chico, mas deformado el mandelbrot, se ve mas suave.

// x goes from xmin to xmax
float xmax = xmin + w;
// y goes from ymin to ymax
float ymax = ymin + h;

// Calculate amount we increment x,y for each pixel
float dx = (xmax - xmin) / (width);
float dy = (ymax - ymin) / (height);

// Start y
float y = ymin;
for (int j = 0; j < height; j++) {
  // Start x
  float x = xmin;
  for (int i = 0; i < width; i++) {

    // Now we test, as we iterate z = z^2 + c does z tend towards infinity?
    float a = x;
    float b = y;
    int n = 0;
    float max = 4.0;  // Infinity in our finite world is simple, let's just consider it 4. max = 4.0 original.
    float absOld = 0.0;
    float convergeNumber = maxiterations; // this will change if the while loop breaks due to non-convergence
    while (n < maxiterations) {
      // We suppose z = a+ib
      float aa = a * a;
      float bb = b * b;
      float abs = sqrt(aa + bb);
      if (abs > max) { // |z| = sqrt(a^2+b^2)
        // Now measure how much we exceeded the maximum: 
        float diffToLast = (float) (abs - absOld);
        float diffToMax  = (float) (max - absOld);
        convergeNumber = n + diffToMax/diffToLast;
        break;  // Bail
      }
      float twoab = 2.0 * a * b;
      a = aa - bb + x; // this operation corresponds to z -> z^2+c where z=a+ib c=(x,y)
      b = twoab + y;
      n++;
      absOld = abs;
    }

    // We color each pixel based on how long it takes to get to infinity
    // If we never got there, let's pick the color black --> black = color(0) original
    if (n == maxiterations) {
      pixels[i+j*width] = color(255, 230, 112);
    } else {
      // Gosh, we could make fancy colors here if we wanted
      color[] colors = {color(51, 179, 173), color(39, 230, 112), color(233, 98, 141), color(179, 12, 149)};
      //float norm = map(convergeNumber, 0, maxiterations, 0, 1);
      //pixels[i+j*width] = color(map(sqrt(norm), 0, 1, 0, 255));
      float norm = map(convergeNumber, 0, maxiterations, 0, 1);
      int colorIndex = floor(norm * colors.length); // choose an index in the colors array based on the normalized iteration count
      pixels[i+j*width] = colors[colorIndex]; // set the pixel color      
    }
    x += dx;
  }
  y += dy;
}
updatePixels();
