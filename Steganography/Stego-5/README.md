
First dump the file into a hex dump file, hd:

hd stego5.bmp | cut -f 2-20  -d ” ” | tr “\n” ” ” | sed ‘s/   / /g’ | sed ‘s/  / /g’ > hd

edit the file and take the 00003a2e off at the end…

There are streams of pixels, with 3 hex bytes representing the RBG. Sometimes they are a little off:

3e 3f 3f 4e 4f 4f 42 43 42 3b 3b 0a

0  1  1  0  1  1  0  1  0  1  1  0

The full bit stream reveals the password to be:  syn-ack-rst
