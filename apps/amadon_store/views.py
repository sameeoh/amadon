# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited

def index(request):
    if not 'items' in request.session:
        request.session['items'] = []
    if not 'total' in request.session:
        request.session['total'] = 0.0
    if not 'total_items' in request.session:
        request.session['total_items'] = 0
    if not 'spent' in request.session:
        request.session['spent'] = 0
    return render(request, "amadon_store/index.html")

def buy(request):
    if request.POST['product_id'] == '1015':
        price = 19.99
    elif request.POST['product_id'] == '1016':
        price = 29.99
    elif request.POST['product_id'] == '1017':
        price = 4.99
    request.session['spent'] = price * float(request.POST['quantity'])
    request.session['total'] += price * float(request.POST['quantity'])
    request.session['total_items'] += int(request.POST['quantity'])

    return redirect ('/amadon/checkout')

def checkout(request):
    context = {
        'items': request.session['items']
    }
    print context
    return render(request, 'amadon_store/checkout.html', context)

def clear(request):
    request.session.clear()
    return redirect('/')
