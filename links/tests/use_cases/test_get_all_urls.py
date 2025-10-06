from unittest.mock import MagicMock

from links.models import Link
from links.use_cases.get_all_urls import GetAllURLs


class TestGetAllUrls:
    def test_get_all_urls_returns_all_urls(self) -> None:
        link_repository = MagicMock()
        urls = [
            Link(
                original_url="http://example.com/1",
                short_code="short1",
                created_at="created_at_1",
            ),
            Link(
                original_url="http://example.com/2",
                short_code="short2",
                created_at="created_at_2",
            ),
        ]
        link_repository.get_all_urls.return_value = urls

        use_case = GetAllURLs(link_repository=link_repository)
        result = use_case.execute()

        link_repository.get_all_urls.assert_called_once()
        assert result == [
            {
                "original_url": "http://example.com/1",
                "short_url": "short1",
                "created_at": "created_at_1",
            },
            {
                "original_url": "http://example.com/2",
                "short_url": "short2",
                "created_at": "created_at_2",
            },
        ]
