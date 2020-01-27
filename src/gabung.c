
// defines pins numbers

const int trigPin = 2;  //D4
const int echoPin = 0;  //D3
const int ledPin = 4;  //D2
const int buzzerPin = 5;  //D1


// defines variables
long duration;
int distance;
int safetyDistance;

void setup() {


pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
pinMode(echoPin, INPUT); // Sets the echoPin as an Input
pinMode(buzzerPin, OUTPUT);
pinMode(ledPin, OUTPUT);
Serial.begin(115200); // Starts the serial communication
}

void loop() {

// Clears the trigPin
digitalWrite(trigPin, LOW);
delayMicroseconds(2);

// Sets the trigPin on HIGH state for 10 micro seconds
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);

// Reads the echoPin, returns the sound wave travel time in microseconds
duration = pulseIn(echoPin, HIGH);

// Calculating the distance
distance= duration*0.034/2;
// Prints the distance on the Serial Monitor
//Serial.print("Distance: ");
//Serial.println(distance);
//delay(2000);

safetyDistance = distance;
if (safetyDistance <= 5){
  digitalWrite(buzzerPin, HIGH);
  digitalWrite(ledPin, HIGH);
}
else{
  digitalWrite(buzzerPin, LOW);
  digitalWrite(ledPin, LOW);
}

// Prints the distance on the Serial Monitor
Serial.print("Distance: ");
Serial.println(distance);
Serial.print("pulseIn ");
Serial.print("duration ");
}

