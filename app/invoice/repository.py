from flask import Flask, jsonify, json, request, abort, render_template, Blueprint
from .models import SalesHistory
from ..database import session_scope

class InvoiceRepository:

    def getRecentInvoices(modified):
        try:
            with session_scope() as session:      

                    invoices = session.query(SalesHistory) \
                                      .filter(SalesHistory._modified > modified) \
                                      .all()
                                 
                    return invoices

        except Exception as ex:
           raise Exception(str(ex))
        
        return None

    def getAllInvoices():
        try:
            with session_scope() as session:      

                    return session.query(SalesHistory) \
                                      .all()

        except Exception as ex:
           raise Exception(str(ex))
        
        return None