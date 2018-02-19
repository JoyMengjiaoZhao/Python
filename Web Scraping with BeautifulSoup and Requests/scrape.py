from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_file:
    soup=BeautifulSoup(html_file,'lxml')

print(soup.prettify())
match1=soup.title
match2=soup.title.text
match3=soup.div #The first div on the page
match4=soup.find('div',class_='footer')
print(match1)
print(match2)
print(match3)
print(match4)

article=soup.find('div',class_='article')
print(article)

headline=article.h2.a.text
print(headline)
summary=article.p.text
print(summary)

for article in soup.find_all('div',class_='article'):
    headline=article.h2.a.text
    print(headline)
    summary=article.p.text
    print(summary)
    print()  #print '\n'
