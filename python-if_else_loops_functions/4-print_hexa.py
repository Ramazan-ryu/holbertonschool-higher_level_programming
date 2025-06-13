#!/usr/bin/python3
for i in range(99):
    print("{} = 0x{:x}".format(i, i))


#  for i in range(99) — Loops from 0 to 98.
#  "{} = 0x{:x}".format(i, i) — Formats:
#  {} → decimal i
#  {:x} → hexadecimal i in lowercase
#  Only one print() is used inside the loop
