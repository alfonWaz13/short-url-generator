from unittest.mock import MagicMock

from django.test import SimpleTestCase

from links.views import IndexView


class TestIndexView(SimpleTestCase):

    def setUp(self):
        self.view = IndexView()
        self.view.url_shortener = MagicMock()
        self.view.link_repository = MagicMock()
        self.view.create_short_url = MagicMock()
        self.view.get_all_urls = MagicMock()
        self.view.get_existing_url = MagicMock()

    def test_no_short_url_returned_if_no_input_url_provided(self):
        request = MagicMock()
        request.POST.get.return_value = None
        self.view.get_all_urls.execute.return_value = []

        response_context = self.view.post(request)

        self.assertNotIn("short_url", response_context)

    def test_short_url_returned_if_input_url_provided(self):
        request = MagicMock()
        request.POST.get.return_value = "http://example.com"
        short_url_returned = "http://short.url/abc123"
        self.view.get_existing_url.execute.return_value = None
        self.view.create_short_url.execute.return_value = short_url_returned
        self.view.get_all_urls.execute.return_value = []

        response = self.view.post(request)

        assert short_url_returned.encode("utf-8") in response.content

    def test_new_url_is_created_with_post_request(self):
        request = MagicMock()
        request.POST.get.return_value = "http://new-url.com"
        self.view.get_existing_url.execute.return_value = None
        self.view.get_all_urls.execute.return_value = []

        self.view.post(request)

        self.view.create_short_url.execute.assert_called_once_with(
            long_url="http://new-url.com"
        )

    def test_no_new_url_is_added_if_url_already_exists(self):
        request = MagicMock()
        request.POST.get.return_value = "http://existing-url.com"
        self.view.get_existing_url.execute.return_value = "http://short.url/existing"
        self.view.get_all_urls.execute.return_value = []

        self.view.post(request)

        self.view.create_short_url.execute.assert_not_called()

    def test_all_urls_are_always_returned_in_context(self):
        request = MagicMock()
        request.POST.get.return_value = "http://some-url.com"
        expected_urls = [
            {
                "original_url": "http://some-url.com",
                "short_url": "http://short.url/some",
                "created_at": "2024-01-01",
            },
            {
                "original_url": "http://another-url.com",
                "short_url": "http://short.url/another",
                "created_at": "2024-01-02",
            },
        ]
        self.view.get_all_urls.execute.return_value = expected_urls

        response = self.view.post(request)

        assert expected_urls[0]["original_url"].encode("utf-8") in response.content
        assert expected_urls[0]["short_url"].encode("utf-8") in response.content
        assert expected_urls[1]["original_url"].encode("utf-8") in response.content
        assert expected_urls[1]["short_url"].encode("utf-8") in response.content
