Asynchronous restful API
================================

[![PyPI](https://img.shields.io/pypi/v/pycaches?style=flat-square)](https://pypi.org/project/pycaches/)
[![Travis build on master](https://img.shields.io/travis/codingjerk/pycaches/master?style=flat-square)](https://travis-ci.org/github/codingjerk/pycaches)
[![Travis build on develop](https://img.shields.io/travis/codingjerk/pycaches/develop?label=develop&style=flat-square)](https://travis-ci.org/github/codingjerk/pycaches)
[![Codecov coverage](https://img.shields.io/codecov/c/gh/codingjerk/pycaches/develop?token=VHP5IBJTDJ&style=flat-square)](https://codecov.io/gh/codingjerk/pycaches/)
[![Chat on Gitter](https://img.shields.io/gitter/room/codingjerk/pycaches?style=flat-square)](https://gitter.im/codingjerk/pycaches)
![License](https://img.shields.io/pypi/l/pycaches?style=flat-square)

特色
------------

✓ 基于aiohttp的异步web后端，实现了路由层和视图层

✓ 使用设计较友好


安装
------------
```sh
pip install asyncweb
```

开始使用
---------------

“pyapi”允许您在几个步骤中快速创建一个rest资源。
它自动在集合或单个项上创建资源路由;只需在方法上指定'_collection'或'_item'后缀即可。
使用python字典，结果/请求的序列化/反序列化是透明的。

使用案例

```python
from aiohttp import web
from asyncweb import RestView, routes


@routes.resource("/views")
class RestResource(RestView):

    # example call: GET to <server>/views?start=10
    async def on_get_collection(self, start=0) -> list:
        return [
            {"id": int(start) + 1, "value": 1},
            {"id": int(start) + 2, "value": 2},
        ]

    # example call: GET <server>/views/80
    async def on_get_item(self, id: str) -> dict:
        return self.key

    # example call: POST to <server>/views
    async def on_post_collection(self, body: dict) -> dict:
        return body


app = web.Application()
app.add_routes(routes)
app['key'] = [1, 2, 4, 5]

if __name__ == '__main__':
    web.run_app(app)
```