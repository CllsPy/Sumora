import requests
from bs4 import BeautifulSoup

class WebsiteContentExtractor:
    def __init__(self, url: str):
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
            }

    def fetch_website_contents(self):
        """
        Return the title and contents of the website at the given url;
        truncate to 2,000 characters as a sensible limit
        """
        response = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(response.content, "html.parser")
        title = soup.title.string if soup.title else "No title found"
        if soup.body:
            for irrelevant in soup.body(["script", "style", "img", "input"]):
                irrelevant.decompose()
            text = soup.body.get_text(separator="\n", strip=True)
        else:
            text = ""
        return (title + "\n\n" + text)[:2_000]

    def acess_and_extract(self):
        web_site_content = self.fetch_website_contents()
        print(web_site_content)

if __name__ == "__main__":
    extractor = WebsiteContentExtractor("https://fr.wikipedia.org/wiki/Batman")
    extractor.acess_and_extract()