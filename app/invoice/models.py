from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, Numeric, String, Table, Text, text, BigInteger, Date, SmallInteger, UniqueConstraint, Index
from sqlalchemy.dialects.postgresql import UUID, ARRAY, HSTORE, JSONB
from sqlalchemy.orm import relationship
from ..database import Base


class SalesHistory(Base):
    __tablename__ = 'sales_history'

    _dbversion = Column(Integer)
    _modified = Column(DateTime)
    _modified_by = Column(String(3))
    _created = Column(DateTime)
    _created_by = Column(String(3))
    order_no = Column(String(10), index=True)
    order_date = Column(Date)
    invoice_no = Column(String(10), unique=True)
    invoice_date = Column(Date, index=True)
    cust_no = Column(String(20), index=True)
    cust_name = Column(String(60))
    cust_po_no = Column(String(20))
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
    currency_rate = Column(Numeric(13, 7), nullable=False, server_default=text("1"))
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
    udf_data = Column(JSONB(astext_type=Text()), server_default=text("'{}'::jsonb"))
    id = Column(Integer, primary_key=True, server_default=text("nextval('sales_history_id_seq'::regclass)"))
    trans_no = Column(String(10), index=True)
    was_standing_no = Column(String(10))
    user_weight = Column(Boolean)
    sales_tax_provider_id = Column(String)
    whse = Column(String(6))

    def __repr__(self):
        return ('<Invoice({0},{1},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12})>') \
                    .format(self.id, 
                            self.invoice_no,
                            self.invoice_date,
                            self.order_no,
                            self.division,
                            self.location,
                            self.profit_center,
                            self.order_date,
                            self.required_date,
                            self._created,
                            self._modified,
                            self._created_by,
                            self._modified_by)   