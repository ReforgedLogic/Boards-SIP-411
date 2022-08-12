#include <M5StickCPlus.h>
#include "NetworkConnection.h"

NetworkConnection NWC;


void FormattingSetup();
void checkBotton();

void setup() {
  FormattingSetup();
  NWC.ConnectToNetwork();
}

void loop() {
  M5.update();
  checkBotton();
}

void FormattingSetup(){
  Serial.begin(115200);
  delay(100);
  M5.begin();
  M5.Lcd.fillScreen(TFT_PURPLE);
  M5.Lcd.setRotation(1);
  M5.Lcd.setCursor(20,20);
  M5.Lcd.setTextSize(3);
  M5.Lcd.setTextColor(WHITE, TFT_PURPLE);
}

void checkBotton(){
  if(M5.BtnB.wasPressed()){
    M5.Lcd.setCursor(20,20);
    M5.Lcd.print("B Pressed");
    NWC.IFTTT_Request_Email();
    NWC.IFTTT_Request_Google();
  }
  else if(M5.BtnA.wasPressed()){
    M5.Lcd.setCursor(20,20);
    M5.Lcd.print("A Pressed");
    NWC.IFTTT_Request_Android();
  }
  else{
    //Serial.print("Non Pressed");
  }
}
