from collections import Counter

a = input("number of lines: ")
poem = []
vowels = ["a", "e", "i", "o", "u"]
TotalVowelsCount = 0
TotalConsonantsCount = 0
replaceWord = [' ', '.', ',', '?', '!']

# pobranie wierszy
for x in range(int(a)):
    line = input()
    poem.append(line)

for id1,el in enumerate(poem):

    # upraszczanie ciągu zapisanie wszystkich liter
    for x in replaceWord:
        poem[id1] = poem[id1].replace(x,"")
    lineWords = Counter(poem[id1])

    #zliczanie samogłosek i spółgłosek w wierszu
    vowelsCount = 0
    consonantsCount = 0
    for x in vowels:
        vowelsCount += lineWords[x]
    consonantsCount = len(poem[id1]) - vowelsCount

    TotalVowelsCount += vowelsCount
    TotalConsonantsCount += consonantsCount

    print(f"Vowels in line {id1+1}: {vowelsCount}")
    print(f"Consonants in line {id1+1}: {consonantsCount}")

print(f"Total vowels: {TotalVowelsCount}")
print(f"Total consonants: {TotalConsonantsCount}")
