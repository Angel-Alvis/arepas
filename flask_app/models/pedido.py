from flask_app.config.mysqlconnection import MySQLConnection
from flask import flash

class Pedido:
    def __init__(self, data):
        self.nombre=data["nombre"]
        self.cantidad=data['cantidad']
        self.relleno=data['relleno']
        self.created_at=data["created_at"]
        self.updated_at=data['updated_at']
    
    @classmethod
    def get_all(cls):
        query='''select *
        from arepas;'''
        resultados=MySQLConnection('db_arepas').query_db(query)
        return resultados
    
    @classmethod
    def insert(cls,datos):
        query='''insert into arepas(nombre, cantidad, relleno)
        values(%(nombre)s, %(cantidad)s, %(relleno)s)'''
        return MySQLConnection('db_arepas').query_db(query, datos)
    
    @staticmethod
    def validar_pedido(pedido):
        esCorrecto = True
        if len(pedido["nombre"]) <= 2:
            flash('Nombre no valido','nombre')
            esCorrecto = False
        if int(pedido["cantidad"]) <= 0:
            flash('Cantidad no valida','cantidad')
            esCorrecto = False
        if len(pedido['relleno']) <= 2:
            flash('Relleno no valido','relleno')
            esCorrecto = False
        if esCorrecto:
            flash('Pedido realizado', 'exito')
        return esCorrecto