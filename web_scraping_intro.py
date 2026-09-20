from bs4 import BeautifulSoup
import requests

url = 'https://www.scrapethissite.com/pages/forms/'

page = requests.get(url)
#returns a response object, like 200 ==> OK
#400 ==> bad request etc etc...

soup = BeautifulSoup(page.text, 'html')
#get the text from the page and parse it as html
#this will be the snapshot of the page at the instant the request
#was sent (since dynamic pages keep updating)

#print(soup.find('div'))
#soup.find will find the first reaponse 

#print(soup.find_all('div'))
#soup.find_all will find all the instances of the 'div' tag 
#and return a list 

#print(soup.find_all('div', class_ = 'col-md-12'))
#we can fine grain out find search even further by specifying 
#the class, note mention the tags in heirarchial order 

