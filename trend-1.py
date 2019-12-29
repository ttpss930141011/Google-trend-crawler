import requests
import json
import re
import time
import random
from random import sample
Google_API = 'https://trends.google.com.tw/trends/api/dailytrends?hl=zh-TW&tz=-480&geo=TW&ns=15'


if __name__ == '__main__':
    count = 0 #google trend裡面有幾筆資料
    output = []
    a = requests.get(Google_API).text[6:]
    b = json.loads(a)
    
    for item in b['default']['trendingSearchesDays'][0]['trendingSearches']: #定位字典
        
        hot = item['title']['query'] #關鍵字
        #print('第'+str(count+1)+'個關鍵字 : '+hot)

        result = hot+'\n'
        
        for news in range(0,3):

            try:
                
                tit = b['default']['trendingSearchesDays'][0]['trendingSearches'][count]['articles'][news]['title']
                tit = re.sub(r'</?\w+[^>]*>','',tit) #標題
        
                href = b['default']['trendingSearchesDays'][0]['trendingSearches'][count]['articles'][news]['url'] #連結

                
                result = result +tit+href+'\n'
            
            except IndexError:
                pass
            #content = b['default']['trendingSearchesDays'][0]['trendingSearches'][count]['articles'][news]['snippet'] #內容
            #content = re.sub(r'</?\w+[^>]*>','',content) #去除標籤
            #content = content[0:-9]+'...' #去除&nbsp
            #print(content)
	#==============相關搜尋=================
        
        
        for keys in range(0,4):
            
            try:
                related = item['relatedQueries'][keys]['query'] #相關搜尋
                result = result +'\n相關搜尋 : '+related
                
            except IndexError:
                pass

        output.append(result)
        
            
        
        count += 1
    print(random.choice(output))
    
  
   