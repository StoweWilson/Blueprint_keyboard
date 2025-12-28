## 🧩 Bill of Materials (BOM)

### Main Keyboard PCB

| Reference | Qty | Value / Part | Footprint | Price | Link | Datasheet |
|---------|-----|-------------|-----------|-------|------|-----------|
| U1 | 1 | ATmega32U4-A | TQFP-44 10×10 mm |  |  | http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-7766-8-bit-AVR-ATmega16U4-32U4_Datasheet.pdf |
| Y1 | 1 | 16 MHz Crystal | SMD 3225-4Pin |  |  | — |
| U2 | 1 | USB6B1 ESD Protector | SOIC-8 |  |  | http://www.st.com/content/ccc/resource/technical/document/datasheet/3e/ec/b2/54/b2/76/47/90/CD00001361.pdf |
| J1 | 1 | USB-C Receptacle (USB 2.0) | GCT USB4105 |  |  | https://www.usb.org/sites/default/files/documents/usb_type-c.zip |
| R1, R4 | 2 | 10 kΩ | 0805 |  |  | — |
| R2, R3 | 2 | 22 Ω | 0805 |  |  | — |
| R5, R6 | 2 | 5.1 kΩ | 0805 |  |  | — |
| C1, C2 | 2 | 22 pF | 0805 |  |  | — |
| C3 | 1 | 1 µF | 0805 |  |  | — |
| C4–C7 | 4 | 0.1 µF | 0805 |  |  | — |
| D1–D64 | 64 | Keyboard Diode | SOD-123 |  |  | — |
| SW1–SW64 | 64 | Gateron Low-Profile Hot-Swap Switch | PTH |  |  | — |
| SW65 | 1 | Reset Button | PTS647 SMD |  |  | — |
| J2–J5 | 4 | Adafruit 5413 Magnetic Connector | Custom |  |  | — |

---

### Keypad / Expansion PCB

| Reference | Qty | Value / Part | Footprint | Price | Link | Datasheet |
|---------|-----|-------------|-----------|-------|------|-----------|
| U1 | 1 | XIAO RP2040 SMD | Seeed 102010428 |  |  | — |
| U2 | 1 | PCF8575DBR I/O Expander | SSOP-24 |  |  | https://www.ti.com/lit/ds/symlink/pcf8575.pdf |
| R1–R4 | 4 | 10 kΩ | 0805 |  |  | — |
| R5, R6 | 2 | 5.1 kΩ | 0805 |  |  | — |
| D1–D21 | 21 | Keyboard Diode | SOD-123 |  |  | — |
| SW1–SW21 | 21 | Gateron Low-Profile Hot-Swap Switch | PTH |  |  | — |
| J1–J4 | 4 | Adafruit 5413 Magnetic Connector | Custom |  |  | — |

---

### Notes
- Prices and links are intentionally left blank for flexibility
- All passives are **0805** for easier assembly
- Diodes are **SOD-123**
- Switches are **low-profile hot-swap**
