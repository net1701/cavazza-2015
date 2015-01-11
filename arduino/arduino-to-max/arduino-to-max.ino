
const int NINPUTS = 2;
int pin_status[NINPUTS];

void setup() {
  Serial.begin(19200);
  for (int i=0; i<NINPUTS; ++i) {
    pinMode(i+2,INPUT); 
    pin_status[i] = 0;
  }
}

void loop() {
  for (int i=0; i<NINPUTS; ++i) {
    int x = digitalRead(i+2);
    if (x != pin_status[i]) {
      
      /*
      Serial.print("pin ");
      Serial.print(i+2);
      Serial.print(" ");
      Serial.print(x);
      Serial.print('\n');
      */
      
      if (x==1) Serial.write(i+2);
      pin_status[i] = x;
    }
  }  
  
  delay(10);
}

