from django.contrib import admin
from django.urls import path, include
import phone_calls.views
from portfolio import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', phone_calls.views.start, name='phone_numbers'),
    path('upload_file/', phone_calls.views.upload_file, name='upload'),
    path('success/url/', phone_calls.views.success, name='success'),
    path('success/url/<int:number>/', phone_calls.views.show_details),
    path('error/', phone_calls.views.error, name='error'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)