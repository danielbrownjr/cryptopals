from collections import Counter

plainText = input("Enter a code that you'd like to score" +
                  " (the default will be given as \"1b37373331363f78151b7f2" +
                  "b783431333d78397828372d363c78373e783a393b3736\"): ")
if not plainText:
    plainText = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"


byteText = bytes.fromhex(plainText).decode('utf-8')

plainList = []
for i in range(0, len(byteText)):
    if byteText[i] != " ":
        plainList.append(byteText[i])

plainCount = Counter(plainList)

for letter, count in plainCount.most_common(10):
    print("{0}: {1}".format(letter, count))

def heXOR(x, y):
    i = int(x, 16)
    j = int(y, 16)
    returnString = hex(i ^ j)
    return returnString

results = heXOR(plainText, "x")[2:]
print(results)

print(bytes.fromhex(results).decode('utf-8'))
