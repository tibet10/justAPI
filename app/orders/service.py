from flask import Flask, jsonify, json, request, abort, render_template, Blueprint
from datetime import datetime

from .repository import OrderRepository
from ..customer.service import CustomerService
from ..address.service import AddressService
from ..tax.service import SalesTaxService
from ..inventory.service import InventoryService

class OrderService:

    def __init__(self):
        pass

    def getOrderById(id):
        try:
            return OrderRepository.getOrderById(id)
        except Exception as ex:
            raise Exception(str(ex))
    
    def getOrderByOrderNo(orderNo):
        try:
            return OrderRepository.getOrderByOrderNo(orderNo)
        except Exception as ex:
            raise Exception(str(ex))

    def getAllOrders():
        try:
            return OrderRepository.getAllOrders()
        except Exception as ex:
            raise Exception(str(ex))

    def getRecentOrders(modified):
        try:
            return OrderRepository.getRecentOrders(modified)
        except Exception as ex:
            raise Exception(str(ex))

    def getDeletedOrders():
        try:
            return OrderRepository.getDeletedOrders()
        except Exception as ex:
            raise Exception(str(ex))

    def buildOrderDetails(sales_order):
        try:
            result = {}

            if sales_order:    
                
                result['id']= sales_order.id
                result['orderNo']= sales_order.order_no
                result['status']= sales_order.status
                result['type']= sales_order.order_type
                result['orderDate']= sales_order.order_date
                result['subtotal']= str(sales_order.subtotal)
                result['total']= str(sales_order.total)
                result['created']= sales_order._created
                result['modified']= sales_order._modified
                result['createdBy']= sales_order._created_by
                result['modifiedBy']= sales_order._modified_by
                result['shippingCarrier']= sales_order.ship_carrier
                result['shipDate']= sales_order.ship_date
                result['trackingNo']= sales_order.ship_track_id
                result['discount']= str(sales_order.discount)
                result['totalDiscount']= str(sales_order.total_discount)

                sales_order_items = OrderRepository.getOrderItemsByOrderNo(sales_order.order_no)
                result['items'] = OrderService.createOrderItemDetails(sales_order_items)

                customer = CustomerService.getCustomerByNo(sales_order.cust_no)
                result['customer'] = CustomerService.createCustomerDetails(customer)

                billing_address = AddressService.getBillingAddressByOrderNo(sales_order.order_no)
                result['address'] = AddressService.createBillingAddressDetails(billing_address)

                shipping_address = AddressService.getShippingAddressByOrderNo(sales_order.order_no)                
                result['shippingAddress'] = AddressService.createShippingAddressDetails(shipping_address)

                sales_taxes = SalesTaxService.getSalesTaxByNumber(shipping_address.sales_tax_no)
                result['taxes'] = SalesTaxService.createTaxDetails(sales_taxes)
                
            return result

        except Exception as ex:
            raise Exception(str(ex))
        
        return None

    def createOrderItemDetails(sales_order_items):
        try:
            result = []

            for row in sales_order_items:

                inventory = InventoryService.getInventoryByPartNo(row.part_no)
                
                result.append({
                    'id': row.id,
                    'partNo': row.part_no,
                    'description': row.description,
                    'orderQty': int(row.order_qty),
                    'unitPrice': str(row.unit_price),
                    'inventory': InventoryService.createInventoryDetails(inventory) if inventory != None else None,
                    'retailPrice': str(row.retail_price),
                    'vendor': row.vendor_no,
                    'sequence': row.sequence
                })
            
            return result

        except Exception as ex:
            raise Exception(str(ex))
        
        return result