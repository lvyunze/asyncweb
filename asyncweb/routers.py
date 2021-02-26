from aiohttp.web import RouteDef, AbstractRouteDef
from aiohttp.web_routedef import _Deco, _HandlerType
from aiohttp import hdrs
from typing import Any, Sequence, overload, Iterator, List


class RouteRestTableDef(Sequence[AbstractRouteDef]):
    """Route definition table"""

    def __init__(self) -> None:
        self._items = []  # type: List[AbstractRouteDef]

    def __repr__(self) -> str:
        return "<RouteRestTableDef count={}>".format(len(self._items))

    @overload
    def __getitem__(self, index: int) -> AbstractRouteDef: ...  # noqa

    @overload  # noqa
    def __getitem__(self, index: slice) -> List[AbstractRouteDef]: ...  # noqa

    def __getitem__(self, index):  # type: ignore  # noqa
        return self._items[index]

    def __iter__(self) -> Iterator[AbstractRouteDef]:
        return iter(self._items)

    def __len__(self) -> int:
        return len(self._items)

    def __contains__(self, item: object) -> bool:
        return item in self._items

    def route(self,
              method: str,
              path: str,
              **kwargs: Any) -> _Deco:
        def inner(handler: _HandlerType) -> _HandlerType:
            self._items.append(RouteDef(method, path, handler, kwargs))
            self._items.append(
                RouteDef(method, path + "/{id}", handler, kwargs))
            return handler
        return inner

    def resource(self, path: str, **kwargs: Any) -> _Deco:
        return self.route(hdrs.METH_ANY, path, **kwargs)

    def add_route(self, path: str, handler: _HandlerType, **kwargs: Any):
        self._items.append(RouteDef(hdrs.METH_ANY, path, handler, kwargs))
        self._items.append(
            RouteDef(hdrs.METH_ANY, path + "/{id}", handler, kwargs))
