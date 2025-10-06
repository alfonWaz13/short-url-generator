import pyshorteners

from links.repositories.link_repository import LinkRepository


class CreateShortURL:
    def __init__(self, link_repository: LinkRepository, url_shortener: pyshorteners.Shortener) -> None:
        self.link_repository = link_repository
        self.url_shortener = url_shortener

    def execute(self, long_url: str) -> str:
        short_url = self.url_shortener.tinyurl.short(long_url)
        self.link_repository.add_link(long_url=long_url, short_url=short_url)
        return short_url
