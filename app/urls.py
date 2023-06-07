from django.urls import path

# urlpatterns = [
#   path("", views.index, name="index"),
#  path("about", views.about, name="about"),
# ]
from django.urls import path
from app.views import index, create_stock, update_stock, delete_stock

# from django.conf import settings
# from django.conf.urls.static import static


urlpatterns = [
    path("", index, name="index"),
    path("create/", create_stock, name="create_stock"),
    path("update/<int:pk>/", update_stock, name="update_stock"),
    path("delete/<int:pk>/", delete_stock, name="delete_stock"),
]
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
