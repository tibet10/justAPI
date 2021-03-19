from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, Numeric, String, Table, Text, text, BigInteger, Date, SmallInteger, UniqueConstraint, Index
from sqlalchemy.dialects.postgresql import UUID, ARRAY, HSTORE, JSONB
from sqlalchemy.orm import relationship
from ..database import Base


class Address(Base):
    __tablename__ = 'addresses'
    __table_args__ = (
        Index('addresses_link_table_link_no_addr_type_ship_id_idx', 'link_table', 'link_no', 'addr_type', 'ship_id', unique=True),
    )

    _dbversion = Column(Integer)
    _modified = Column(DateTime)
    _modified_by = Column(String(3))
    _created = Column(DateTime)
    _created_by = Column(String(3))
    id = Column(Integer, primary_key=True, server_default=text("nextval('addresses_id_seq'::regclass)"))
    link_table = Column(String(4))
    link_no = Column(String(20), index=True)
    addr_type = Column(String(1))
    ship_id = Column(String(20), nullable=False, index=True)
    name = Column(String(60), nullable=False)
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
    ecommerce = Column(Boolean)
    udf_data = Column(JSONB(astext_type=Text()), server_default=text("'{}'::jsonb"))

    def __repr__(self):
        return ('<Address({0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14},{15},{16},{17},{18},{19})>') \
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
                            self.sales_tax_no,
                            self.ship_id,
                            self.sell_no,
                            self.contact_name,
                            self.contact_email,
                            self.contact_phone,
                            self.contact_fax)