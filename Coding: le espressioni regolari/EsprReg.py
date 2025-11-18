import re
print(re.split(r'\W+', 'Words, words, words.'))
print(re.split(r'(\W+)', 'Words, words, words.'))

print(re.split(r'\W+', 'Words, words, words.', maxsplit=1))

print(re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE))
    