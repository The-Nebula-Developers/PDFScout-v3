# PDFScout API

PDFScout API allows you to search for PDFs, ebooks, and books using Google and Archive.org. It utilizes Google dorking techniques to scrape Google search results.

<h1>Endpoints</h1>

1. `/api/google`
    <br>Search for books or PDFs on Google.
    <br>Example: <code>pdf-scout.vercel.app/api/google?query=The Art Of War</code>

2. `/api/archive.org`
    <br>Search for books or PDFs on Archive.org.
    <br>Example: <code>pdf-scout.vercel.app/api/archive?query=48 Laws Of Power</code>

<h1>Usage</h1>

To use the API, simply make a GET request to the desired endpoint with the appropriate query parameter.

<h1>How it works</h1>

The PDFScout API performs searches on Google and Archive.org by utilizing specific search queries (Google dorking) to find relevant PDFs, ebooks, and books. It then scrapes the search results to provide you with the most relevant documents based on your query.

<h1>Disclaimer</h1>

Please note that the PDFScout API is for educational and informational purposes only. The developers do not endorse or encourage any illegal or unethical use of this API. Make sure to comply with all relevant laws and regulations when using this API.
