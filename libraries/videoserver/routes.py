from aiohttp import web

import views
import settings


url_patterns = [
    web.view("/", views.IndexView),
    web.static(settings.STATIC_URL, settings.STATIC_ROOT)
]
