from aiohttp.web import Response, Request, StreamResponse, HTTPMethodNotAllowed
from aiohttp.abc import AbstractView
from aiohttp import hdrs
from typing import Generator, Any
import json


class RestView(AbstractView):

    def __init__(self, request: Request) -> None:
        for item in request.app:
            setattr(self, item, request.app[item])
        self._request = request

    async def _iter(self) -> StreamResponse:
        if self.request.method not in hdrs.METH_ALL:
            self._raise_allowed_methods()
        if 'id' in self.request.match_info:
            method_name = "on_" + self.request.method.lower() + "_item"
        else:
            method_name = "on_" + self.request.method.lower() + "_collection"
        method = getattr(self, method_name, None)
        if not method:
            self._raise_allowed_methods()
        parameters = dict(**self.request.match_info, **self.request.query)
        if self.request.body_exists:
            parameters['body'] = json.loads(await self.request.text())
        body = json.dumps(await method(**parameters))
        resp = Response(body=body, content_type="application/json")
        return resp

    def __await__(self) -> Generator[Any, None, StreamResponse]:
        return self._iter().__await__()

    def _raise_allowed_methods(self) -> None:
        allowed_methods = {
            m for m in hdrs.METH_ALL if hasattr(self, m.lower())}
        raise HTTPMethodNotAllowed(self.request.method, allowed_methods)
