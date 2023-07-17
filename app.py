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
            video_content = requests.get(pre_text).content

            video_filename = f'video_{len(videos)}.mp4'
            with open(video_filename, 'wb') as f:
                f.write(video_content)

            video_tag = f'<video controls><source src="{video_filename}" type="video/mp4"></video>'
            videos.append(video_tag)

    return render_template('index.html', videos=videos)

if __name__ == '__main__':
    app.run()
