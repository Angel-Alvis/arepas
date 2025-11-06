from flask_app import app
from flask import redirect, render_template, flash, request
from flask_app.models import pedido

@app.route('/')
def pag_inicio():
    return render_template('inicio.html')

@app.route('/crear_pedido', methods=['POST','GET'])
def form_pedido():
    if request.method=='GET':
        return redirect('/')
    datos={
        'nombre':request.form['nombre'],
        'cantidad':request.form['cantidad'],
        'relleno':request.form['relleno']
    }
    if not pedido.Pedido.validar_pedido(datos):
        return redirect('/')
    pedido.Pedido.insert(datos)
    return redirect('/')

@app.route('/ver_pedidos')
def pagPedidos():
    pedidos=pedido.Pedido.get_all()
    return render_template('pedidos.html', pedidos=pedidos)