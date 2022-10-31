#%% 
from scholarly import scholarly
from codecs import ignore_errors

# Retrieve the author's data, fill-in, and print
# Get an iterator for the author results
#%%
search_query = scholarly.search_author('Xinde Zhang')
# Retrieve the first result from the iterator
first_author_result = next(search_query)
second_author_result = next(search_query)
scholarly.pprint(second_author_result)
#%%
# Retrieve all the details for the author
author = scholarly.fill(second_author_result )
scholarly.pprint(author)
#%%
# Take a closer look at the first publication
first_publication = author['publications'][0]
first_publication_filled = scholarly.fill(first_publication)
scholarly.pprint(first_publication_filled)

# Print the titles of the author's publications
publication_titles = [pub['bib']['title'] for pub in author['publications']]
print(publication_titles)

#%% Which papers cited that publication?
citations = [citation['bib']['title'] for citation in scholarly.citedby(first_publication_filled)]
print(citations)
# %% add \n
n_citations = ["{}\n".format(i) for i in citations]
#%% drop non-ascii characters
n_citations_asc = [i.encode('ascii', 'ignore').decode('ascii') for i in n_citations]
#%% write to disk
with open(r'./citations.txt', 'w') as fp:
    fp.writelines(n_citations_asc)

# %%
