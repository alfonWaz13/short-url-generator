from links.repositories.link_repository import LinkRepository


class GetAllURLs:
    def __init__(self, link_repository: LinkRepository):
        self.link_repository = link_repository

    def execute(self) -> list[dict[str, str]]:
        all_urls = self.link_repository.get_all_urls()
        return [
            {
                "original_url": url.original_url,
                "short_url": url.short_code,
                "created_at": url.created_at,
            }
            for url in all_urls
        ]
