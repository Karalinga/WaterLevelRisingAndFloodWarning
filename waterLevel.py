import requests
import html
from bs4 import BeautifulSoup
import ntplib
from time import ctime
highLevel = False 
infile = open("wollLines.txt","r")
lines = infile.readlines()
previousAvg = float(str(lines[-1:])[2:6])
#print(previousAvg)
infile.close()
c = ntplib.NTPClient()
totalHeight = 0.0
response = c.request('au.pool.ntp.org', version=3)
ctime(response.tx_time)
url = "https://www.waterwaysguide.org.au/river-levels"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36','Cache-Control': 'no-cache'}
r = requests.get(url, headers = headers)
#print(html.unescape(r.text))
outFile = open('wollLines.txt','a')
soup = BeautifulSoup(html.unescape(r.text))
list1 = soup.findAll('td')
#print(list1)
outFile.write("Loading heights...\n")
outFile.write("Current Time: "+ctime(response.tx_time)+"\n")
for td in list1:
	something = td.findAll("span")
	#print(something)
	for i in something:
		
		if "Wollondilly" in str(i):
			for j in something:
				#print("sasa")
				if "level-latest" in str(j):

					outFile.write(str(j)[40:44]+"\n")
					totalHeight  += float(str(j)[40:44])
					if(float(str(j)[40:44])>1):
						print("Water level is over 1m")
					#print(str(j)[40:44])
average  = totalHeight/4;
outFile.write(str(average)+"\n")
if previousAvg<average+5:
	print("Water level is rising")



# for i in inFile:
# 	if("Wollondilly" in i):
# 		outFile.write(i)
# 		print(i)
