from flask import Flask, jsonify, json, request, abort, render_template, Blueprint, Response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.serializer import loads, dumps
from datetime import datetime

from ..database import session_scope
from ..invoice.service import InvoiceService
from . import invoices_bp


@invoices_bp.route('/sales/invoices/GetNewSpireInvoices', methods=['GET'])
def GetNewSpireInvoices():
    try:
        result = []  

        lastSynchronized = request.args.get('lastSynchronized')
        
        if not lastSynchronized:
            raise Exception("missing lastSynchronized")
        
        modified = datetime.strptime(lastSynchronized, '%m/%d/%Y %H:%M:%S %p').strftime('%Y-%m-%d %H:%M:%S %p') 

        invoices = InvoiceService.getRecentInvoices(modified)

        for invoice in invoices:
                result.append({
                    'id': invoice.id,
                    'invoiceNo': invoice.invoice_no,
                    'invoiceDate': invoice.invoice_date,
                    'orderNo': invoice.order_no,
                    'division': invoice.division,
                    'location': invoice.location,
                    'profitCenter': invoice.profit_center,
                    'orderDate': invoice.order_date,
                    'requiredDate': invoice.required_date,
                    'created': invoice._created,
                    'modified': invoice._modified,
                    'createdBy': invoice._created_by,
                    'modifiedBy': invoice._modified_by
                })

        return Response(status=200, mimetype='application/json', response= json.dumps(result) if result else 'null')

    except Exception as e:
        abort(404, description=str(e))

    return result


@invoices_bp.route('/sales/invoices/GetAllSpireInvoices', methods=['GET'])
def GetAllSpireInvoices():
    result = []                
            
    try:
        with session_scope() as session:
        
            invoices = InvoiceService.getAllInvoices()
            
            for invoice in invoices:
                result.append({
                    'id': invoice.id,
                    'invoiceNo': invoice.invoice_no,
                    'invoiceDate': invoice.invoice_date,
                    'orderNo': invoice.order_no,
                    'division': invoice.division,
                    'location': invoice.location,
                    'profitCenter': invoice.profit_center,
                    'orderDate': invoice.order_date,
                    'requiredDate': invoice.required_date,
                    'created': invoice._created,
                    'modified': invoice._modified,
                    'createdBy': invoice._created_by,
                    'modifiedBy': invoice._modified_by
                })


            return Response(status=200, mimetype='application/json', response= json.dumps(result) if result else 'null')

    except Exception as ex:
        abort(404, description=str(ex))
        
    return result