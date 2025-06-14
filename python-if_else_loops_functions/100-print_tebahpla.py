#!/usr/bin/python3
print("{}".format("".join(
    chr(122 - i) if i % 2 == 0 else chr(90 - i) for i in range(26)
)), end="")


'''chr(122 - i) → starts from 'z' and goes down (lowercase)

chr(90 - i) → starts from 'Z' and goes down (uppercase)

if i % 2 == 0 → even indices get lowercase, odd get uppercase

''.join(...) → builds the final string without storing intermediate characters

end="" → avoids printing a newline'''
