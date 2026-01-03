#include <Wire.h>
#include <Keyboard.h>

#define PCF_ADDR 0x20

#define ROWS 5
#define COLS 5

const uint8_t rowBits[ROWS] = {0, 1, 2, 3, 4};
const uint8_t colBits[COLS] = {5, 6, 7, 8, 9};

const uint8_t keymap[5][5] = {
  {KEY_F13,      'o',        't',        's',        'x'       }, 
  {KEY_F14,      KEY_NUM_LOCK, '/',      '*',        '-'       },  
  {KEY_F15,      '7',        '8',        '9',        '+'       },  
  {KEY_F16,      '4',        '5',        '6',        KEY_RETURN},  
  {KEY_F17,      '1',        '2',        '3',        '.'       }   
};

bool stable[ROWS][COLS];
bool lastStable[ROWS][COLS];
uint32_t lastChange[ROWS][COLS];

void pcfWrite(uint16_t v) {
  Wire.beginTransmission(PCF_ADDR);
  Wire.write(v & 0xFF);
  Wire.write(v >> 8);
  Wire.endTransmission();
}

uint16_t pcfRead() {
  Wire.requestFrom(PCF_ADDR, 2);
  uint16_t v = Wire.read();
  v |= Wire.read() << 8;
  return v;
}

void driveRow(int r) {
  uint16_t v = 0xFFFF;
  v &= ~(1 << rowBits[r]);
  pcfWrite(v);
}

bool readKey(int r, int c) {
  return !(pcfRead() & (1 << colBits[c]));
}

void setup() {
  Wire.begin();
  Wire.setClock(400000);
  pcfWrite(0xFFFF);
  Keyboard.begin();
  uint32_t t = millis();
  for (int r = 0; r < ROWS; r++)
    for (int c = 0; c < COLS; c++)
      stable[r][c] = lastStable[r][c] = false, lastChange[r][c] = t;
}

void loop() {
  static uint32_t lastScan = 0;
  uint32_t now = millis();
  if (now - lastScan < 2) return;
  lastScan = now;

  for (int r = 0; r < ROWS; r++) {
    driveRow(r);
    delayMicroseconds(250);

    for (int c = 0; c < COLS; c++) {
      bool raw = readKey(r, c);
      if (raw != stable[r][c]) {
        stable[r][c] = raw;
        lastChange[r][c] = now;
      }
      if (now - lastChange[r][c] > 10) {
        if (stable[r][c] != lastStable[r][c]) {
          lastStable[r][c] = stable[r][c];
          if (stable[r][c]) Keyboard.press(keymap[r][c]);
          else Keyboard.release(keymap[r][c]);
        }
      }
    }
    pcfWrite(0xFFFF);
  }
}