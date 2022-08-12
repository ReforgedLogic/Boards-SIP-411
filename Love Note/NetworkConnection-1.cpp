#include "NetworkConnection.h"

NetworkConnection::NetworkConnection(){
}

void NetworkConnection::ConnectToNetwork(){
    Serial.println();
    Serial.println();
    Serial.print("Connecting to ");
    Serial.println(ssid);
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    Serial.println("");
    Serial.println("WiFi connected");
    Serial.println("IP address: ");
    Serial.println(WiFi.localIP());
}

void NetworkConnection::IFTTT_Request_Email(){
  WiFiClient IFTTTClient;  
  Serial.print("Connecting to: ");
  Serial.print(serv);
  while(!!!IFTTTClient.connect(serv, 80) && retries-- > 0){
     Serial.print(".");
  }
  if(!!!IFTTTClient.connected()){
    Serial.println("\n Connection Failed A");
    return;
  }
  Serial.print("\nRequest Made"); 
  Serial.print(email);
  IFTTTClient.print(String("GET ") + email + " HTTP/1.1\r\n" + 
  "Host: " + serv + "\r\n" + 
  "Connection: close\r\n\r\n");
  while(!!!IFTTTClient.available() && timeOut-- > 0){
    delay(100);
  }
  if(!!!IFTTTClient.connected()){
    Serial.println("\n Connection Failed B");
    return;
  }
  while(IFTTTClient.available()){
    Serial.write(IFTTTClient.read());
  }
  Serial.println("Closing Connection");
  IFTTTClient.stop();
}

void NetworkConnection::IFTTT_Request_Google(){
  WiFiClient IFTTTClient;  
  Serial.print("Connecting to: ");
  Serial.print(serv);
  while(!!!IFTTTClient.connect(serv, 80) && retries-- > 0){
     Serial.print(".");
  }
  if(!!!IFTTTClient.connected()){
    Serial.println("\n Connection Failed A");
    return;
  }
  Serial.print("\nRequest Made"); 
  Serial.print(google);
  IFTTTClient.print(String("GET ") + google + " HTTP/1.1\r\n" + 
  "Host: " + serv + "\r\n" + 
  "Connection: close\r\n\r\n");
  while(!!!IFTTTClient.available() && timeOut-- > 0){
    delay(100);
  }
  if(!!!IFTTTClient.connected()){
    Serial.println("\n Connection Failed B");
    return;
  }
  while(IFTTTClient.available()){
    Serial.write(IFTTTClient.read());
  }
  Serial.println("Closing Connection");
  IFTTTClient.stop();
}
  
void NetworkConnection::IFTTT_Request_Android(){
  WiFiClient IFTTTClient;  
  Serial.print("Connecting to: ");
  Serial.print(serv);
  while(!!!IFTTTClient.connect(serv, 80) && retries-- > 0){
     Serial.print(".");
  }
  if(!!!IFTTTClient.connected()){
    Serial.println("\n Connection Failed A");
    return;
  }
  Serial.print("\nRequest Made"); 
  Serial.print(android);
  IFTTTClient.print(String("GET ") + android + " HTTP/1.1\r\n" + 
  "Host: " + serv + "\r\n" + 
  "Connection: close\r\n\r\n");
  while(!!!IFTTTClient.available() && timeOut-- > 0){
    delay(100);
  }
  if(!!!IFTTTClient.connected()){
    Serial.println("\n Connection Failed B");
    return;
  }
  while(IFTTTClient.available()){
    Serial.write(IFTTTClient.read());
  }
  Serial.println("Closing Connection");
  IFTTTClient.stop();
}
