from PIL import Image
from pwn import xor
im1 = Image.open('lemur.png')
im2 = Image.open('flag.png')

XOR = xor(im1.tobytes(),im2.tobytes())
im3 = Image.frombytes(im1.mode, im1.size, XOR)
im3.show()
