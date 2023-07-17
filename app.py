import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Retrieve href attribute values from the initial link
    initial_link = 'https://hello-world-restless-lake-f4e4.devdesk.workers.dev'
    response = requests.get(initial_link)
    soup = BeautifulSoup(response.text, 'html.parser')
    href_values = [a['href'] for a in soup.find_all('a', href=True)]

    # Process each href value
    video_sources = []
    for href in href_values:
        completed_link = f'https://hello-world-dawn-sunset-aa71.devdesk.workers.dev/?url={href}'
        completed_response = requests.get(completed_link)
        completed_soup = BeautifulSoup(completed_response.text, 'html.parser')
        pre_tag = completed_soup.find('pre')

        if pre_tag:
            text_inside_pre = pre_tag.text.strip()
            video_sources.append(text_inside_pre)

    return render_template('index.html', video_sources=video_sources)

if __name__ == '__main__':
    app.run()
