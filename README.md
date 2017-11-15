# WaveShare-ePaper-Display
Cross Platform Raspberry Pi Display Driver For the WaveShare 4.3 Inch ePaper Display.  I have tested it on Linux platforms and it works using a USB to TTL serial converter.  After Looking online for a display library, I found most of them were ported over from Arduino and did not take advantage of some Python functions.  I wrote the library to be as simple as possible to interact with. For example:

if __name__=="__main__":
    display=Display()
    display.setComPort("/dev/ttyUSB1")
    display.connect()
    display.clear()
    display.print(0,0,'You can put any text here!')
    display.update()

# Hardware Needed

- Waveshare 4.3 inch display [Amazon](https://www.amazon.com/gp/product/B00VV5IMN0/ref=oh_aui_detailpage_o02_s02?ie=UTF8&psc=1)
- A USB to serial converter if using a computer [Amazon](https://www.amazon.com/gp/product/B014Y1IMNM/ref=oh_aui_detailpage_o07_s00?ie=UTF8&psc=1)

# Hardware Setup

- If you are using a USB converter it is connected as follows:
	- Waveshare Black ----> USB Converter GND
	- Waveshare Red ------> USB Converter DC
	- Waveshare Green ----> USB Converter TX
	- Waveshare White ----> USB Converter White
	
# Software Setup

- Modify the line `display.setComPort("/dev/ttyUSB1")` in EthDisplay.py to match your hardware
	- If you are using linux it is most likely `/dev/ttyUSB0` or `/dev/ttyUSB1`
	- if you are using an raspberry pi directly pluged into the GPIO header `/dev/ttyAMA0` (You may have to modify the kernal line so that ttyAMA0 is not a uart display terminal)
	- OSX should be `/dev/cu.usbserial` I do not own a mac so I cannot test this
	- Windows should be 'COM1' or COM#
- Run the display code `python WaveshareDisply.py` in your terminal for a demo

# Donations
	- If you enjoy this project tip some ETH `0xfE53DbDE58057B535b9df7220B854Ea26E5fA641` 
	- Let me know if you have any questions or if you made anything using this library!
