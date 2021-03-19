from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, Numeric, String, Table, Text, text, BigInteger, Date, SmallInteger, UniqueConstraint, Index
from sqlalchemy.dialects.postgresql import UUID, ARRAY, HSTORE, JSONB
from sqlalchemy.orm import relationship
from ..database import Base

class Customer(Base):
    __tablename__ = 'customers'

    _dbversion = Column(Integer)
    _modified = Column(DateTime)
    _modified_by = Column(String(3))
    _created = Column(DateTime)
    _created_by = Column(String(3))
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
    dflt_ship_to = Column(String(20))
    last_pmt_date = Column(Date)
    upload = Column(Boolean, nullable=False)
    last_modified = Column(DateTime)
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
    bank_institution = Column(String(3))
    bank_transit = Column(String(5))
    bank_account = Column(String(31))
    levy_exempt = Column(Boolean, nullable=False, server_default=text("false"))
    surcharge_exempt = Column(Boolean, nullable=False, server_default=text("false"))
    udf_data = Column(JSONB(astext_type=Text()), server_default=text("'{}'::jsonb"))
    payment_provider_id = Column(String)
    sales_tax_provider_entity_code = Column(String)
    
    def __repr__(self):
        return ('<Customer({0},{1},{2},{3},{4},{5},{6})>') \
                    .format(self.id, 
                            self.cust_no,
                            self.name,
                            self.status,
                            self._modified,
                            self._created,
                            self.last_modified)