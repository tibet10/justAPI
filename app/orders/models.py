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

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, server_default=text("nextval('customers_id_seq'::regclass)"))
    cust_no = Column(String(20), unique=True)
    name = Column(String(60), index=True)
    currency = Column(String(3), nullable=False)
    reference = Column(String(60))
    last_invoice_no = Column(String(25))
    last_invoice_date = Column(Date)
    present_bal = Column(Numeric(15, 2))
    no_credit = Column(SmallInteger)
    credit_line = Column(Numeric(13, 0))
    disc_pct = Column(Numeric(5, 2))
    terms_code = Column(String(10))
    notes = Column(String(30))
    misc1 = Column(String(40))
    spec_handling = Column(String(1))
    statement_code = Column(Boolean, nullable=False)
    svce_chg_code = Column(Boolean, nullable=False)
    tax_prompt = Column(Boolean, nullable=False)
    dflt_ship_to = Column(String(20))
    last_pmt_date = Column(Date)
    upload = Column(Boolean, nullable=False)
    last_modified = Column(DateTime)
    last_sale_amt = Column(Numeric(15, 2))
    last_pmt_amt = Column(Numeric(15, 2))
    hold = Column(Boolean, nullable=False, server_default=text("false"))
    status = Column(String(1), nullable=False, server_default=text("'A'::character varying"))
    statement_type = Column(String(1))
    invoice_type = Column(String(1))
    po_no_required = Column(Boolean, nullable=False)
    ar_account = Column(String(24))
    last_year_sales = Column(ARRAY(Numeric(precision=15, scale=2)), nullable=False, server_default=text("'{0,0,0,0,0,0,0,0,0,0,0,0,0}'::numeric[]"))
    this_year_sales = Column(ARRAY(Numeric(precision=15, scale=2)), nullable=False, server_default=text("'{0,0,0,0,0,0,0,0,0,0,0,0,0}'::numeric[]"))
    next_year_sales = Column(ARRAY(Numeric(precision=15, scale=2)), nullable=False, server_default=text("'{0,0,0,0,0,0,0,0,0,0,0,0,0}'::numeric[]"))
    last_year_gp = Column(ARRAY(Numeric(precision=15, scale=2)), nullable=False, server_default=text("'{0,0,0,0,0,0,0,0,0,0,0,0,0}'::numeric[]"))
    this_year_gp = Column(ARRAY(Numeric(precision=15, scale=2)), nullable=False, server_default=text("'{0,0,0,0,0,0,0,0,0,0,0,0,0}'::numeric[]"))
    next_year_gp = Column(ARRAY(Numeric(precision=15, scale=2)), nullable=False, server_default=text("'{0,0,0,0,0,0,0,0,0,0,0,0,0}'::numeric[]"))
    avg_days_to_pay = Column(Numeric(15, 2))
    approved_by = Column(String(3))
    approved_date = Column(Date)
    color_text = Column(BigInteger, nullable=False, server_default=text("'0'::bigint"))
    color_back = Column(BigInteger, nullable=False, server_default=text("'16777215'::bigint"))
    website = Column(String(125))
    open_ord = Column(Numeric(15, 2))
    bank_institution = Column(String(3))
    bank_transit = Column(String(5))
    bank_account = Column(String(31))
    levy_exempt = Column(Boolean, nullable=False, server_default=text("false"))
    surcharge_exempt = Column(Boolean, nullable=False, server_default=text("false"))
    udf_data = Column(HSTORE(Text()), server_default=text("''::hstore"))
    provider_id = Column(String(32))
    _dbversion = Column(Integer)
    _modified = Column(DateTime)
    _modified_by = Column(String(3))
    _created = Column(DateTime)
    _created_by = Column(String(3))
    
    def __repr__(self):
        return ('<Customer({0},{1},{2},{3})>') \
                    .format(self.id, 
                            self.cust_no,
                            self.name,
                            self._created)

class Address(Base):
    __tablename__ = 'addresses'
    __table_args__ = (
        Index('addresses_link_table_link_no_addr_type_ship_id_idx', 'link_table', 'link_no', 'addr_type', 'ship_id', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('addresses_id_seq'::regclass)"))
    link_table = Column(String(4))
    link_no = Column(String(20), index=True)
    addr_type = Column(String(1))
    ship_id = Column(String(20), nullable=False, index=True)
    name = Column(String(60))
    address = Column(ARRAY(String(length=45)))
    city = Column(String(45))
    prov_state = Column(String(2))
    postal_zip = Column(String(16))
    country_code = Column(String(3))
    phone_type = Column(SmallInteger)
    phone = Column(String(30))
    fax_type = Column(SmallInteger)
    fax = Column(String(30))
    email = Column(String(254))
    webpage = Column(String(80))
    contact_name = Column(ARRAY(String(length=60)), nullable=False)
    contact_phone_type = Column(ARRAY(SmallInteger()), nullable=False)
    contact_phone = Column(ARRAY(String(length=30)), nullable=False)
    contact_fax_type = Column(ARRAY(SmallInteger()), nullable=False)
    contact_fax = Column(ARRAY(String(length=30)), nullable=False)
    contact_email = Column(ARRAY(String(length=254)), nullable=False)
    hold = Column(Boolean)
    sales_terr = Column(String(10))
    sales_terr_desc = Column(String(80))
    sales_person = Column(String(10))
    slspsn_name = Column(String(60))
    ship_code = Column(String(10))
    ship_desc = Column(String(60))
    dflt_whse = Column(String(6))
    rv_account = Column(String(24))
    sell_no = Column(SmallInteger)
    sales_tax_no = Column(ARRAY(SmallInteger()), nullable=False)
    sales_tax_exempt_no = Column(ARRAY(String(length=20)), nullable=False)
    native = Column(Boolean)
    ecommerce = Column(Boolean)
    billto_csp = Column(Boolean)
    udf_data = Column(HSTORE(Text()), server_default=text("''::hstore"))
    _dbversion = Column(Integer)
    _modified = Column(DateTime)
    _modified_by = Column(String(3))
    _created = Column(DateTime)
    _created_by = Column(String(3))

    def __repr__(self):
        return ('<Address({0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13})>') \
                    .format(self.id, 
                            self.city,
                            self.postal_zip, 
                            self.prov_state,
                            self.country_code,
                            self.email,
                            self.phone,
                            self._created,
                            self._modified,
                            self.name,
                            self.address,                            
                            self.addr_type,
                            self.fax,
                            self.sales_tax_no)

class Inventory(Base):
    __tablename__ = 'inventory'
    __table_args__ = (
        Index('inventory_whse_part_no_idx', 'whse', 'part_no', unique=True),
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('inventory_id_seq'::regclass)"))
    whse = Column(String(6), nullable=False)
    part_no = Column(String(34), nullable=False, index=True)
    description = Column(String(80))
    product_code = Column(String(10), index=True)
    hold = Column(SmallInteger)
    current_cost = Column(Numeric(15, 5))
    average_cost = Column(Numeric(15, 5))
    tax_flags = Column(Boolean, nullable=False, server_default=text("'{f,f,f,f}'::boolean[]"))
    tax_code = Column(SmallInteger)
    uom_purchase = Column(String(10))
    uom_inventory = Column(String(10))
    uom_sales = Column(String(10))
    current_po = Column(String(10))
    min_buy_qty = Column(Numeric(11, 0))
    po_due_date = Column(Date)
    discountable = Column(Boolean)
    serialized = Column(Boolean, nullable=False, server_default=text("false"))
    sales_acct = Column(SmallInteger)
    onhand_qty = Column(Numeric(15, 5))
    reorder_qty = Column(Numeric(15, 5))
    committed_qty = Column(Numeric(15, 5))
    backorder_qty = Column(Numeric(15, 5))
    purchase_qty = Column(Numeric(15, 5))
    alt_part_no = Column(String(40))
    misc_1 = Column(String(40))
    misc_2 = Column(Numeric(15, 5))
    type = Column(String(1), index=True)
    image_path = Column(String(261))
    upload = Column(Boolean)
    last_modified = Column(DateTime)
    allow_back_orders = Column(Boolean)
    allow_returns = Column(Boolean)
    preferred_vendor = Column(String(20))
    rebate_ab = Column(Boolean)
    rebate_bc = Column(Boolean)
    rebate_mb = Column(Boolean)
    rebate_nb = Column(Boolean)
    rebate_nl = Column(Boolean)
    rebate_nu = Column(Boolean)
    rebate_ns = Column(Boolean)
    rebate_nt = Column(Boolean)
    rebate_on = Column(Boolean)
    rebate_pe = Column(Boolean)
    rebate_qc = Column(Boolean)
    rebate_sk = Column(Boolean)
    rebate_yt = Column(Boolean)
    rebate_zz = Column(Boolean)
    pack_size = Column(Numeric(9, 3))
    color_text = Column(BigInteger, nullable=False, server_default=text("'0'::bigint"))
    color_back = Column(BigInteger, nullable=False, server_default=text("'16777215'::bigint"))
    chgn_int = Column(String(3))
    chgn_date = Column(Date)
    levy_code = Column(String(3))
    lot_numbered = Column(Boolean, nullable=False, server_default=text("false"))
    duty_perc = Column(Numeric(7, 2))
    freight_perc = Column(Numeric(7, 2))
    std_cost = Column(Numeric(15, 5))
    last_serial = Column(String(40))
    dflt_expiry_days = Column(Integer)
    non_standard = Column(Boolean)
    hs_code = Column(String(27))
    mfg_country = Column(String(3))
    rental_whse = Column(String(6))
    rental_part_no = Column(String(34))
    rental_description = Column(String(80))
    lot_consume_type = Column(SmallInteger)
    extended_description = Column(Text)
    last_year_qty = Column(Numeric(15, 5), server_default=text("'0'::numeric"))
    last_year_revenue = Column(Numeric(15, 5), server_default=text("'0'::numeric"))
    this_year_qty = Column(Numeric(15, 5), server_default=text("'0'::numeric"))
    this_year_revenue = Column(Numeric(15, 5), server_default=text("'0'::numeric"))
    next_year_qty = Column(Numeric(15, 5), server_default=text("'0'::numeric"))
    next_year_revenue = Column(Numeric(15, 5), server_default=text("'0'::numeric"))
    udf_data = Column(HSTORE(Text()), server_default=text("''::hstore"))
    last_count_date = Column(Date)
    last_count_qty = Column(Numeric(15, 5))
    last_count_variance = Column(Numeric(15, 5))
    show_options = Column(Boolean)
    _dbversion = Column(Integer)
    _modified = Column(DateTime)
    _modified_by = Column(String(3))
    _created = Column(DateTime)
    _created_by = Column(String(3))  



    def __repr__(self):
        return ('<Inventory({0},{1},{2},{3},{4})>') \
                    .format(self.id, 
                            self.whse,
                            self.part_no, 
                            self.description,
                            self.alt_part_no)                          

class SalesTax(Base):
    __tablename__ = 'sales_taxes'

    id = Column(Integer, primary_key=True, server_default=text("nextval('sales_taxes_id_seq'::regclass)"))
    tax_no = Column(SmallInteger, unique=True)
    name = Column(String(60))
    rate = Column(Numeric(7, 4))
    gl_account = Column(String(24))
    gl_credit_account = Column(String(24))
    short_name = Column(String(20))
    use_partial_rate = Column(Boolean)
    partial_rate = Column(Numeric(7, 4))
    freight = Column(Boolean, server_default=text("false"))
    surcharge = Column(Boolean, server_default=text("true"))
    include_landed = Column(Boolean, server_default=text("true"))
    udf_data = Column(HSTORE(Text()), server_default=text("''::hstore"))
    _dbversion = Column(Integer)
    _modified = Column(DateTime)
    _modified_by = Column(String(3))
    _created = Column(DateTime)
    _created_by = Column(String(3))


    def __repr__(self):
        return ('<SalesTax({0},{1},{2},{3},{4})>') \
                    .format(self.tax_no, 
                            self.name,
                            self.rate, 
                            self.gl_account,
                            self._created)  