from tabulate import tabulate


document = 'doc1.txt'
original_text = open('./testdocs/' + document).read()
text = open('./testdocs/' + document).read()
exclude = 'the''and''to''of'

for character in '.-,";:\n':
    text = text.replace(character, ' ')
    text = text = text.replace('the', ' ').replace('and', ' ').replace('to', ' ').replace('of', ' ')
text = text.lower()
# print(text)

word_list = text.split()
# print(word_list)

d = {}
for word in word_list:
    d[word] = d.get(word, 0) + 1
# print(d)

word_freq = []
for key, value in d.items():
    word_freq.append((value, key))
word_freq.sort(reverse=True)
# print(word_freq[0])

the_word = word_freq[0][1]
times = word_freq[1][0]

sentences = [sentences + '.' for sentences in original_text.split('.') if the_word in sentences]

sentences = '\n'.join(map(str, sentences))

space = '\n' + '\n'
data = [(the_word, document, sentences)]
headers = ['WORD', 'DOCUMENT', 'SENTENCE CONTAINING THE WORD']

print(space, 'TEXT', space, original_text, space, 'MOST COMMON WORD', space, tabulate(data, headers=headers))

sentence = original_text.split('.')

