void setup() {


  Serial.begin(115200);
  myBot.wifiConnect(WIFISSID, PASSWORD);
  myBot.setTelegramToken(token);
  delay(1000);

  antares.setDebug(true);
  antares.wifiConnection(WIFISSID, PASSWORD);

  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input
  pinMode(buzzerPin, OUTPUT);
  pinMode(ledPin, OUTPUT);

}