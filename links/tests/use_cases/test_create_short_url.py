from unittest.mock import MagicMock

from links.use_cases.create_short_url import CreateShortURL


class TestCreateShortURL:

    def test_url_is_generated_and_added_into_db(self) -> None:
        url_shortener = MagicMock()
        short_url = "short url"
        url_shortener.tinyurl.short.return_value = short_url
        link_repository = MagicMock()

        use_case = CreateShortURL(
            link_repository=link_repository, url_shortener=url_shortener
        )
        long_url = "long_url"
        use_case.execute(long_url=long_url)

        url_shortener.tinyurl.short.assert_called_once_with(long_url)
        link_repository.add_link.assert_called_once_with(
            long_url=long_url, short_url=short_url
        )
