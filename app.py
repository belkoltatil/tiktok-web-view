import asyncio
import re
import aiohttp
from flask import Flask, render_template

app = Flask(__name__)

async def process_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()
            matches = re.findall(r'<pre style="word-wrap: break-word; white-space: pre-wrap;">(.*?)<\/pre>', data)
            if matches:
                return matches[0]
            return None

@app.route('/')
def index():
    base_url = 'https://hello-world-restless-lake-f4e4.devdesk.workers.dev'
    regex = r'\b\w+\:\/\/[^\s"]+'
    completed_links = []

    loop = asyncio.get_event_loop()
    tasks = []

    while True:
        response = requests.get(base_url)
        matches = re.findall(regex, response.text)

        if not matches:
            break

        for match in matches:
            completed_link = 'https://hello-world-dawn-sunset-aa71.devdesk.workers.dev/?url=' + match
            completed_links.append(completed_link)
            tasks.append(process_url(completed_link))

        results = loop.run_until_complete(asyncio.gather(*tasks))
        tasks = []

        for result in results:
            if result:
                completed_links.append(result)

        base_url = completed_links[-1] if completed_links else None

    return render_template('index.html', links=completed_links)

if __name__ == '__main__':
    app.run()
