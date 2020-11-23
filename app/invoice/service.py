from flask import Flask, jsonify, json, request, abort, render_template, Blueprint
from datetime import datetime

from .repository import InvoiceRepository

class InvoiceService:
    def __init__(self):
        pass
    
    def getRecentInvoices(modified):
        try:
            return InvoiceRepository.getRecentInvoices(modified)
        except Exception as ex:
            raise Exception(str(ex))

    def getAllInvoices():
        try:
            return InvoiceRepository.getAllInvoices()
        except Exception as ex:
            raise Exception(str(ex))