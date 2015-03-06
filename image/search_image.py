import urllib2
import urllib
import os.path
from BeautifulSoup import BeautifulSoup

def download(url):
  img = urllib.urlopen(url)
  localfile = open( os.path.basename(url), 'wb')
  localfile.write(img.read())
  img.close()
  localfile.close()

def clowler(url="http://moeimg.blog133.fc2.com/blog-entry-6272.html"):
  print url
  c = urllib2.urlopen(url)
  soup = BeautifulSoup(c.read())
  imgs = soup.findAll(['img'])
  print 'Image'
  for img in imgs:
    if img['src'].endswith(".jpg") or img['src'].endswith(".jpeg"):
      download(img['src'])
  
  links = soup.findAll(['a'])
  list = []
  print 'Link'
  for link in links:
    if 'blog-entry' in link['href']:
      print link['href']
      list.append(link['href'])
  print '--------------------------------------------------------------------'
  return list

def main():
  list = clowler()
  for l in list:
    clowler(l)