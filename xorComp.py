inputBufferOne = input("Enter Buffer 1 (default = c0111001f010100061a024b53535009181c)")

if not inputBufferOne:
    inputBufferOne = "1c0111001f010100061a024b53535009181c"

inputBufferTwo = input("Enter Buffer 2 (default = 686974207468652062756c6c277320657965)")

if not inputBufferTwo:
    inputBufferTwo = "686974207468652062756c6c277320657965"

def heXOR(x, y):
    i = int(x, 16)
    j = int(y, 16)
    returnString = str(hex(i ^ j))[2:]
    return returnString

print("XOR between buffer one and buffer two")
print("is {0}".format(heXOR(inputBufferOne, inputBufferTwo)))
