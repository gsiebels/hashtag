# I have imported tabulate to create a table that displays the data.
from tabulate import tabulate

# These are the variables that read the document inside the folder "test_docs" More TXT files can be added.
document = 'doc3.txt'
original_text = open('./test_docs/' + document).read()
text = open('./test_docs/' + document).read()

# This for loop removes the punctuation characters by replacing them for empty spaces and sets the full texts in lower case.
for character in '.-,";:\n':
    text = text.replace(character, ' ')
    text = text = text.replace('the', '')#.replace('and', ' ').replace('to', ' ').replace('ofaeiou', ' ')
text = text.lower()
# print(text)


word_list = text.split()
# print(word_list)

# This section counts the words. 
counter = {}
for word in word_list:
    counter[word] = counter.get(word, 0) + 1
# print(counter)

# This section store the words and the number of times they appear in the text, then arranges them.
word_freq = []
for key, value in counter.items():
    word_freq.append((value, key))
word_freq.sort(reverse=True)
# print(word_freq)
the_word = word_freq[0][1]
times = word_freq[1][0]

# This section matches the filters the most frequent word from the original text and display in a list all the sentences where the word appears.
sentences = [sentences + '.' for sentences in original_text.split('.') if the_word in sentences]
sentences = '\n'.join(map(str, sentences))

# This is the preparation for the layout on the table like spacing, header titles and the date displayed.
space = '\n' + '\n'
data = [(the_word, times, document, sentences)]
headers = ['WORD', 'TIMES', 'DOCUMENT', 'SENTENCE CONTAINING THE WORD']

print(space, 'TEXT', space, original_text, space, 'MOST COMMON WORD', space, tabulate(data, headers=headers))
