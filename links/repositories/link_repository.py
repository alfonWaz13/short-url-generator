from links.models import Link


class LinkRepository:

    @classmethod
    def add_link(cls, long_url: str, short_url: str) -> None:
        Link.objects.create(original_url=long_url, short_code=short_url)
