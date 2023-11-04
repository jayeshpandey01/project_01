# from bs4 import BeautifulSoup
# import requests

# url = 'https://www.chaingpt.org/' # Replace with your URL

# response = requests.get(url)

# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, 'html.parser')
#     print(soup.prettify()) # The HTML will be printed out here
# else:
#     print(f"Failed to retrieve webpage: {response.status_code}")

# for css
import requests
from bs4 import BeautifulSoup

url = 'https://www.chaingpt.org/' # Replace with your URL

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    for link in soup.find_all('link', rel='stylesheet'):
        css_url = link.get('href')
        css_response = requests.get(css_url)
        
        if css_response.status_code == 200:
            print(css_response.text)
        else:
            print(f"Failed to retrieve CSS from {css_url}")
else:
    print(f"Failed to retrieve webpage: {response.status_code}")