from flask import Flask, jsonify, json, request, abort, render_template, Blueprint
from ..repository.sales_tax_repository import SalesTaxRepository
from ...database import session_scope

class SalesTaxService:

    def getSalesTaxByNumber(TaxNos):
        try:
            return SalesTaxRepository.getSalesTaxByNumber(TaxNos)
        except Exception as ex:
            raise Exception(str(ex))

    
    def createTaxDetails(sales_taxes):
        try:
            result = []

            for row in sales_taxes:

                result.append({
                    "code": row.tax_no,
                    "name": row.name,
                    "rate": str(row.rate),
                    "total": "0"
                })
            
            return result

        except Exception as ex:
            raise Exception(str(ex))
        
        return result