import pandas as pd
from pytrends.request import TrendReq
pytrends = TrendReq(hl='en-GB', tz=360)
pytrends.build_payload(kw_list=['machine learning'])



def getkeywords():
    keyword=input('What would you like your keywords to be?')
    keywords = pytrends.suggestions(keyword=keyword)
    df = pd.DataFrame(keywords)
    print(df)
    return df

def getrelatedqueries():
    from pytrends.request import TrendReq
    pytrend = TrendReq()
    kw_list=[]
    number_of_keywords=int(input('How many keywords do you want to search(there is a limit of 5)'))
    for i in range(0,number_of_keywords):
        keyword=input('Please type new keyword')
        kw_list.append(keyword)
        
    
    pytrend.build_payload(kw_list, cat=0, timeframe='now 7-d',geo='GB-ENG', gprop='youtube')
    # related queries
    related_queries = pytrend.related_queries()
    print(related_queries)



getkeywords()
getrelatedqueries()
