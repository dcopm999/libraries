import logging
import aiohttp_jinja2
from aiohttp import web, WSMsgType


logger = logging.getLogger(__name__)


class IndexView(web.View):
    @aiohttp_jinja2.template('index.html')
    async def get(self):
        return {"msg": "Hello"}


class OfferWS(web.View):
    
    async def get(self):
        ws = web.WebSocketResponse()
        await ws.prepare(self.request)

        async for msg in ws:
            if msg.type == WSMsgType.TEXT:
                if msg.data == 'close':
                    await ws.close()
                else:
                    await ws.send_str(msg.data + '/answer')
            elif msg.type == WSMsgType.ERROR:
                logger.info('ws connection closed with exception %s', ws.exception())
