from collections import Counter
import re

document = 'doc1.txt'

words = re.findall(r'\w+', open('./testdocs/' + document).read().lower())
counter = Counter(words)
most_common = counter.most_common(1)
print(most_common)
