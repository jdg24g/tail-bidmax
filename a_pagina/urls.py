from django.urls import path
from . import views
from .views import DeleteTicketView, EditarTicketView

urlpatterns = [
    path('', views.index, name='index'),
    path('ticket/<int:pk>/', views.detalle_ticket, name='detalle_ticket'),
    path('ticket/<int:pk>/ver/', views.ver_ticket, name='ver_ticket'),
    path('crear-ticket/', views.crear_ticket, name='crear_ticket'),
    path('delete-ticket/<int:pk>/', DeleteTicketView.as_view(), name='delete_ticket'),
    path('editar-ticket/<int:pk>/', EditarTicketView.as_view(), name='editar_ticket'),
    path('login/', views.login_page, name='login_page'),
    path('cocina/', views.cocina_views, name='cocina_views'),
]
