import pandas as pd
import requests
from bs4 import BeautifulSoup
Product_name = []
Prices = []
Description = []
Reviews = []


for i in range(1,18):
 url = "https://www.flipkart.com/search?q=best+mobile+phones+under+30000&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_3_25_na_na_ps&otracker1=AS_Query_OrganicAutoSuggest_3_25_na_na_ps&as-pos=3&as-type=RECENT&suggestionId=best+mobile+phones+under+30000&requestId=5008f1d5-38e2-4bdf-b06e-3cd6a2150646&as-searchtext=best%20mobile%20phones%20under%2030000"+ str(i)

 r= requests.get(url)
    #print(r)

 soup = BeautifulSoup(r.text,"lxml")
    #print(soup)


    # np = soup.find("a", class_="_9QVEpD").get("href")
    # cnp = "https://www.flipkart.com/"+ np 
    # print(cnp)

 box =  soup.find("div",class_= "DOjaWF gdgoEp") # KzDlHZ 
 
 names = box.find_all("div",class_= "KzDlHZ")
    #print(names)

 for i in names:
        name = i.text,
        Product_name.append(name)
        
    # print(Product_name)
    # print(len(Product_name))

 prices = box.find_all("div",class_ = "yRaY8j ZYYwLA")

 for i in prices:
        
        name = i.text 
        Prices.append(name)
        
    # print(Prices)

 Desc = box.find_all("ul", class_="G4BRas")    
    # G4BRas , _6NESgJ
 for i in Desc : 
    name = i.text
    Description.append(name)
#  print(Description)


 reviews   = box.find_all("div",class_ = "XQDdHH")

 for i in reviews:    

    name = i.text 
    Reviews.append(name)
        
    # print(Reviews)

df = pd.DataFrame({"Product Name":Product_name,"Prices": Prices, "Ratings":Reviews,"Description":Description})
print(df)


df.to_csv("F:/data science masters course/PYTHON/Web Scraping project/data/Flipkat_dataset.csv")