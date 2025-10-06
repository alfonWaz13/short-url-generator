from links.repositories.link_repository import LinkRepository


class GetExistingURL:
    def __init__(self, link_repository: LinkRepository):
        self.link_repository = link_repository

    def execute(self, original_url: str) -> str | None:
        return self.link_repository.get_existing_short_url(original_url)
