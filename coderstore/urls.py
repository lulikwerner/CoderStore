from django.contrib import admin
from django.urls import path, include
from coderstore.views import all_products, home_page, search_products, index, about_us
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('meat/', include('meat.urls')),
    path('drink/', include('drink.urls')),
    path('bakery/', include('bakery.urls')),
    path('search/', search_products, name='search-products'),
    path('inicio/', home_page, name='inicio'),
    path('user/', include('users.urls')),
    path('contact/', include('contact.urls')),
    path('all/', all_products, name='all_products'),
    path('stock/', include('stock.urls')),
    path('cart/', include('cart.urls')),
    path('about/', about_us, name='about'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
