from .views import RestView
from .routers import RouteRestTableDef

__version__ = '0.1.2'

__all__ = (
    'RestView',
    'RouteRestTableDef',
)

routes = RouteRestTableDef()
