from .purchase_order import purchase_order_urlpatterns
from .vendor import vendor_urlpatterns

urlpatterns = []
urlpatterns += vendor_urlpatterns
urlpatterns += purchase_order_urlpatterns
