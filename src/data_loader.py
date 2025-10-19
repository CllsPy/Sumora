from scraper import fetch_website_contents

class WebsiteContentExtractor:
    def __init__(self, url: str):
        self.url = url

    def acess_and_extract(self):
        web_site_content = fetch_website_contents(self.url)
        return web_site_content

