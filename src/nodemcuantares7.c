#include <AntaresESP8266HTTP.h>

const int trigPin = 2;  //D4
const int echoPin = 0;  //D3
const int ledPin = 4;  //D2
const int buzzerPin = 5;  //D1

// defines pins numbers
#define ACCESSKEY "xxx"
#define WIFISSID "xxx"
#define PASSWORD "xxx"

#define projectName "nama project"
#define deviceName "nama device"
AntaresESP8266HTTP antares(ACCESSKEY);

// defines variables
int duration;
int distance;
int safetyDistance;

void setup() {
  Serial.begin(115200);
  antares.setDebug(true);
  antares.wifiConnection(WIFISSID,PASSWORD);
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input
  pinMode(buzzerPin, OUTPUT);
  pinMode(ledPin, OUTPUT);

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

safetyDistance = distance;
if (safetyDistance <= 10){
  digitalWrite(buzzerPin, HIGH);
  digitalWrite(ledPin, HIGH);
}
else{
  digitalWrite(buzzerPin, LOW);
  digitalWrite(ledPin, LOW);
}


  antares.add("distance", distance);
  antares.add("duration", duration);
  antares.send(projectName, deviceName);

// Prints the distance on the Serial Monitor
Serial.print("Distance: ");
Serial.println(distance);
Serial.print("pulseIn ");
Serial.print(duration);
}
