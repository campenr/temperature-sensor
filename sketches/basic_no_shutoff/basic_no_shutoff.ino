/* Basic Sketch to read temperature from a TMP35/36/37 temperature sensor (no shutoff signal). */

#define PIN_SENSOR A1
#define SOURCE_VOLTAGE 5000  // in millivolts

void setup() {
  Serial.begin(9600);
}

void loop() {
  printTemperature(readTemperature());
  delay(1000);
}

float readTemperature() {
  float voltage = analogRead(PIN_SENSOR) * (SOURCE_VOLTAGE / 1024.0);
  return (voltage - 500) / 10;
}

void printTemperature(float value) {
  // it is implied that the value is °C
  Serial.print(value, 1);
}
