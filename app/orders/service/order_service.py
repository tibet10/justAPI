from flask import Flask, jsonify, json, request, abort, render_template, Blueprint
from ..repository.order_repository import OrderRepository
from ..repository.order_items_repository import OrderItemRepository
from ..repository.customer_repository import CustomerRepository
from ..repository.address_repository import AddressRepository
from ..service.order_item_service import OrderItemService
from ..service.customer_service import CustomerService
from ..service.address_service import AddressService
from ..service.sales_tax_service import SalesTaxService
from ...database import session_scope
from datetime import datetime

class OrderService:

    def getOrderById(id):
        try:
            return OrderRepository.getOrderById(id)
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
            if sales_order:    
                
                result = {
                    "id": sales_order.id,
                    "orderNo": sales_order.order_no,
                    "status": sales_order.status,
                    "type": sales_order.order_type,
                    "orderDate": sales_order.order_date,
                    "subtotal": str(sales_order.subtotal),
                    "total": str(sales_order.total),
                    "created": sales_order._created,
                    "modified": sales_order._modified,
                    "createdBy": sales_order._created_by,
                    "modifiedBy": sales_order._modified_by,
                    "shippingCarrier": sales_order.ship_carrier,
                    "shipDate": sales_order.ship_date,
                    "trackingNo": sales_order.ship_track_id,
                    "discount": str(sales_order.discount),
                    "totalDiscount": str(sales_order.total_discount)
                }

                sales_order_items = OrderItemRepository.getOrderItemsByOrderNo(sales_order.order_no)
                result['items'] = OrderItemService.createOrderItemDetails(sales_order_items)

                customer = CustomerRepository.getCustomerByNo(sales_order.cust_no)
                result['customer'] = CustomerService.createCustomerDetails(customer)

                billing_address = AddressRepository.getBillingAddressByOrderNo(sales_order.order_no)
                result['address'] = AddressService.createBillingAddressDetails(billing_address)

                shipping_address = AddressRepository.getShippingAddressByOrderNo(sales_order.order_no)                
                result['shippingAddress'] = AddressService.createShippingAddressDetails(shipping_address)

                sales_taxes = SalesTaxService.getSalesTaxByNumber(shipping_address.sales_tax_no)
                result['taxes'] = SalesTaxService.createTaxDetails(sales_taxes)
                
            return result

        except Exception as ex:
            raise Exception(str(ex))
        
        return None