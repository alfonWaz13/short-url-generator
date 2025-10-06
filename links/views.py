import pyshorteners
from django.shortcuts import render

from links.repositories.link_repository import LinkRepository
from links.use_cases.create_short_url import CreateShortURL


def index(request):
    if request.method == 'POST':
        long_url = request.POST['url_input']

        link_repository = LinkRepository()
        url_shortener = pyshorteners.Shortener()
        create_short_url_use_case = CreateShortURL(
            link_repository=link_repository,
            url_shortener=url_shortener
        )
        short_url = create_short_url_use_case.execute(long_url=long_url)
        return render(request, 'links/index.html', {'short_url': short_url})
    return render(request, 'links/index.html')