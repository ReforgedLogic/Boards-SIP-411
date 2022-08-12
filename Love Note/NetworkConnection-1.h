#ifndef NetworkConnection_h
#define NetworkConnection_h
#include <WiFi.h>
#include "arduino.h"
#include "secrets.h"

class NetworkConnection{
  
  public:
  NetworkConnection();
  void ConnectToNetwork();
  void IFTTT_Request_Email();
  void IFTTT_Request_Google();
  void IFTTT_Request_Android();
  const char* ssid = SECRET_SSID;
  const char* password = SECRET_PASS;
  const char* email = IFTTT_EMAIL;
  const char* google = IFTTT_GOOGLE;
  const char* android = IFTTT_ANDROID;
  const char* serv = IFTTT_SERVER;
  int retries = 5;
  int timeOut = 5 * 10;
};

#endif
