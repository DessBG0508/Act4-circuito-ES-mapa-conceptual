
int valorLDR = 0;
int umbral = 400;   
void setup() {
  pinMode(13, OUTPUT);   
  pinMode(8, OUTPUT);    
  Serial.begin(9600);
}

void loop() {
  valorLDR = analogRead(A0);   
  Serial.println(valorLDR);   
  if (valorLDR > umbral) {     
    tone(8, 1000);              
    digitalWrite(13, HIGH);     
  } else {
    noTone(8);                
    digitalWrite(13, LOW);      
  }
  delay(100);
}