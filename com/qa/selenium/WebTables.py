import urllib
import urllib.request
from bs4 import BeautifulSoup
import os

def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

playerdatasaved=""
soup = make_soup("http://www.basketball-reference.com/players/a/")
for record in soup.find_all('tr'):
    playerdata = ""
    for data in record.findAll('td'):
        playerdata = playerdata+","+data.text
        print(data.text)
        playerdatasaved = playerdatasaved + "\n" + playerdata[1:]

header = "Player,From,To,Pos,Ht,Wt,Birth Date,College"
file = open(os.path.expanduser("Basketball.csv"),"Wb")
file.write(bytes(header,encoding="ascii",errors='ignore'))
file.write(bytes(playerdatasaved, encoding="ascii",errors='ignore'))

print(playerdatasaved)



