from django.urls import path
from . import views
from .views import DeleteTicketView, EditarTicketView,tabla_todos
from .table_views import tabla_delivery,tabla_cobrado,tabla_delivery_todos,ver_tabla_por_mesa
urlpatterns = [
    path('', views.index, name='index'),
    path('ticket/<int:pk>/', views.detalle_ticket, name='detalle_ticket'),
    path('ticket/<int:pk>/ver/', views.ver_ticket, name='ver_ticket'),
    path('crear-ticket/', views.crear_ticket, name='crear_ticket'),
    path('delete-ticket/<int:pk>/', DeleteTicketView.as_view(), name='delete_ticket'),
    path('editar-ticket/<int:pk>/', EditarTicketView.as_view(), name='editar_ticket'),
    path('login/', views.login_page, name='login_page'),
    path('cocina/', views.cocina_views, name='cocina_views'),
    path('cocina/cambiarEstado/<int:pk>/listo', views.cambiar_estado_listo, name='cambiar_estado_listo'),
    path('cocina/cambiarEstado/<int:pk>/cancelado', views.cambiar_estado_cancelado, name='cambiar_estado_cancelado'),
    path('tabla-delivery/', tabla_delivery, name='tabla_delivery'),
    path('tabla-cobrado/', tabla_cobrado, name='tabla_cobrado'),
    path('tabla-todos/', tabla_todos, name='tabla_todos'),
    path('tabla-delivery-todos/', tabla_delivery_todos, name='tabla_delivery_todos'),
    path('cambiarCajaCobrado/<int:pk>/', views.cambiar_caja_cobrado, name='cambiar_caja_cobrado'),
    path('ver-tabla-por-mesa/', ver_tabla_por_mesa, name='ver_tabla_por_mesa'),
    path('ver-tabla-por-mesa/<int:mesa>/', ver_tabla_por_mesa, name='tabla_por_mesas'),

]
