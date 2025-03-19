from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Ticket, ItemPedido, Producto
from django.core.paginator import Paginator

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