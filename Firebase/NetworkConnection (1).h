#ifndef NetworkConnection_h
#define NetworkConnection_h
#include <WiFi.h>
#include "arduino.h"
#include "secrets.h"

class NetworkConnection{
  
  public:
  NetworkConnection();
  void ConnectToNetwork();
  const char* ssid = SECRET_SSID;
  const char* password = SECRET_PASS;
};

#endif
