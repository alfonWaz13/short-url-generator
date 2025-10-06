from links.models import Link


class LinkRepository:

    @classmethod
    def add_link(cls, long_url: str, short_url: str) -> None:
        Link.objects.create(original_url=long_url, short_code=short_url)

    @classmethod
    def get_all_urls(cls) -> list[Link]:
        return list(Link.objects.all().order_by("original_url"))

    @classmethod
    def get_existing_short_url(cls, original_url: str) -> Link | None:
        return Link.objects.get(original_url=original_url).short_code
