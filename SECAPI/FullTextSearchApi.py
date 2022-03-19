# %%
from sec_api import FullTextSearchApi

fullTextSearchApi = FullTextSearchApi(api_key="346674ad7f8f0048de7a7ce19170e1b5e6a37de1ba608b56ed1a2a1a851ee916")
# %%
query = {
  "query": '"Russia"',
  "formTypes": ['N-CSR'],
  "startDate": '2021-01-01',
  "endDate": '2022-03-17',
}
# %%
filingsRussia = fullTextSearchApi.get_filings(query)
# %%
print(filingsRussia)
# %%
