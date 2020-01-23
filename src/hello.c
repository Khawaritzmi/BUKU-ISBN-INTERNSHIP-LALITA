//Test Program Dasar Serial Monitor Menggunakan Arduino
// by Fungky King
void setup()
{
Serial.begin(9600);
}

void loop()
{
Serial.print("Hello World");
delay(2000);
}