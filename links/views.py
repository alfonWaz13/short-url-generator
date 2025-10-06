import pyshorteners
from django.shortcuts import render
from django.views import View

from links.repositories.link_repository import LinkRepository
from links.use_cases.create_short_url import CreateShortURL
from links.use_cases.get_all_urls import GetAllURLs


class IndexView(View):
    template_name = "links/index.html"

    link_repository = LinkRepository()
    url_shortener = pyshorteners.Shortener()
    create_short_url = CreateShortURL(
        link_repository=link_repository, url_shortener=url_shortener
    )
    get_all_urls = GetAllURLs(link_repository=link_repository)

    def get(self, request, *args, **kwargs):
        return render(
            request, self.template_name, {"all_urls": self.get_all_urls.execute()}
        )

    def post(self, request, *args, **kwargs):
        response_context = {}
        long_url = request.POST.get("url_input")

        if long_url:
            short_url = self.create_short_url.execute(long_url=long_url)
            response_context["short_url"] = short_url

        response_context["all_urls"] = self.get_all_urls.execute()
        return render(request, self.template_name, response_context)
