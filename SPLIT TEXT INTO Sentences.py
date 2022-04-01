# USE sent_tokenize() TO SPLIT TEXT INTO SENTENCES
# %%
import nltk
import pandas as pd
from pandas import DataFrame
# %%
nltk.download('punkt')
# %%
text = "I do not like green eggs and ham. I do not like them Sam-I-am."
a_list = nltk.tokenize.sent_tokenize(text)
# %%
print(a_list)
# %%
txt_df = DataFrame(a_list,columns = ['Text'])
# %%
txt_df.head()
# %%
