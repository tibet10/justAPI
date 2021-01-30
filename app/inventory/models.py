from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, Numeric, String, Table, Text, text, BigInteger, Date, SmallInteger, UniqueConstraint, Index
from sqlalchemy.dialects.postgresql import UUID, ARRAY, HSTORE
from sqlalchemy.orm import relationship
from ..database import Base

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
    levy_code = Column(String(3))
    lot_numbered = Column(Boolean, nullable=False, server_default=text("false"))
    duty_perc = Column(Numeric(7, 2))
    freight_perc = Column(Numeric(7, 2))
    std_cost = Column(Numeric(15, 5))
    last_serial = Column(String(40))
    dflt_expiry_days = Column(Integer)
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
        return ('<Inventory({0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13})>') \
                    .format(self.id, 
                            self.product_code,
                            self.whse,
                            self.part_no, 
                            self.description,
                            self.alt_part_no,
                            self.extended_description,
                            self.min_buy_qty,
                            self.purchase_qty,
                            self._created,
                            self._modified,
                            self._created_by,
                            self._modified_by,
                            self.hold)

class InventoryUom(Base):
    __tablename__ = 'inventory_uoms'
    __table_args__ = (
        Index('inventory_uoms_inventory_id_uom_idx', 'inventory_id', 'uom', unique=True),
        Index('inventory_uoms_whse_part_no_uom_idx', 'whse', 'part_no', 'uom', unique=True)
    )

    id = Column(Integer, primary_key=True, server_default=text("nextval('inventory_uoms_id_seq'::regclass)"))
    inventory_id = Column(ForeignKey('inventory.id', ondelete='CASCADE'), nullable=False)
    whse = Column(String(6), nullable=False)
    part_no = Column(String(34), nullable=False)
    uom = Column(String(10))
    description = Column(String(80))
    qty_factor = Column(Numeric(11, 5))
    direct_factor = Column(Boolean)
    allow_fractional_qty = Column(Boolean)
    buy_uom = Column(Boolean)
    sell_uom = Column(Boolean)
    whse_location = Column(String(20), nullable=False, server_default=text("''::character varying"))
    weight = Column(Numeric(11, 5))
    sell_prices = Column(ARRAY(Numeric(precision=15, scale=5)), nullable=False, server_default=text("'{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}'::numeric[]"))
    use_price_factor = Column(Boolean, nullable=False)
    price_factor = Column(Numeric(11, 5))
    _dbversion = Column(Integer)
    _modified = Column(DateTime)
    _modified_by = Column(String(3))
    _created = Column(DateTime)
    _created_by = Column(String(3))

    inventory = relationship('Inventory')   


    def __repr__(self):
        return ('<InventoryUom({0},{1},{2},{3},{4},{5},{6},{7},{8},{9})>') \
                    .format(self.id, 
                            self.inventory_id,
                            self.whse,
                            self.part_no, 
                            self.uom,
                            self.sell_prices,
                            self._created,
                            self._modified,
                            self._created_by,
                            self._modified_by)