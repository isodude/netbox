from netbox.search import SearchIndex, register_search
from . import models


@register_search
class L2VPNIndex(SearchIndex):
    model = models.L2VPN
    fields = (
        ('name', 100),
        ('slug', 110),
        ('description', 500),
        ('comments', 5000),
    )
    display_attrs = ('type', 'identifier', 'tenant', 'description')
