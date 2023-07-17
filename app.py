from flask import Flask, render_template
import re
import requests

app = Flask(__name__)

@app.route('/')
def index():
    url = 'https://hello-world-restless-lake-f4e4.devdesk.workers.dev'
    regex = r'\b\w+\:\/\/[^\s"]+'

    completed_links = []

    while True:
        response = requests.get(url)
        matches = re.findall(regex, response.text)
        
        if not matches:
            break

        for match in matches:
            completed_link = 'https://hello-world-dawn-sunset-aa71.devdesk.workers.dev/?url=' + match
            completed_links.append(completed_link)
            response = requests.get(completed_link)
            value = re.findall(r'<pre style="word-wrap: break-word; white-space: pre-wrap;">(.*?)<\/pre>', response.text)
            
            if value:
                completed_links.append(value[0])
            
            url = completed_link

    return render_template('index.html', links=completed_links)

if __name__ == '__main__':
    app.run()
