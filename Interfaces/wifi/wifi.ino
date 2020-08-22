#include <ESP8266WiFi.h>
const char* ssid[] = {"Router_2", "Router_3", "Router_4"};
const char* password[] = {"alpha_123", "beta_123", "gamma_123"};
int ledPinb = 16;
int ledPinr = 4;
int buzzPin = 0;
WiFiServer server(80);
void setup() {
  Serial.begin(65200);
  pinMode(buzzPin, OUTPUT);
  digitalWrite(ledPinb, HIGH);
  digitalWrite(ledPinr, HIGH);
  digitalWrite(buzzPin, HIGH);


  // Connect to WiFi network
      WiFi.begin(ssid, password);
      Serial.println("Connecting to ");
      Serial.print(ssid);
  pinMode(ledPinb, OUTPUT);
  pinMode(ledPinr, OUTPUT);
      WiFi.mode(WIFI_STA);
    while (WiFi.status() != WL_CONNECTED) {
      delay(5000);
      Serial.print(".");
  }

  
  
  // Start the server
  server.begin();
  Serial.println("Server started");
 
  // Print the IP address
  Serial.print("Use this URL to connect: ");
  Serial.print("http://");
  Serial.print(WiFi.localIP());
  Serial.println("/");
 
}
 
void loop() {
  // Check if a client has connected
  WiFiClient client = server.available();
  if (!client) {
    return;
  }
 
  // Wait until the client sends some data
  Serial.println("new client");
  while(!client.available()){
    delay(1);
  }
 
  // Read the first line of the request
  String request = client.readStringUntil('\r');
  Serial.println(request);
  client.flush();
  
  if (request.indexOf("/LED=Fire") != -1)  {
    blinkRedLED();
    client.println("HTTP/1.1 200 OK");
  }
  if (request.indexOf("/LED=Flood") != -1)  {
    blinkBlueLED();
    client.println("HTTP/1.1 200 OK");
  }
  if (request.indexOf("/LED=Call") != -1)  {
    ringBell();
    client.println("HTTP/1.1 200 OK");
  }
  delay(1);
  Serial.println("Client disonnected");
  Serial.println("");
 
}

  void blinkBlueLED(){
  int i;
  for (i = 1; i < 6; i++){     
  digitalWrite(ledPinb, LOW);
  delay(1000);
  digitalWrite(ledPinb, HIGH);
  delay(1000);
  }
}

  void blinkRedLED(){
  int i;
  for (i = 1; i < 6; i++){
  digitalWrite(ledPinr, LOW);
  delay(1000);
  digitalWrite(ledPinr, HIGH);
  delay(1000);
  }
}

  void ringBell(){
  int i;
  for (i = 1; i < 6; i++){
  digitalWrite(buzzPin, LOW);
  delay(1000);
  digitalWrite(buzzPin, HIGH);
  delay(1000);
  }
}
