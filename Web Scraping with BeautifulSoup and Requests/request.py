from bs4 import BeautifulSoup
import requests
import csv

source= requests.get('http://coreyms.com').text
soup=BeautifulSoup(source,'lxml')

#write to csv
csv_file=open('cms_scrape.csv','w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['headline','summary','video_link'])

#print(soup.prettify())

article=soup.find('article')
#print(article.prettify())  #the first article

#headline=article.h2.a.text
#print(headline)

#summary=article.find('div',class_='entry-content').p.text
#print(summary)

###Get ID
vid_src=article.find('iframe', class_='youtube-player')['src']
# access it like dictionary: add[]
print(vid_src)

vid_id=vid_src.split('/')
print(vid_id)
vid_id=vid_id[4]
print(vid_id)
vid_id=vid_id.split('?')
print(vid_id)
vid_id=vid_id[0]
print(vid_id)

yt_link='http://youtube.com/watch?v={}'.format(vid_id)
print(yt_link)
print()


for article in soup.find_all('article'): #make it as a list

    headline=article.h2.a.text
    print(headline)

    summary=article.find('div',class_='entry-content').p.text
    print(summary)

    try:##In case there is an exception or anything

        vid_src=article.find('iframe', class_='youtube-player')['src']

        vid_id=vid_src.split('/')[4]
        vid_id=vid_id.split('?')[0]

        yt_link='http://youtube.com/watch?v={}'.format(vid_id)

    except Exception as e:

        yt_link=None

    print(yt_link)

    print()

    csv_writer.writerow([headline,summary,yt_link])

csv_file.close()


