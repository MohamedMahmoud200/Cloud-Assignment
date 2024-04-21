import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
# nltk.download('stopwords')
with open("paragraphs.txt","r") as f:
    fileContent=f.read()
text_tokens=word_tokenize(fileContent)
stop_words=stopwords.words('english')
textWithoutStopwords=[t for t in text_tokens if t not in stop_words]
for t in text_tokens:
    textWithoutStopwords.append(t.lower())
# print(textWithoutStopwords)
count = dict(Counter(textWithoutStopwords))
print(count)
