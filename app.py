from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    url = "https://hello-world-restless-lake-f4e4.devdesk.workers.dev"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    href_values = [a['href'] for a in soup.find_all('a', href=True)]
    
    completed_links = []
    for href in href_values:
        completed_link = f"https://hello-world-dawn-sunset-aa71.devdesk.workers.dev/?url={href}"
        completed_links.append(completed_link)
        
    pre_texts = []
    for link in completed_links:
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')
        pre_text = soup.find('pre').text
        pre_texts.append(pre_text)
    
    return render_template('index.html', pre_texts=pre_texts)

if __name__ == '__main__':
    app.run()
