
#Date-13-2-23-Day-13
                    # -WEBSCRAPPING-

#importing requests and pandas and bs4(beautifulsoup)
import requests
import pandas as p
from bs4 import BeautifulSoup

responce=requests.get("https://www.flipkart.com/search?q=mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mobiles%7CMobiles&requestId=6e94b852-e006-40e1-b167-bbbbbf134cd2&as-searchtext=mob")
#print(responce)
# output=<Response [200]> so got permission from flipkart we can take the data
 #Now implementing parser
 #Parser means reader or scanner or convrter-it converts the data from one format to another

 #now flipkaet code written in html format so we should use html parser

soup=BeautifulSoup(responce.content,"html.parser")
#print(soup )

#First taking the names of mobile names

Mobilenames=soup.find_all("div",class_="_4rR01T")
name=[] #taking empty list for storing the data
#print(Mobilenames)

#i only need 20 mobiles

for i in Mobilenames[0:20]:
    d=i.get_text()
    name.append(d)
#print(name)
#We will get the structured data


#Now taking the prices of Mobiles
prices=soup.find_all("div",class_="_30jeq3 _1_WHN1")
price=[] #taking empty list for storing the data
#print(prices)

#i only need 20 moile prices

for i in prices[0:20]:
    d=i.get_text()
    price.append(d)
#print(price)



#Now taking the Mobile ratings

#Now taking the rating of Mobiles
ratings=soup.find_all("div",class_="_3LWZlK")
rating=[] #taking empty list for storing the data
#print(prices)

#i only need 20 moile ratings

for i in ratings[0:20]:
    d=i.get_text()
    rating.append(d)
#print(rating)


#Now Taking Mobile Images

#Now taking the images of Mobiles
Mobileimages=soup.find_all("img",class_="_396cs4")
image=[] #taking empty list for storing the data
#print(prices)

#i only need 20 moile images it will implement links

for i in Mobileimages[0:20]:
    d=i["src"]  #Image should get from src 
    image.append(d)
#print(image)



#Now taking the Mobile Links
Mobilelinks=soup.find_all("a",class_="_1fQZEK")
link=[] #taking empty list for storing the data
#print(prices)

#i only need 20 moile images it will implement links

for i in Mobilelinks[0:20]:
    d= "https://www.flipkart.com"+i["href"]  #adding WWW.flipkart.com for successful link
    link.append(d)
#print(link)


#Now Entering the Pandas

df=p.DataFrame()                #Dataframe means table it contains roes and colums
#p means pandas we imported pandas as p

#print(df)
#Output 0 coluns and 0 rows now we can store the data
#Columns: []
#Index: []


#Generting Columns Names

#name,price,rating,image,link we store our data separetely now we can use pandas and store the data in rows
df["Mobile_Names"]=name
df["Mobile_prices"]=price
df["Mobile_Ratings"]=rating
df["Mobile_Images"]=image
df["Mobile_Links"]=link
print(df)

#I got the data but i need in a separate file then
df.to_csv("Vardhan Mobiles_Data.csv")  #csv means a file format which separates the CSV=comma separated value
#File name=Vardhan Mobile_data extenssion .csv
#it will seen in XL sheet format
#Created separate file stored in New-D Febraury coaching









