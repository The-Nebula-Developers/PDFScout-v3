from flask import Flask, render_template, redirect, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def fetch_pdf_links_google(query):
    base_url = f"https://www.google.com/search?q={query}&num=3&as_filetype=pdf"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(base_url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        pdf_links = {i+1: a['href'] for i, a in enumerate(soup.find_all('a', href=True)) if '.pdf' in a['href']}
        pdf_links = {key: pdf_links[key] for key in list(pdf_links.keys())[:5]}
        return {"pdf_links": pdf_links}
    else:
        print(f"Error: Unable to fetch Google search results. Status code: {response.status}")
        return {"pdf_links": ["/"]}

def search_archive_org(book_title):
    base_url = "https://archive.org/advancedsearch.php"
    params = {
        'q': f'title:"{book_title}" AND mediatype:texts',
        'fl[]': 'identifier,title,creator',
        'output': 'json'
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        docs = data.get('response', {}).get('docs', [])

        results = []
        for doc in docs[:3]:  # Get up to three results
            identifier = doc.get('identifier', '')
            title = doc.get('title', '')
            creator = doc.get('creator', '')
            url = f"https://archive.org/details/{identifier}"

            results.append({
                'identifier': identifier,
                'title': title,
                'creator': creator,
                'url': url
            })

        return results
    else:
        return ["/"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api', methods=['POST','GET'])
def api():
    return "Please specify a valid endpoint to access the API."

@app.route('/api/google', methods=['GET','POST'])
def google():
    if request.method == 'POST':
        query = request.form['query']
        if query is None or "":
            return {"error": "Please provide a query parameter"}
        else:
            pdf_links = fetch_pdf_links_google(query)
            return pdf_links
    else:
        query = request.args.get('query')
        if query is None or "":
            return {"error": "Please provide a query parameter"}
        else:
            pdf_links = fetch_pdf_links_google(query)
            return pdf_links

@app.route('/api/archive', methods=['GET','POST'])
def archive():
    if request.method == 'POST':
        book_title = request.form['query']
        if book_title is None or "":
            return {"error": "Please provide a book_title parameter"}
        else:
            results = search_archive_org(book_title)
            return {"results": results}
    else:
        book_title = request.args.get('query')
        if book_title is None or "":
            return {"error": "Please provide a book_title parameter"}
        else:
            results = search_archive_org(book_title)
            return {"results": results}

if __name__ == '__main__':
    app.run(debug=True)
