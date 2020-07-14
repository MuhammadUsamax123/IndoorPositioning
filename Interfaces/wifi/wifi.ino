#include <ESP8266WiFi.h>
 
const char* ssid = "Zong G4  pknet 03471819549";
const char* password = "link 12$.";
int ledPinb = 16;
int ledPinr = 5;
int buzzPin = 0;
WiFiServer server(80);
IPAddress staticIP(192, 168, 1, 143); //ESP static ip
IPAddress gateway(192, 168, 1, 1);   //IP Address of your WiFi Router (Gateway)
IPAddress subnet(255, 255, 255, 0);  //Subnet mask
IPAddress dns(192, 168, 1, 1);
void setup() {
  Serial.begin(115200);
  pinMode(ledPinb, OUTPUT);
  pinMode(ledPinr, OUTPUT);
  pinMode(buzzPin, OUTPUT);
  digitalWrite(ledPinb, HIGH);
  digitalWrite(ledPinr, HIGH);
  digitalWrite(buzzPin, HIGH);


  // Connect to WiFi network
      WiFi.begin(ssid, password);
      
      WiFi.disconnect();  //Prevent connecting to wifi based on previous configuration
  
       // DHCP Hostname (useful for finding device for static lease)
      WiFi.config(staticIP, subnet, gateway, dns);
      Serial.println("Connecting to ");
      Serial.print(ssid);
      WiFi.begin(ssid, password);
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
  
  if (request.indexOf("/LED=fire") != -1)  {
    blinkRedLED();
    client.println("HTTP/1.1 200 OK");
  }
  if (request.indexOf("/LED=flood") != -1)  {
    blinkBlueLED();
    client.println("HTTP/1.1 200 OK");
  }

  delay(1);
  Serial.println("Client disonnected");
  Serial.println("");
 
}

  void blinkBlueLED(){
  int i;
  for (i = 1; i < 11; i++){     
  digitalWrite(ledPinb, LOW);
  delay(1000);
  digitalWrite(ledPinb, HIGH);
  delay(1000);
  }
}

  void blinkRedLED(){
  int i;
  for (i = 1; i < 11; i++){
  digitalWrite(ledPinr, LOW);
  delay(1000);
  digitalWrite(ledPinr, HIGH);
  delay(1000);
  }
}

  void ringBell(){
  int i;
  for (i = 1; i < 11; i++){
  digitalWrite(buzzPin, LOW);
  delay(1000);
  digitalWrite(buzzPin, HIGH);
  delay(1000);
  }
}
