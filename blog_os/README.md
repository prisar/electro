

os

	cargo bootimage


run qemu
	qemu-system-x86_64 -drive format=raw,file=target/x86_64-blog_os/debug/bootimage-blog_os.bin


The VGA text buffer is accessible via memory-mapped I/O to the address 0xb8000.
