#!/usr/bin/env python3
from aiohttp import web
import aiohttp_jinja2
import settings
from routes import url_patterns


if __name__ == "__main__":
    app = web.Application()
    aiohttp_jinja2.setup(
        app,
        loader=aiohttp_jinja2.jinja2.FileSystemLoader(settings.TEMPLATE_ROOT)
    )
    app.router.add_routes(url_patterns)
    web.run_app(app)
