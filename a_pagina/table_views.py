from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Ticket, ItemPedido, Producto
from django.core.paginator import Paginator
from django.http import HttpResponse

@login_required(login_url="/login/")
def tabla_delivery(request):
    title = "BIDMAX - DELIVERY"
    color = "#0F172A"
    filtros = ["PENDIENTE","A PAGAR"]
    lista_tickets = Ticket.objects.filter(caja__in=filtros,tipo="DELIVERY").order_by('-add_time')
    paginator = Paginator(lista_tickets,50)
    page_number = request.GET.get('page',1)
    tickets = paginator.get_page(page_number)
    context = {
        'title':title,
        'items':tickets,
        'color':color,
        'tab_context':"DELIVERY"
    }
    return render(request,"index.html",context)

@login_required(login_url="/login/")
def tabla_cobrado(request):
    title = "BIDMAX - COBRADO"
    color = "#0F172A"
    filtros = ["COBRADO"]
    lista_tickets = Ticket.objects.filter(caja__in=filtros).order_by('-add_time')
    paginator = Paginator(lista_tickets,50)
    page_number = request.GET.get('page',1)
    tickets = paginator.get_page(page_number)
    context = {
        'title':title,
        'items':tickets,
        'color':color,
        'tab_context':"COBRADO"
    }
    return render(request,"index.html",context)

@login_required(login_url="/login/")
def tabla_delivery_todos(request):
    title = "BIDMAX - DELIVERY TODOS"
    color = "#0F172A"
    lista_tickets = Ticket.objects.filter(tipo="DELIVERY").order_by('-add_time')
    pagintor = Paginator(lista_tickets,5)
    page_number = request.GET.get('page',1)
    tickets = pagintor.get_page(page_number)
    context ={
        'title' : title,
        'color': color,
        'items' : tickets,
        'tab_context' : "DELIVERY_TODOS"
    }
    return render(request,"index.html",context)
    

@login_required(login_url='/login/')
def ver_tabla_por_mesa(request, mesa=None):
    if mesa != None:
        mesa = int(mesa)
        lista_tickets = Ticket.objects.filter(mesa=mesa,tipo="MESA",caja="PENDIENTE").order_by('-add_time')
        if lista_tickets.count() == 0:
            return HttpResponse(f"No hay tickets con esa mesa numero {mesa}")
        pagintor = Paginator(lista_tickets,5)
        page_number = request.GET.get('page',1)
        tickets = pagintor.get_page(page_number)
        context ={
            'title' : "BIDMAX - MESA: " + str(mesa),
            'color': "#0F172A",
            'items' : tickets,
            'tab_context' : "PENDIENTE",
            "mostrar_tabla": True
        }
        return render(request,"index.html",context)
    else:
        filtro = ["PENDIENTE","A PAGAR"]
        mesas = Ticket.objects.filter(caja__in=filtro,tipo="MESA").order_by('mesa')
        context = {
            'title': "BIDMAX - MESAS PENDIENTES",
            'color': "#0F172A",
            'items': mesas,
            'tab_context': "PENDIENTE",
            "mostrar_tabla": False
        }
        return render(request, "sub_index.html", context)


    
    
    