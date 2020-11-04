''' Web Scraping corono virus data to MS Excel

Approach: 

1) Request for a response from the webpage.
2) Parse and extract with the help of the BeautifulsSoup() class method and lxml module.
3) Download and export the data with pandas into Excel.'''

# Import required modules 
import requests 
import bs4 
import pandas as pd 


# Make requests from webpage 
url = 'https://www.worldometers.info/coronavirus/country/india/'
result = requests.get(url) 


# Creating soup object to scrape data from website
soup = bs4.BeautifulSoup(result.text,'lxml') 


# Searching div tags having maincounter-number class i
cases = soup.find_all('div' ,class_= 'maincounter-number') 

# List to store number of cases 
data = [] 

# Find the span and get data from it 
for i in cases: 
	span = i.find('span') 
	data.append(span.string) 

# Dispaly number of cases 
print(data) 

# Creating dataframe 
df = pd.DataFrame({"CoronaData": data}) 

# Naming the coloumns 
df.index = ['TotalCases', ' Deaths', 'Recovered'] 


# Exporing data into Excel 
df.to_csv('Corona_Data.csv')
