# # Before you run this code pleas intall tabulate: on the terminal go to this apps file and type 'pipenv tabulate' it whould take a few seconds to complete.

# from tabulate import tabulate

# document = 'doc1.txt'

# Text = open('./testdocs/' + document).read()
# exclude = 'the''and''to''of' 

# for character in '-,";:\n':
#     Text=Text.replace(character,'')
#     Text=Text.replace('the',' ')#.replace('and',' ').replace('to',' ')
# Text = Text.lower()
# # print(Text)

# word_list = Text.split()
# # print(word_list)

# d = {}
# for word in word_list:
#     d[word] = d.get(word, 0) + 1
# # print(d)

# word_freq = []
# for key, value in d.items():
#     word_freq.append((value,key))
# word_freq.sort(reverse=True)
# # print(word_freq[0])
# the_word = word_freq[0][1]
# times = word_freq[1][0]


# sentence = 'here goes the sentence'
# # def sentence(sentence, word_freq):
# #     res = [all(k in s for k in word_freq)]
# #     return [sentence[i] for i in range(0, len(res)) if res]


# data = [(the_word, times, document, sentence)]
# headers = ['WORD(#)', 'TIMES', 'DOCUMENT', 'SENTENCE CONTAINING THE WORD']
# print(tabulate(data, headers=headers))



from tabulate import tabulate
import re

document = 'doc1.txt'

original_text = open('./testdocs/' + document).read()
text = open('./testdocs/' + document).read()
exclude = 'the''and''to''of'

for character in '.-,";:\n':
    text = text.replace(character, ' ')
    text = text = text.replace('the', ' ')  # .replace('and',' ').replace('to',' ')
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


sentences = re.findall(r'([^.]*?begin[^.]*\.)', original_text)

print(sentences)


space = '\n' + '\n'
data = [(the_word, document, sentences, times)]
headers = ['WORD', 'DOCUMENT', 'SENTENCE CONTAINING THE WORD', 'TIMES ']

print(space, 'TEXT', space, original_text, space, 'MOST COMMON WORD', space, tabulate(data, headers=headers))

sentence = original_text.split('.')

# print(sentences)
