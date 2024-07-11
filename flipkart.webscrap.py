from io import BytesIO
from tkinter import Image
import pandas as pd
import requests
from bs4 import BeautifulSoup
Product_name = []
Prices = []
Description = []
Reviews = []
Images =[]


for i in range(1,15):
 url = "https://www.flipkart.com/search?q=best+mobile+phones+under+30000&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_3_25_na_na_ps&otracker1=AS_Query_OrganicAutoSuggest_3_25_na_na_ps&as-pos=3&as-type=RECENT&suggestionId=best+mobile+phones+under+30000&requestId=5008f1d5-38e2-4bdf-b06e-3cd6a2150646&as-searchtext=best%20mobile%20phones%20under%2030000"+ str(i)

 r= requests.get(url)
    #print(r)

 soup = BeautifulSoup(r.text,"lxml")
    #print(soup)

    # np = soup.find("a", class_="_9QVEpD").get("href")
    # cnp = "https://www.flipkart.com/"+ np 
    # print(cnp)

 box =  soup.find("div", class_= "DOjaWF gdgoEp") # KzDlHZ 
 
 # Send a request to the website
 response = requests.get(url)
 soup = BeautifulSoup(response.content, 'html.parser')

    # Find all image tags with the specified class
 image_tags = soup.find_all('img', {'class': 'DByuf4'})

    # Loop through the image tags and process images
 for i, img in enumerate(image_tags):
        img_url = img.get('src')
        if img_url:
            # Construct a valid image URL if it's not an absolute URL
            if not img_url.startswith('http'):
                img_url = 'https:' + img_url

            # Fetch the image
            img_response = requests.get(img_url)
            if img_response.status_code == 200:
                # Open the image in memory
                img_data = BytesIO(img_response.content)
                image = Image.open(img_data)
                
                # You can now work with the image in memory
                # For example, display the image
                image.show()

                # Or perform other operations with the image object
                print(f'Processed image {i+1}')

    # Note: Image.show() opens the image in the default image viewer
    # You can replace it with other image processing tasks as needed

 
 names = box.find_all("div", class_="KzDlHZ")
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

# df = pd.DataFrame({"Product Name":Product_name,"Prices": Prices, "Ratings":Reviews,"Description":Description})
# print(df)


# df.to_csv("F:/data science masters course/PYTHON/Web Scraping project/data/Flipkat_dataset.csv")

# image = box.find_all("img", class_="DByuf4")

# for i in image:
#    name= i.text 
#    Images.append(name)
   
# print(Images)   
  