import base64 as b64
print("Enter the hexcode (default is")
hexCode = input("49276d206b696c6c696e6720796f757220627261696e206c" +
                "696b65206120706f69736f6e6f7573206d757368726f6f6d): ")

if not hexCode:
    hexCode = "49276d206b696c6c696e6720796f757220627261696e206c\
               696b65206120706f69736f6e6f7573206d757368726f6f6d"

byteCode = bytes.fromhex(hexCode)
print("Your code in bytes is: {0}".format(byteCode))

# b64Code = b64.b64encode(byteCode)

# print("Your hexcode in b64 is: {0}".format(b64Code))
