# USE sent_tokenize() TO SPLIT TEXT INTO SENTENCES
import nltk
nltk.download('punkt')
text = "I do not like green eggs and ham. I do not like them Sam-I-am."
a_list = nltk.tokenize.sent_tokenize(text)
