#### stm32Mx 

install stm32mx and stm32cubeIde

#### flash mcu 

	brew install stlink

	brew install openocd

	(x) install gcc-arm-none-eabi-10.3-2021.10-mac


https://github.com/libopencm3/libopencm3

	brew install gcc-arm-none-eabi

#### list st link 
	ls /dev | grep st

Or
	st-info --probe

#### flash the device with st-flash

	st-flash --reset write blinkled.bin 0x8000000


configure openocd

	openocd -f /usr/local/share/openocd/scripts/interface/stlink-v2.cfg -f /usr/local/share/openocd/scripts/interface/stm32flx.cfg

gdb tools (optional)
https://github.com/ferrous-systems/embedded-trainings/blob/master/INSTALL.md


https://github.com/ntut-rf/mcu - stm32 wiki
