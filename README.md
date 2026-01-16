## What my project is 
My project is a 64% keyboard designed to resemble the layout of an Apple Magic Keyboard, with a few keys rearranged on either side of the PCB. There will be two magnetic pogo pins on either side, which will allow the keypad with identical pogo pins to connect, as well as allowing the keypad to be placed on either side of the keyboard, therefore making it modular. The case takes inspiration from the Worklouder XYZ Work Board.

## Why I made the project
I really like low-profile 60%–65% keyboards but had trouble finding ones that fit my needs. Learning that I had to put my own spin on the idea, I decided to take on the challenge of adding a keypad while keeping it modular, so I could still have the compactness of a 64% keyboard with the ability to have a numpad that does not make it bulky.

## Images

### Keyboard
<img width="858" height="657" alt="keyboard sch" src="https://github.com/user-attachments/assets/cf0c033d-5d6e-421a-b24f-0f9b38cdadd3" />
<img width="1116" height="400" alt="Screenshot 2026-01-01 at 11 01 54 PM" src="https://github.com/user-attachments/assets/3fee80d2-d682-486d-9bf8-d66ce15dba10" />


### Keypad
<img width="770" height="703" alt="keypad pcb" src="https://github.com/user-attachments/assets/108db54f-6382-46bc-ab69-63a811b1e695" />
<img width="1599" height="1004" alt="Screenshot 2026-01-01 at 11 03 55 PM" src="https://github.com/user-attachments/assets/47a25b63-e769-4775-af76-6c5aea5b665b" />


### Render
<img width="1671" height="1021" alt="Screenshot 2026-01-16 141933" src="https://github.com/user-attachments/assets/394bec12-2a40-4efb-bb15-da2f0abc8f7e" />
<img width="425" height="1186" alt="Screenshot 2026-01-16 141941" src="https://github.com/user-attachments/assets/ff86fc57-0d48-4d75-b83d-a7f4128c1a91" />

## BOM
### Keyboard

|Product name|Product Description|Qty|Price|Product Link|
|------------|-------------------|---|-----|------------|
|ATmega32U4-A|AVR AVR® ATmega Microcontroller IC 8-Bit 16MHz 32KB (16K x 16) FLASH 44-TQFP (10x10)|1|5.29|https://www.digikey.com/en/products/detail/microchip-technology/ATMEGA32U4-AU/1914602|
|16 MHz Crystal|CRYSTAL 3225 16MHZ 20PF 10PPM|1|.18|https://www.digikey.com/en/products/detail/eaton-electronics-division/E3X160201Y08/25656418?gclsrc=aw.ds&gad_source=1&gad_campaignid=20509818236&gbraid=0AAAAADrbLlgS94xmC2OHtv7KUQTO5uOa0&gclid=Cj0KCQiAx8PKBhD1ARIsAKsmGbeNFFstWFqMior3PH_CgvAHFOVgZvViWWTwkzizrjl1ohLOkbDwLqwaAlaHEALw_wcB|
|USB6B1 ESD Protector|TVS DIODE 5.25VWM 8SOIC|1|.69|https://www.digikey.com/en/products/detail/stmicroelectronics/USB6B1RL/654663|https://www.digikey.com/en/products/detail/amphenol-icc-fci-/10171746-00021LF/24366718?gclsrc=aw.ds&gad_source=1&gad_campaignid=20504594076&gbraid=0AAAAADrbLliKa-isyfEEG1K0mhQ-IdK9f&gclid=Cj0KCQiAx8PKBhD1ARIsAKsmGbfS4QL507NDol1-6Cdh5rUTj5M5hC5s0NrW_j3S6W67Z4K-qavOG4UaAp8YEALw_wcB|
|USB-C Receptacle (USB 2.0)|USB C RECEPTACLE R/A SMT 16P G/F|1|.72|https://www.digikey.com/en/products/detail/amphenol-icc-fci-/10171746-00021LF/24366718?gclsrc=aw.ds&gad_source=1&gad_campaignid=20504594076&gbraid=0AAAAADrbLliKa-isyfEEG1K0mhQ-IdK9f&gclid=Cj0KCQiAx8PKBhD1ARIsAKsmGbfS4QL507NDol1-6Cdh5rUTj5M5hC5s0NrW_j3S6W67Z4K-qavOG4UaAp8YEALw_wcB|
|10 kΩ|RES 10 OHM 1% 1/8W 0805|2|.11|https://www.digikey.com/en/products/detail/yageo/RC0805FR-1310RL/13694343?gclsrc=aw.ds&gad_source=1&gad_campaignid=17335707486&gbraid=0AAAAADrbLlj7rEgZ30rWPo_IyYLBKIC1T&gclid=Cj0KCQiAx8PKBhD1ARIsAKsmGbe2BlRAZ_fbKZ1YBvA79CHduwhXdcr3Sd3RQTWvr3wtoWWFxpEhsnEaAhrXEALw_wcB|
|22 Ω|RES 22 OHM 1% 1/8W 0805|2|.11|https://www.digikey.com/en/products/detail/yageo/RC0805FR-1322RL/13694339?gclsrc=aw.ds&gad_source=1&gad_campaignid=17335707486&gbraid=0AAAAADrbLlj7rEgZ30rWPo_IyYLBKIC1T&gclid=Cj0KCQiAx8PKBhD1ARIsAKsmGbfZP3-md_kWXjVo2urg73f88iKE2tR9Xip3xlEVRXTp1bbZVnmvqCgaAlWkEALw_wcB|
|5.1 kΩ|RES 5.1K OHM 5% 1/8W 0805|2|.10|https://www.digikey.com/en/products/detail/yageo/RC0805JR-075K1L/728338|
|22 pF|22 pF ±5% 50V Ceramic Capacitor C0G, NP0 0603 (1608 Metric)|2|.12|https://www.digikey.com/en/products/detail/kemet/C0603C220J5GACTU/411055|
|1 µF|CAP CER 1UF 6.3V X5R 0402|1|.08|https://www.digikey.com/en/products/detail/samsung-electro-mechanics/CL05A104KA5NNNC/3886701|
|.1uF|0.1 µF ±10% 25V Ceramic Capacitor X5R 0402 (1005 Metric)|4|.08|https://www.digikey.com/en/products/detail/samsung-electro-mechanics/CL05A104KA5NNNC/3886701|
|Diode|DIODE STANDARD 100V 150MA SOD123|64|.11|https://www.digikey.com/en/products/detail/diodes-incorporated/1N4148W-7-F/814371|
|Reset Button|SWITCH TACTILE SPST-NO 0.05A 12V|1|.41|https://www.digikey.ca/en/products/detail/c-k/Y97KT23B2NAFP/9649861|
|Adafruit 5413 Magnetic Connector|four 0.1" spaced contact pogo pins and a right angl|4|2.13|https://www.aliexpress.us/p/shoppingcart/index.html?spm=a2g0o.detail.0.0.2397nvtbnvtbTw|

### Keypad
|Product name|Product Description|Qty|Price|Product Link|
|------------|-------------------|---|-----|------------|
|XIAO RP2040 SMD|XIAO RP2040 SMD|1|4.68|https://www.digikey.com/en/products/detail/seeed-technology-co-ltd/102010428/14672129?gclsrc=aw.ds&gad_source=1&gad_campaignid=20243136172&gbraid=0AAAAADrbLlj-cx_AB7IYmSUrHfcZ3IQLC&gclid=Cj0KCQiAx8PKBhD1ARIsAKsmGbcn_ZEg4zv6ObEisLv_b6IgijRfvJiZc21Bz6JM8BaIT7ggCM4oFr8aAoSUEALw_wcB|
|PCF8575DBR I/O Expander|IC XPNDR 400KHZ I2C SMBUS 24SSOP|1|3.58|https://www.digikey.com/en/products/detail/texas-instruments/PCF8575DBR/754551|
|10 kΩ|RES 10 OHM 1% 1/8W 0805|4|.11|https://www.digikey.com/en/products/detail/yageo/RC0805FR-1310RL/13694343?gclsrc=aw.ds&gad_source=1&gad_campaignid=17335707486&gbraid=0AAAAADrbLlj7rEgZ30rWPo_IyYLBKIC1T&gclid=Cj0KCQiAx8PKBhD1ARIsAKsmGbe2BlRAZ_fbKZ1YBvA79CHduwhXdcr3Sd3RQTWvr3wtoWWFxpEhsnEaAhrXEALw_wcB|
|5.1 kΩ|RES 5.1K OHM 5% 1/8W 0805|2|.10|https://www.digikey.com/en/products/detail/yageo/RC0805JR-075K1L/728338|
|Diode|DIODE STANDARD 100V 150MA SOD123|21|.11|https://www.digikey.com/en/products/detail/diodes-incorporated/1N4148W-7-F/814371|
|Adafruit 5413 Magnetic Connector|four 0.1" spaced contact pogo pins and a right angl|4|2.13|https://www.aliexpress.us/p/shoppingcart/index.html?spm=a2g0o.detail.0.0.2397nvtbnvtbTw|


### Notes
- Shipping is not included in any of the prices.
- PCB with shippiing is $59.04 Qty of 5 each can't change.
- I will pay for the keyboard switches with my own money.
