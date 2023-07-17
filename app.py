from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    url = 'https://hello-world-restless-lake-f4e4.devdesk.workers.dev'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    hrefs = [a['href'] for a in soup.find_all('a', href=True)]

    videos = []
    for href in hrefs:
        completed_url = 'https://hello-world-dawn-sunset-aa71.devdesk.workers.dev/?url=' + href
        completed_response = requests.get(completed_url)
        completed_soup = BeautifulSoup(completed_response.text, 'html.parser')
        pre_tag = completed_soup.find('pre')
        if pre_tag:
            pre_text = pre_tag.get_text().strip()
            video_tag = f'<video controls><source src="{pre_text}" type="video/mp4"></video>'
            videos.append(video_tag)

    return render_template('index.html', videos=videos)

if __name__ == '__main__':
    app.run()
