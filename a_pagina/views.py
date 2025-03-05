#views.py
from django.shortcuts import render,redirect,get_object_or_404
from .models import ItemPedido,Ticket,Cliente,Producto
from django.contrib.auth.decorators import login_required
from .models import tipo  
from django.http import JsonResponse
from django.views import View
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

#login required redirect to django admin login page
@login_required(login_url='/login/')
def index(request):
    title = "BIDMAX - INICIO"
    color = "#0F172A"
    
    # Obtener todos los tickets ordenados
    lista_tickets = Ticket.objects.all().order_by('-add_time')
    
    # Crear el paginador con 50 items por página
    paginator = Paginator(lista_tickets, 50)
    
    # Obtener el número de página desde la URL
    page_number = request.GET.get('page', 1)
    
    # Obtener los tickets para la página actual
    tickets = paginator.get_page(page_number)
    
    context = {
        'title': title,
        'items': tickets,  # Mantiene el mismo nombre 'items' para compatibilidad con el template
        'color': color
    }
    return render(request, 'index.html', context)

@login_required(login_url='/login/')
def ver_ticket(request,pk):
    ticket = get_object_or_404(Ticket,pk=pk)
    items = ItemPedido.objects.filter(ticket=ticket)
    total = sum(item.producto.precio * item.cantidad for item in items)
    context = {
        'ticket':ticket,
        'items':items,
        'total':total
    }
    return render(request,'watch.html',context)

@login_required(login_url='/login/')
def detalle_ticket(request,pk):
    ticket = get_object_or_404(Ticket,pk=pk)
    items = ItemPedido.objects.filter(ticket=ticket)
    total = sum(item.producto.precio * item.cantidad for item in items)
    context = {
        'ticket':ticket,
        'items':items,
        'total':total
    }
    return render(request,'detalle_ticket.html',context)

@login_required(login_url='/login/')
def crear_ticket(request):
    if request.method == 'POST':
        # Crear el ticket
        ticket = Ticket.objects.create(
            tipo=request.POST['tipo'],
            cliente=request.POST['cliente'],
            celular=request.POST.get('celular'),
            mesa=request.POST.get('mesa') if request.POST.get('mesa') else None,
            observacion=request.POST.get('observacion')
        )
        
        # Crear los items del pedido
        productos = request.POST.getlist('productos[]')
        cantidades = request.POST.getlist('cantidades[]')
        
        for producto_id, cantidad in zip(productos, cantidades):
            ItemPedido.objects.create(
                ticket=ticket,
                producto_id=producto_id,
                cantidad=int(cantidad)
            )
        items = ItemPedido.objects.filter(ticket=ticket)
        total = sum(item.producto.precio * item.cantidad for item in items)
        async_to_sync(get_channel_layer().group_send)(
                "tickets",
                {
                    "type": "ticket_created",
                    "message": {
                        "action": "created",
                    }
                }
            )

        if 'imprimir' in request.POST:
            return JsonResponse({
                'success': True,
                'ticket_id': ticket.id
            })
        return redirect('index')
    
    # GET request
    title = "BIDMAX - CREAR TICKET"
    color = "#0F172A"
    context = {
        'title': title,
        'color': color,
        'productos': Producto.objects.all(),
        'tipos': tipo,
    }
    return render(request, 'crear_ticket.html', context)

class DeleteTicketView(View):
    def delete(self, request, pk):
        try:
            ticket = get_object_or_404(Ticket, pk=pk)
            ticket.delete()
            async_to_sync(get_channel_layer().group_send)(
                "tickets",
                {
                    "type": "ticket_deleted",
                    "message": {
                        "action": "deleted",
                    }
                }
            )
            return JsonResponse({'message': 'Ticket eliminado correctamente'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

class EditarTicketView(UpdateView):
    model = Ticket
    template_name = 'editar_ticket.html'
    fields = ['tipo', 'cliente', 'celular', 'mesa', 'observacion']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = Producto.objects.all()
        return context

    def form_valid(self, form):
        self.object = form.save()
        
        # Obtener los productos y cantidades del formulario
        productos = self.request.POST.getlist('productos[]')
        cantidades = self.request.POST.getlist('cantidades[]')
        
        # Eliminar todos los items existentes
        self.object.itempedido_set.all().delete()
        
        # Crear los nuevos items
        for producto_id, cantidad in zip(productos, cantidades):
            ItemPedido.objects.create(
                ticket=self.object,
                producto_id=producto_id,
                cantidad=int(cantidad)
            )

        # Enviar notificación WebSocket
        async_to_sync(get_channel_layer().group_send)(
            "tickets",
            {
                "type": "ticket_updated",
                "message": {
                    "action": "updated",
                }
            }
        )

        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': True, 'redirect_url': self.get_success_url()})
        return redirect('index')
    
def login_page(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        try:
            if user is not None:
                login(request,user)
                return redirect('index')
            else:
                error_message = 'Usuario o contraseña incorrectos'
        except Exception as e:
            error_message = str(e)
    context = {
        'error_message': error_message,
        'title': 'BIDMAX - LOGIN',
        'color': '#0F172A'
    }
    return render(request, 'login.html', context)
