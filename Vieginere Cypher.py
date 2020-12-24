alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
punctuations = "!@#$%^&*()_+?|~`.,<>'  '"

def code_cipher(message, keyword):
    list = []
    index = 0
    for letter in message:
        if ((letter in alphabets) == True) and (index < len(keyword)):
            list.append(keyword[index])
            index += 1
        if (index == len(keyword)):
            index -= len(keyword)
        elif ((letter in alphabets) == False):
            list.append(letter)
    starter = []
    ender = []
    for code in list:
        if ((code in alphabets) == True):
            dexin = alphabets.index(code)
            starter.append(dexin)
        else:
            starter.append(code)
    for point in message:
        if ((point in alphabets) == True):
            xinde = alphabets.index(point)
            ender.append(xinde)
        else:
            ender.append(point)
    combined_index = []
    for number in range(0, len(ender)):
        if ((starter[number] in range(1000)) == True):
            first = starter[number]
            last = ender[number]
            added = first + last
            combined_index.append(added)
        elif ((starter[number] in range(1000)) == False):
            combined_index.append(starter[number])

    coded = []
    for number in combined_index:
        if ((number in range(1000)) == True) and number < 26:
            coded.append(alphabets[number])
        if ((number in range(1000)) ==  True) and number >= 26:
            modified = number - 26
            coded.append(alphabets[modified])
        if ((number in range(1000)) == False):
            coded.append(number)

    coded_sentence = "".join(coded)
    return coded_sentence

def decode_cipher(dmessage, keyword):
    dindex = []
    for letter in dmessage:
        if ((letter in alphabets) == True):
            dindex.append(alphabets.index(letter))
        else:
            dindex.append(letter)
    keycode = []
    dex = 0
    for letter in dmessage:
        if ((letter in alphabets) == True) and (dex < len(keyword)):
            keycode.append(keyword[dex])
            dex += 1
        if (dex == len(keyword)):
            dex -= len(keyword)
        if ((letter in alphabets) == False):
            keycode.append(letter)
    beginner = []
    for letter in keycode:
        if ((letter in alphabets) == True):
            beginner.append(alphabets.index(letter))
        else:
            beginner.append(letter)
    val = []
    for num in range(0, len(dindex)):
        if ((dindex[num] in range(1000)) == True) and (dindex[num] >= beginner[num]):
            dresult = dindex[num] - beginner[num]
            val.append(dresult)
        elif ((dindex[num] in range(1000)) == False):
            val.append(dindex[num])
        elif ((dindex[num] in range(1000)) == True) and (dindex[num] < beginner[num]):
            dresult = (dindex[num] - beginner[num]) + 26
            val.append(dresult)
    decoded = []
    for mun in val:
        if ((mun in range(1000)) == True):
            decoded.append(alphabets[mun])
        else:
            decoded.append(mun)
    decoded_sentence = "".join(decoded)
    return decoded_sentence

print(code_cipher("I dont want dummies to see my message", "keycodestood"))
print(decode_cipher("I nslv kdrl wiapsiq vc viw fm ahcwyis", "keycodestood"))