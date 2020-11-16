from flask import Flask, jsonify, json, request, abort, render_template, Blueprint
from ..models import SalesTax
from ...database import session_scope

class SalesTaxRepository:

    def getSalesTaxByNumber(TaxNos):
        try:
            with session_scope() as session:      

                sales_tax = session.query(SalesTax)\
                                   .filter(SalesTax.tax_no.in_(TaxNos)) \
                                   .all()

                return sales_tax

        except Exception as ex:
            raise Exception(str(ex))
        
        return None