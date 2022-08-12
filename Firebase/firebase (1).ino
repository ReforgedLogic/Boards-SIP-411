#include "NetworkConnection.h"
#include <ArduinoJson.h>
#include <IOXhop_FirebaseESP32.h>
#include <IOXhop_FirebaseStream.h>
#include <M5StickCPlus.h>
#define LED_BUILTIN 10

String fireStatus;
NetworkConnection NWC;


void setup() {
  Formatting();
  NWC.ConnectToNetwork();
  FirebaseConnectSetup();
}

void loop() {
  LED_Controls();
}

void FirebaseConnectSetup(){
  pinMode(LED_BUILTIN, OUTPUT);
  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTHERIZATION);
  Firebase.setString("LED_STATUS", "OFF");
}

void LED_Controls(){
  fireStatus = Firebase.getString("LED_STATUS");

  if(fireStatus == "OFF"){
    Serial.println("LED OFF");
    M5.Lcd.setCursor(20,20);
    M5.Lcd.print("OFF ");
    digitalWrite(LED_BUILTIN, HIGH);
  }
  else if(fireStatus == "ON"){
    Serial.println("LED ON");
    M5.Lcd.setCursor(20,20);
    M5.Lcd.print("ON  ");
    digitalWrite(LED_BUILTIN, LOW);
  }
  else{
    Serial.println("LED LOGIC ERR.");
    M5.Lcd.setCursor(20,20);
    M5.Lcd.print("ERR.");
  }
}

void Formatting(){
  Serial.begin(115200);
  delay(100);
  M5.begin();
  M5.Lcd.fillScreen(TFT_NAVY);
  M5.Lcd.setRotation(1);
  M5.Lcd.setCursor(20,20);
  M5.Lcd.setTextSize(5);
  M5.Lcd.setTextColor(WHITE, TFT_NAVY);
}
