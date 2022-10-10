from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
        path('core/', include('payment.urls')),
#     path('about/', views.about, name='about'),
#     path('dashboard/', views.dashboard, name='dashboard'),
#     path('services/', views.services, name='services'),
#     path('sales/', views.sales, name='sales'),
#     path('fees/', views.fees, name='fees'),
#     path('fines/', views.fines, name='fines'),
#     path('licences/', views.licences, name='licences'),
#     path('general/', views.general, name='general'),
    path('connect/', views.connect, name='connector'),
    path('payment/', views.payment, name='payment'),
    path('verify/', views.verify, name='verify'),
#     path('otppin/', views.pinotp, name='otp'),
#     path('terms_and_condition/', views.terms_and_condition, name='terms'),
#     path('authentication/', include('authentication.urls')),
#     path('activate/<uidb64>/<token>',activate, name='activate'),
]


# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)