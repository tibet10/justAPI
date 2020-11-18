from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, Numeric, String, Table, Text, text, BigInteger, Date, SmallInteger, UniqueConstraint, Index
from sqlalchemy.dialects.postgresql import UUID, ARRAY, HSTORE
from sqlalchemy.orm import relationship
from ..database import Base

metadata = Base.metadata

class SalesOrder(Base):
    
    __tablename__ = 'sales_orders'
    
    id = Column(Integer, primary_key=True, server_default=text("nextval('sales_orders_id_seq'::regclass)"))
    order_type = Column(String(1))
    hold = Column(Boolean)
    inv_date_rrule = Column(String(120))
    batch_no = Column(BigInteger)
    total_payments = Column(Numeric(15, 2), nullable=False)
    backordered = Column(Boolean)
    sales_tax_applicable_ordered = Column(ARRAY(Numeric(precision=15, scale=2)), nullable=False, server_default=text("'{0,0,0,0}'::numeric[]"))
    subtotal_ordered = Column(Numeric(15, 2), nullable=False)
    total_discount_ordered = Column(Numeric(15, 2), nullable=False)
    freight_ordered = Column(Numeric(15, 2), nullable=False)
    sales_tax_total_ordered = Column(ARRAY(Numeric(precision=15, scale=2)), nullable=False, server_default=text("'{0,0,0,0}'::numeric[]"))
    sales_tax_ordered = Column(Numeric(15, 2), nullable=False)
    gross_profit_ordered = Column(Numeric(15, 2), nullable=False)
    current_cost_ordered = Column(Numeric(15, 2), nullable=False)
    average_cost_ordered = Column(Numeric(15, 2), nullable=False)
    standard_cost_ordered = Column(Numeric(15, 5), nullable=False)
    total_ordered = Column(Numeric(15, 2), nullable=False)
    total_surcharge_ordered = Column(Numeric(15, 2), nullable=False, server_default=text("'0'::numeric"))
    backorder_created = Column(Boolean)
    cr_approve_amt = Column(Numeric(15, 2), nullable=False)
    cr_approve_date = Column(Date)
    cr_approve_user = Column(String(3))
    _deleted = Column(DateTime)
    _deleted_by = Column(String(3))
    _dbversion = Column(Integer)
    _modified = Column(DateTime)
    _modified_by = Column(String(3))
    _created = Column(DateTime)
    _created_by = Column(String(3))
    order_no = Column(String(10), unique=True)
    order_date = Column(Date)
    invoice_no = Column(String(10))
    invoice_date = Column(Date)
    cust_no = Column(String(20), index=True)
    cust_name = Column(String(60))
    cust_po_no = Column(String(20))
    status = Column(String(1), index=True)
    division = Column(String(3))
    location = Column(String(24))
    profit_center = Column(String(24))
    territory_code = Column(String(10))
    salesperson_no = Column(String(10))
    ship_id = Column(String(20), nullable=False)
    ship_code = Column(String(10))
    ship_date = Column(Date)
    required_date = Column(Date)
    ship_carrier = Column(String(20))
    ship_track_id = Column(String(50))
    pack_date = Column(Date)
    pack_init = Column(String(3))
    ref_no = Column(String(20))
    terms_code = Column(String(10))
    terms_description = Column(String(60))
    terms_days_before_due = Column(SmallInteger)
    terms_days_allowed = Column(SmallInteger)
    terms_discount_rate = Column(Numeric(5, 2), nullable=False)
    fob = Column(String(20))
    currency = Column(String(3), nullable=False, server_default=text("''::character varying"))
    currency_rate_method = Column(String(1))
    currency_rate = Column(Numeric(13, 7), nullable=False)
    discount = Column(Numeric(5, 2), nullable=False)
    was_quote_no = Column(String(10))
    sales_tax_rate = Column(ARRAY(Numeric(precision=7, scale=4)), nullable=False, server_default=text("'{0,0,0,0}'::numeric[]"))
    sales_tax_applicable = Column(ARRAY(Numeric(precision=15, scale=2)), nullable=False, server_default=text("'{0,0,0,0}'::numeric[]"))
    partial_tax_rate = Column(Numeric(7, 4), server_default=text("'0'::numeric"))
    partial_tax_total = Column(Numeric(15, 2), server_default=text("'0'::numeric"))
    subtotal = Column(Numeric(15, 2), nullable=False)
    total_discount = Column(Numeric(15, 2), nullable=False)
    freight = Column(Numeric(15, 2), nullable=False)
    user_freight = Column(Boolean, nullable=False, server_default=text("false"))
    sales_tax_total = Column(ARRAY(Numeric(precision=15, scale=2)), nullable=False, server_default=text("'{0,0,0,0}'::numeric[]"))
    sales_tax = Column(Numeric(15, 2), nullable=False)
    gross_profit = Column(Numeric(15, 2), nullable=False)
    total_current_cost = Column(Numeric(15, 2), nullable=False)
    total_average_cost = Column(Numeric(15, 2), nullable=False)
    total_standard_cost = Column(Numeric(15, 2), nullable=False)
    total = Column(Numeric(15, 2), nullable=False)
    total_surcharge = Column(Numeric(15, 2), nullable=False, server_default=text("'0'::numeric"))
    user_surcharge = Column(Boolean)
    last_inv_no = Column(String(10))
    last_inv_date = Column(Date)
    processed_user = Column(String(3))
    processed_date = Column(DateTime)
    invoiced_user = Column(String(3))
    invoiced_date = Column(DateTime)
    job_no = Column(String(10))
    job_acct_no = Column(String(10))
    phase_id = Column(String(20))
    contact_name = Column(String(60))
    contact_phone = Column(String(30))
    contact_fax = Column(String(30))
    contact_phone_type = Column(SmallInteger)
    contact_fax_type = Column(SmallInteger)
    contact_email = Column(String(254))
    total_weight = Column(Numeric(15, 2))
    udf_data = Column(HSTORE(Text()), server_default=text("''::hstore"))

    def __repr__(self):
        return ('<SalesOrder({0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15},{16},{17},{18})>') \
                    .format(self.id, 
                            self.order_no,
                            self.status, 
                            self.order_date,
                            self._created,
                            self._created_by,
                            self._modified,
                            self._modified_by,
                            self.cust_no,
                            self.order_type,
                            self.subtotal,
                            self.total,
                            self.ship_carrier,
                            self.ship_date,
                            self.ship_track_id,
                            self.discount,
                            self.total_discount,
                            self.sales_tax_total,
                            self._deleted)

class SalesOrderItem(Base):
    __tablename__ = 'sales_order_items'
    __table_args__ = (
        UniqueConstraint('order_no', 'sequence'),
        Index('sales_order_items_whse_part_no_idx', 'whse', 'part_no'),
        Index('sales_order_items_guid_order_no_idx', 'guid', 'order_no', unique=True)
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('sales_order_items_id_seq'::regclass)"))
    order_no = Column(String(10), index=True)
    req_no = Column(String(10))
    backorder_todate_qty = Column(Numeric(15, 5), nullable=False)
    _deleted = Column(DateTime)
    _deleted_by = Column(String(3))
    _dbversion = Column(Integer)
    _modified = Column(DateTime)
    _modified_by = Column(String(3))
    _created = Column(DateTime)
    _created_by = Column(String(3))
    sequence = Column(SmallInteger)
    parent_item = Column(SmallInteger)
    guid = Column(String(32))
    item_type = Column(SmallInteger, nullable=False)
    whse = Column(String(6))
    part_no = Column(String(34))
    description = Column(String(80))
    product_code = Column(String(10))
    uom_inventory = Column(String(10))
    uom_sales = Column(String(10))
    uom_sales_factor = Column(Numeric(11, 5))
    sell_direct_factor = Column(Boolean)
    order_qty = Column(Numeric(15, 5), nullable=False, server_default=text("'0'::numeric"))
    committed_qty = Column(Numeric(15, 5), nullable=False, server_default=text("'0'::numeric"))
    backorder_qty = Column(Numeric(15, 5), nullable=False, server_default=text("'0'::numeric"))
    inventory_order_qty = Column(Numeric(15, 5), nullable=False, server_default=text("'0'::numeric"))
    inventory_committed_qty = Column(Numeric(15, 5), nullable=False, server_default=text("'0'::numeric"))
    inventory_backorder_qty = Column(Numeric(15, 5), nullable=False, server_default=text("'0'::numeric"))
    serialized_qty = Column(Numeric(11, 0), nullable=False, server_default=text("'0'::numeric"))
    retail_price = Column(Numeric(15, 5), nullable=False, server_default=text("'0'::numeric"))
    unit_price = Column(Numeric(15, 5), nullable=False, server_default=text("'0'::numeric"))
    status = Column(SmallInteger)
    price_matrix_id = Column(Integer)
    price_matrix_promo_code = Column(String(25))
    price_matrix_score = Column(SmallInteger)
    current_cost = Column(Numeric(15, 5), nullable=False, server_default=text("'0'::numeric"))
    average_cost = Column(Numeric(15, 5), nullable=False, server_default=text("'0'::numeric"))
    standard_cost = Column(Numeric(15, 5), nullable=False, server_default=text("'0'::numeric"))
    user_cost = Column(Boolean)
    tax_applicable = Column(Boolean, nullable=False, server_default=text("'{f,f,f,f}'::boolean[]"))
    partial_tax = Column(Boolean, server_default=text("false"))
    levy_code = Column(String(3))
    levy_amount = Column(Numeric(9, 3), nullable=False, server_default=text("'0'::numeric"))
    levy_tax_applicable = Column(Boolean, nullable=False, server_default=text("'{f,f,f,f}'::boolean[]"))
    discountable = Column(Boolean)
    line_disc = Column(Numeric(5, 2), nullable=False, server_default=text("'0'::numeric"))
    line_disc_amt = Column(Numeric(15, 2), nullable=False, server_default=text("'0'::numeric"))
    required_date = Column(Date)
    ref_no = Column(String(20))
    vendor_no = Column(String(20))
    po_number = Column(String(10))
    employee_no = Column(String(6))
    inventory_gl = Column(String(24))
    revenue_gl = Column(String(24))
    cost_gl = Column(String(24))
    upc_code = Column(String(40))
    job_no = Column(String(10))
    job_acct_no = Column(String(10))
    weight = Column(Numeric(15, 5))
    comment = Column(Text)
    udf_data = Column(HSTORE(Text()), server_default=text("''::hstore"))
    suppress = Column(Boolean, server_default=text("false"))

    def __repr__(self):
        return ('<SalesOrderItem({0},{1},{2},{3},{4},{5},{6},{7},{8},{9})>') \
                    .format(self.id, 
                            self.order_no,
                            self.part_no,
                            self._created,
                            self.description,
                            self.order_qty,
                            self.unit_price,
                            self.retail_price,
                            self.vendor_no,
                            self.sequence)
