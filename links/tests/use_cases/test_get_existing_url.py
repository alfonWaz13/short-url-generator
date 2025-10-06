from unittest.mock import MagicMock

from links.use_cases.get_existing_url import GetExistingURL


class TestGetExistingURL:

    def test_get_existing_url_returns_expected_url(self):
        repository = MagicMock()
        repository.get_existing_short_url.return_value = "my_url"
        use_case = GetExistingURL(link_repository=repository)

        result = use_case.execute("my_original_url")

        assert result == "my_url"
