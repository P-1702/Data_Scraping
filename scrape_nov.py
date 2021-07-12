
import requests
import urllib.request
from bs4 import BeautifulSoup


def modify(image):
    new_image="https://books.toscrape.com"+ image[2:]
    return new_image

def find_rating():
     rating1=book.findAll("p",{"class":"star-rating One"})
     rating2=book.findAll("p",{"class":"star-rating Two"})
     rating3=book.findAll("p",{"class":"star-rating Three"})
     rating4=book.findAll("p",{"class":"star-rating Four"})
     rating5=book.findAll("p",{"class":"star-rating Five"})

     if(rating1):
        return "One-star"
     elif(rating2):
        return "Two-star"
     elif(rating3):
        return "Three-star"
     elif(rating4):
        return "Four-star"
     elif(rating5):
        return "Five-star"


count=0
for page_n in range(1,6,1):
    i=str(page_n)
    Data={}
    page = requests.get("https://books.toscrape.com/catalogue/page-"+i+".html")
    soup=BeautifulSoup(page.text,'html.parser')
    for book in soup.findAll(class_="col-xs-6 col-sm-4 col-md-3 col-lg-3"):
       count=count+1
       h3=book.find('h3')
       ic=book.find(class_="image_container")
       image=ic.find('img').get("src")
       m_image=modify(image)
       name=h3.get_text('title')
       rating=find_rating()
       url=ic.find('a').get('href')
       price=book.find(class_="price_color").get_text('class')
       Data={'Name':name, 'URL':url, 'Price':price, 'Rating':rating}
       urllib.request.urlretrieve(m_image,r"C:\Users\Dell\OneDrive\Pictures\Python_Images\img"+str(count)+r".jpg")
       print(Data)
       



    