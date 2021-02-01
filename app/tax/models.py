
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, Numeric, String, Table, Text, text, BigInteger, Date, SmallInteger, UniqueConstraint, Index
from sqlalchemy.dialects.postgresql import UUID, ARRAY, HSTORE, JSONB
from sqlalchemy.orm import relationship
from ..database import Base

class SalesTax(Base):
    __tablename__ = 'sales_taxes'

    _dbversion = Column(Integer)
    _modified = Column(DateTime)
    _modified_by = Column(String(3))
    _created = Column(DateTime)
    _created_by = Column(String(3))
    id = Column(Integer, primary_key=True, server_default=text("nextval('sales_taxes_id_seq'::regclass)"))
    tax_no = Column(SmallInteger, unique=True)
    name = Column(String(60))
    rate = Column(Numeric(7, 4), nullable=False, server_default=text("'0'::numeric"))
    gl_account = Column(String(24))
    gl_credit_account = Column(String(24))
    short_name = Column(String(20))
    use_partial_rate = Column(Boolean)
    partial_rate = Column(Numeric(7, 4))
    freight = Column(Boolean, server_default=text("false"))
    surcharge = Column(Boolean, server_default=text("true"))
    include_landed = Column(Boolean, server_default=text("true"))
    udf_data = Column(JSONB(astext_type=Text()), server_default=text("'{}'::jsonb"))
    integrated = Column(Boolean)


    def __repr__(self):
        return ('<SalesTax({0},{1},{2},{3},{4})>') \
                    .format(self.tax_no, 
                            self.name,
                            self.rate, 
                            self.gl_account,
                            self._created)  