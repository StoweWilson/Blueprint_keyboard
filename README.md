## 🧩 Bill of Materials (BOM)

### Main Keyboard PCB

| Reference | Qty | Value / Part | Footprint | Price Total | Link | Datasheet |
|---------|-----|-------------|-----------|-------|------|-----------|
| U1 | 1 | ATmega32U4-A | TQFP-44 10×10 mm |$5.29| https://www.microchip.com/en-us/product/atmega32u4 | http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-7766-8-bit-AVR-ATmega16U4-32U4_Datasheet.pdf |
| Y1 | 1 | 16 MHz Crystal | SMD 3225-4Pin | $.18 | https://www.digikey.com/en/products/detail/eaton-electronics-division/E3X160201Y08/25656418?gclsrc=aw.ds&gad_source=1&gad_campaignid=20509818236&gbraid=0AAAAADrbLlgS94xmC2OHtv7KUQTO5uOa0&gclid=Cj0KCQiAx8PKBhD1ARIsAKsmGbeNFFstWFqMior3PH_CgvAHFOVgZvViWWTwkzizrjl1ohLOkbDwLqwaAlaHEALw_wcB | — |
| U2 | 1 | USB6B1 ESD Protector | SOIC-8 |  |  | http://www.st.com/content/ccc/resource/technical/document/datasheet/3e/ec/b2/54/b2/76/47/90/CD00001361.pdf |
| J1 | 1 | USB-C Receptacle (USB 2.0) | GCT USB4105 | $.72|  https://www.digikey.com/en/products/detail/amphenol-icc-fci-/10171746-00021LF/24366718?gclsrc=aw.ds&gad_source=1&gad_campaignid=20504594076&gbraid=0AAAAADrbLliKa-isyfEEG1K0mhQ-IdK9f&gclid=Cj0KCQiAx8PKBhD1ARIsAKsmGbfS4QL507NDol1-6Cdh5rUTj5M5hC5s0NrW_j3S6W67Z4K-qavOG4UaAp8YEALw_wcB| https://www.usb.org/sites/default/files/documents/usb_type-c.zip |
| R1, R4 | 2 | 10 kΩ | 0805 |$.22|https://www.digikey.com/en/products/detail/yageo/RC0805FR-1310RL/13694343?gclsrc=aw.ds&gad_source=1&gad_campaignid=17335707486&gbraid=0AAAAADrbLlj7rEgZ30rWPo_IyYLBKIC1T&gclid=Cj0KCQiAx8PKBhD1ARIsAKsmGbe2BlRAZ_fbKZ1YBvA79CHduwhXdcr3Sd3RQTWvr3wtoWWFxpEhsnEaAhrXEALw_wcB| — |
| R2, R3 | 2 | 22 Ω | 0805 |$.22|https://www.digikey.com/en/products/detail/yageo/RC0805FR-1322RL/13694339?gclsrc=aw.ds&gad_source=1&gad_campaignid=17335707486&gbraid=0AAAAADrbLlj7rEgZ30rWPo_IyYLBKIC1T&gclid=Cj0KCQiAx8PKBhD1ARIsAKsmGbfZP3-md_kWXjVo2urg73f88iKE2tR9Xip3xlEVRXTp1bbZVnmvqCgaAlWkEALw_wcB| — |
| R5, R6 | 2 | 5.1 kΩ | 0805 |$.20|https://www.digikey.com/en/products/detail/yageo/RC0805JR-075K1L/728338| — |
| C1, C2 | 2 | 22 pF | 0805 |$.50|https://www.mouser.com/ProductDetail/KEMET/C0805C220J4GACAUTO?qs=MyNHzdoqoQJPr3F6isUymA%3D%3D| — |
| C3 | 1 | 1 µF | 0805 |$.70|https://www.mouser.com/ProductDetail/KYOCERA-AVX/KAF21KR71H105JU?qs=9vOqFld9vZWh8YVe5AsImg%3D%3D| — |
| C4–C7 | 4 | 0.1 µF | 0805 |$.16|https://www.digikey.com/en/products/detail/kemet/C0805C104K5RACTU/411169| — |
| D1–D64 | 64 | Keyboard Diode | SOD-123 |$2.37|https://www.digikey.com/en/products/detail/diodes-incorporated/1N4148W-7-F/815280?gclsrc=aw.ds&gad_source=1&gad_campaignid=20228387720&gbraid=0AAAAADrbLlgypAje0IPavXjgqFPx6XVld&gclid=Cj0KCQiAx8PKBhD1ARIsAKsmGbevNIc3pz5DCNokEEO_8CvM73vlO7yoCVwzxSf4ZXIzwrOgU6EtQNMaAnAVEALw_wcB| — |
| SW1–SW64 | 64 | Gateron Low-Profile Hot-Swap Switch | PTH |I can pay|  | — |
| SW65 | 1 | Reset Button | PTS647 SMD |$.21|https://www.digikey.com/en/products/detail/same-sky-formerly-cui-devices-/TS18-5-17-SL-160-SMT-TR/16590911?gclsrc=aw.ds&gad_source=1&gad_campaignid=20243136172&gbraid=0AAAAADrbLlj-cx_AB7IYmSUrHfcZ3IQLC&gclid=Cj0KCQiAx8PKBhD1ARIsAKsmGbfI-z-H6oBziXrPcqtyQUk9HacCuEkQtOFEPs540QdjCIGjgg51T7QaAr-XEALw_wcB| — |
| J2–J5 | 4 | Adafruit 5413 Magnetic Connector | Custom |$6.50|https://www.adafruit.com/product/5358| — |

---

### Keypad / Expansion PCB

| Reference | Qty | Value / Part | Footprint | Price | Link | Datasheet |
|---------|-----|-------------|-----------|-------|------|-----------|
| U1 | 1 | XIAO RP2040 SMD | Seeed 102010428 |$4.68|https://www.digikey.com/en/products/detail/seeed-technology-co-ltd/102010428/14672129?gclsrc=aw.ds&gad_source=1&gad_campaignid=20243136172&gbraid=0AAAAADrbLlj-cx_AB7IYmSUrHfcZ3IQLC&gclid=Cj0KCQiAx8PKBhD1ARIsAKsmGbcn_ZEg4zv6ObEisLv_b6IgijRfvJiZc21Bz6JM8BaIT7ggCM4oFr8aAoSUEALw_wcB| — |
| U2 | 1 | PCF8575DBR I/O Expander | SSOP-24 |$3.58|https://www.digikey.com/en/products/detail/texas-instruments/PCF8575DBR/754551| https://www.ti.com/lit/ds/symlink/pcf8575.pdf |
| R1–R4 | 4 | 10 kΩ | 0805 |$.44|https://www.digikey.com/en/products/detail/yageo/RC0805FR-1310RL/13694343?gclsrc=aw.ds&gad_source=1&gad_campaignid=17335707486&gbraid=0AAAAADrbLlj7rEgZ30rWPo_IyYLBKIC1T&gclid=Cj0KCQiAx8PKBhD1ARIsAKsmGbe2BlRAZ_fbKZ1YBvA79CHduwhXdcr3Sd3RQTWvr3wtoWWFxpEhsnEaAhrXEALw_wcB| — |
| R5, R6 | 2 | 5.1 kΩ | 0805 |$.20|https://www.digikey.com/en/products/detail/yageo/RC0805JR-075K1L/728338| — |
| D1–D21 | 21 | Keyboard Diode | SOD-123 |$.78|https://www.digikey.com/en/products/detail/diodes-incorporated/1N4148W-7-F/815280?gclsrc=aw.ds&gad_source=1&gad_campaignid=20228387720&gbraid=0AAAAADrbLlgypAje0IPavXjgqFPx6XVld&gclid=Cj0KCQiAx8PKBhD1ARIsAKsmGbevNIc3pz5DCNokEEO_8CvM73vlO7yoCVwzxSf4ZXIzwrOgU6EtQNMaAnAVEALw_wcB| — |
| SW1–SW21 | 21 | Gateron Low-Profile Hot-Swap Switch | PTH |  |  | — |
| J1–J4 | 4 | Adafruit 5413 Magnetic Connector | Custom |$6.50|https://www.adafruit.com/product/5358| — |

---

### Notes
- All passives are **0805** for easier assembly
- Diodes are **SOD-123**
- Switches are **low-profile hot-swap**
