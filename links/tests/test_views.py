from unittest.mock import MagicMock

from links.views import IndexView


class IndexViewSpec(IndexView):
    link_repository = MagicMock()
    url_shortener = MagicMock()
    create_short_url = MagicMock()


class TestIndexView:
    def setup_method(self):
        self.view = IndexViewSpec()

    def test_if_no_input_url_provided_then_no_short_url_returned(self):
        request = MagicMock()
        request.POST.get.return_value = None

        response = self.view.post(request)

        assert "short_url" not in response

    def test_if_input_url_provided_then_short_url_returned(self):
        request = MagicMock()
        request.POST.get.return_value = "http://example.com"
        short_url_returned = "http://short.url/abc123"
        self.view.create_short_url.execute.return_value = short_url_returned

        response = self.view.post(request)

        assert short_url_returned.encode("utf-8") in response.content
