const int ledPin = D1;
void setup() {
pinMode(1, OUTPUT); 
void loop() {
digitalWrite(1, LOW);
delay(1000); 
digitalWrite(1, HIGH);
delay(2000); 
}