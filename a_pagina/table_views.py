from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Ticket, ItemPedido, Producto
from django.core.paginator import Paginator
from django.http import HttpResponse
import json

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
    filtros_mesa = ["PENDIENTE","A PAGAR"]
    lista_mesas = Ticket.objects.filter(caja__in=filtros_mesa,tipo="MESA").order_by('mesa')
    if mesa != None:
        mesaNum = int(mesa)
        lista_mesa_num = Ticket.objects.filter(mesa=mesaNum,tipo="MESA",caja="PENDIENTE").order_by('-add_time')
        if lista_mesa_num.count() == 0:
            return HttpResponse(f"No hay tickets con esa mesa numero {mesaNum}")
        else:
            context = {
                'title': "BIDMAX - MESAS PENDIENTES",
                'color': "#0F172A",
                'items': lista_mesas,
                'tab_context': f"MESAS_PENDIENTES {mesaNum}",
                'tabla_mesa' : lista_mesa_num
            }
            return render(request, "sub_index.html", context)
    else:
        context = {
            'title': "BIDMAX - MESAS PENDIENTES",
            'color': "#0F172A",
            'items': lista_mesas,
            'tab_context': "MESAS_PENDIENTES"
        }
        return render(request, "sub_index.html", context)




    