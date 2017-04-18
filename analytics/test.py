from collections import defaultdict

dictionary = lambda: defaultdict(dictionary)
result = dictionary()

result['Text']['Ello']['Plus'] = 99

print(result['Text']['Ello'])