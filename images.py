import requests
from bs4 import BeautifulSoup
import pandas as pd
from IPython.display import display, HTML

Product_name = []
Prices = []
Description = []
Reviews = []
Images = []

for i in range(1, 12):
    # URL of the Flipkart page to scrape
    url = f"https://www.flipkart.com/search?q=best+mobile+phones+under+30000&page={i}"
    
    # Send a request to the website
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the main container for the products
    box = soup.find("div", class_="DOjaWF gdgoEp")
    if not box:
        continue
    
    # Scraping product names
    names = box.find_all("div", class_="KzDlHZ")
    for name in names:
        Product_name.append(name.text)
    
    # Scraping prices
    prices = box.find_all("div", class_="yRaY8j ZYYwLA")
    for price in prices:
        Prices.append(price.text)
    
    # Scraping descriptions
    descs = box.find_all("ul", class_="G4BRas")
    for desc in descs:
        Description.append(desc.text)
    
    # Scraping reviews
    reviews = box.find_all("div", class_="XQDdHH")
    for review in reviews:
        Reviews.append(review.text)
    
    # Scraping images
    image_tags = box.find_all('img', {'class': 'DByuf4'})
    for img in image_tags:
        img_url = img.get('src')
        alt_text = img.get('alt')
        if img_url:
            if not img_url.startswith('http'):
                img_url = 'https:' + img_url
            
            # Create HTML for displaying the image
            img_html = f'<img src="{img_url}" alt="{alt_text}" style="width:100px;height:auto;">'
            Images.append(img_html)

# Find the maximum length of the lists
max_length = max(len(Product_name), len(Prices), len(Description), len(Reviews), len(Images))

# Pad the lists to ensure they all have the same length
Images += [''] * (max_length - len(Images))
Product_name += [''] * (max_length - len(Product_name))
Prices += [''] * (max_length - len(Prices))
Description += [''] * (max_length - len(Description))
Reviews += [''] * (max_length - len(Reviews))


# Create a DataFrame from the collected data
data = {
    'Image': Images,
    'Product_Name': Product_name,
    'Price': Prices,
    'Description': Description,
    'Reviews': Reviews
    
}

df = pd.DataFrame(data)

# Display the DataFrame (in a Jupyter notebook or similar environment)
display(HTML(df.to_html(escape=False)))

# Optionally, save the DataFrame to a CSV file


