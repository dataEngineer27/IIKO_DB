from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, DateTime, Date, Boolean, BIGINT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from datetime import datetime
import uuid
import pytz

timezonetash = pytz.timezone("Asia/Tashkent")

Base = declarative_base()


class Categories(Base):
    __tablename__ = 'nomenclature_categories'
    id = Column(String, primary_key=True)  # UUID(as_uuid=True)
    deleted = Column(Boolean)
    name = Column(String)
    last_update = Column(DateTime(timezone=True), default=func.now())


class Groups(Base):
    __tablename__ = 'nomenclature_groups'
    id = Column(String, primary_key=True)  # UUID(as_uuid=True)
    deleted = Column(Boolean, nullable=True)
    parent_id = Column(String, nullable=True)  # UUID(as_uuid=True)
    name = Column(String, nullable=True)
    num = Column(String, nullable=True)
    code = Column(String, nullable=True)
    category_id = Column(String, nullable=True)  # UUID(as_uuid=True)
    accountingCategory_id = Column(String, nullable=True)  # UUID(as_uuid=True)
    departments_visibility = Column(ARRAY(String), nullable=True)  # UUID(as_uuid=True)
    last_update = Column(DateTime(timezone=True), default=func.now())


class Nomenclatures(Base):
    __tablename__ = 'nomenclatures'
    id = Column(String, primary_key=True)  # UUID(as_uuid=True)
    group_id = Column(String, nullable=True)  # UUID(as_uuid=True)
    category_id = Column(String, nullable=True)  # UUID(as_uuid=True)
    accounting_category = Column(String, nullable=True)  # UUID(as_uuid=True)
    name = Column(String, nullable=True)
    num = Column(String, nullable=True)
    code = Column(BIGINT, nullable=True)
    main_unit = Column(String, nullable=True)  # UUID(as_uuid=True)
    price = Column(DECIMAL, nullable=True)
    place_type = Column(String, nullable=True)  # UUID(as_uuid=True)
    included_in_menu = Column(Boolean, nullable=True)
    type = Column(String, nullable=True)
    unit_weight = Column(DECIMAL, nullable=True)
    last_update = Column(DateTime(timezone=True), default=func.now())


class Departments(Base):
    __tablename__ = 'departments'
    id = Column(String, primary_key=True)  # UUID(as_uuid=True)
    parent_id = Column(String, nullable=True)  # UUID(as_uuid=True)
    code = Column(String, nullable=True)
    name = Column(String, nullable=True)
    type = Column(String, nullable=True)
    tax_payer_id = Column(String, nullable=True)
    # is_added = Column(Integer, default=0)
    last_update = Column(DateTime(timezone=True), default=func.now())


class Stores(Base):
    __tablename__ = 'stores'
    id = Column(String, primary_key=True)  # UUID(as_uuid=True)
    department_id = Column(String, nullable=True)  # UUID(as_uuid=True)
    code = Column(String, nullable=True)
    name = Column(String, nullable=True)
    type = Column(String, nullable=True)
    last_update = Column(DateTime(timezone=True), default=func.now())
    # is_added = Column(Integer, default=0)


class StoreRemains(Base):
    __tablename__ = 'store_remains'
    id = Column(BIGINT, primary_key=True, index=True, autoincrement=True)
    store_id = Column(String, nullable=True)  # UUID(as_uuid=True)
    nomenclature_id = Column(String, nullable=True)  # UUID(as_uuid=True)
    datetime = Column(DateTime(timezone=True))
    amount = Column(DECIMAL, nullable=True)
    sum = Column(DECIMAL, nullable=True)
    last_update = Column(DateTime(timezone=True), default=func.now())


# class StoreIncomings(Base):
#     __tablename__ = 'store_incomings'
#     id = Column(BIGINT, primary_key=True, index=True, autoincrement=True)
#     # incoming_invoice_id = Column(UUID(as_uuid=True), nullable=True)
#     doc_number = Column(String, nullable=True)
#     incoming_date = Column(DateTime(timezone=True))
#     transaction_date = Column(DateTime(timezone=True))
#     counteragent_id = Column(UUID(as_uuid=True), nullable=True)
#     counteragent_type = Column(String, nullable=True)
#     store_name = Column(String, nullable=True)  # ForeignKey('stores.name')
#     # actual_amount = Column(DECIMAL, nullable=True)
#     # price = Column(DECIMAL, nullable=True)
#     # price_withoutVat = Column(DECIMAL, nullable=True)
#     sum = Column(DECIMAL, nullable=True)
#     measureunit = Column(String, nullable=True)  # ForeignKey('reference_units.name')
#     nomenclature_id = Column(UUID(as_uuid=True), nullable=True)  # ForeignKey('nomenclatures.id')
#     amount = Column(DECIMAL, nullable=True)
#     last_update = Column(DateTime(timezone=True), default=func.now())
#     # store = relationship('Stores', back_populates='incomings')
#     # store_fk = relationship('Stores', backref='store_name', uselist=False,
#     #                         foreign_keys="StoreIncomings.store_name")
#     # nomenclatures = relationship('Nomenclatures', back_populates='incomings')
#     # units = relationship('ReferenceUnits', back_populates='incomings')
#     # units_fk = relationship('ReferenceUnits', backref='measureunit_name', uselist=False,
#     #                         foreign_keys="StoreIncomings.measureunit")
#     # sendings = relationship('StoreSendings', back_populates='incomings')


# class StoreSendings(Base):
#     __tablename__ = 'store_sendings'
#     id = Column(BIGINT, primary_key=True, index=True, autoincrement=True)
#     outgoing_invoice_id = Column(UUID(as_uuid=True), nullable=True)
#     doc_number = Column(String, nullable=True)
#     incoming_date = Column(DateTime(timezone=True))
#     store_id = Column(UUID(as_uuid=True), nullable=True)  # ForeignKey('stores.id')
#     supplier_id = Column(UUID(as_uuid=True), nullable=True)
#     incominginvoice_id = Column(UUID(as_uuid=True), nullable=True)
#     nomenclature_id = Column(UUID(as_uuid=True), nullable=True)  # ForeignKey('nomenclatures.id')
#     price = Column(DECIMAL, nullable=True)
#     price_withoutVat = Column(DECIMAL, nullable=True)
#     amount = Column(DECIMAL, nullable=True)
#     sum = Column(DECIMAL, nullable=True)
#     last_update = Column(DateTime(timezone=True), default=func.now())
#     store = relationship('Stores', back_populates='sendings')
#     # incomings = relationship('StoreIncomings', back_populates='sendings')
#     # nomenclatures = relationship('Nomenclatures', back_populates='sendings')


class ReferenceUnits(Base):
    __tablename__ = 'reference_units'
    id = Column(String, primary_key=True)  # UUID(as_uuid=True)
    type = Column(String, nullable=True)
    deleted = Column(Boolean, nullable=True)
    code = Column(String, nullable=True)
    name = Column(String, nullable=True)


class DepartmentRevenue(Base):
    __tablename__ = 'department_revenue'
    id = Column(BIGINT, primary_key=True, index=True, autoincrement=True)
    department_id = Column(String, nullable=True)  # UUID(as_uuid=True)
    nomenclature_id = Column(String, nullable=True)  # UUID(as_uuid=True)
    date = Column(Date, nullable=True)
    sum = Column(DECIMAL, nullable=True)
    last_update = Column(DateTime(timezone=True), default=func.now())


class EmployeeRoles(Base):
    __tablename__ = 'employee_roles'
    id = Column(String, primary_key=True)  # UUID(as_uuid=True)
    code = Column(String, nullable=True)
    name = Column(String, nullable=True)
    deleted = Column(Boolean, nullable=True)
    last_update = Column(DateTime(timezone=True), default=func.now())


class Employees(Base):
    __tablename__ = 'employees'
    id = Column(String, primary_key=True)  # UUID(as_uuid=True)
    code = Column(String, nullable=True)
    name = Column(String, nullable=True)
    role_ids = Column(ARRAY(String), nullable=True)  # UUID(as_uuid=True)
    role_id = Column(String, nullable=True)  # UUID(as_uuid=True)
    role_codes = Column(ARRAY(String), nullable=True)
    role_code = Column(String, nullable=True)
    # department_id = Column(UUID(as_uuid=True), nullable=True)
    deleted = Column(Boolean, nullable=True)
    supplier = Column(Boolean, nullable=True)
    employee = Column(Boolean, nullable=True)
    client = Column(Boolean, nullable=True)
    representStore = Column(Boolean, nullable=True)
    last_update = Column(DateTime(timezone=True), default=func.now())


class ShiftList(Base):
    __tablename__ = 'shift_list'
    id = Column(String, primary_key=True)  # UUID(as_uuid=True)
    session_number = Column(Integer, nullable=True)
    fiscal_number = Column(Integer, nullable=True)
    cash_reg_number = Column(Integer, nullable=True)
    cash_reg_serial = Column(String, nullable=True)
    open_date = Column(DateTime, nullable=True)
    close_date = Column(DateTime, nullable=True)
    accepted_date = Column(DateTime, nullable=True)
    manager_id = Column(String, nullable=True)  # UUID(as_uuid=True)
    responsible_user_id = Column(String, nullable=True)  # UUID(as_uuid=True)
    session_start_cash = Column(DECIMAL, nullable=True)
    pay_orders = Column(DECIMAL, nullable=True)
    sum_write_off_orders = Column(DECIMAL, nullable=True)
    sales_cash = Column(DECIMAL, nullable=True)
    sales_credit = Column(DECIMAL, nullable=True)
    sales_card = Column(DECIMAL, nullable=True)
    pay_in = Column(DECIMAL, nullable=True)
    pay_out = Column(DECIMAL, nullable=True)
    pay_income = Column(DECIMAL, nullable=True)
    cash_remain = Column(DECIMAL, nullable=True)
    cash_diff = Column(DECIMAL, nullable=True)
    session_status = Column(String, nullable=True)
    conception_id = Column(String, nullable=True)  # UUID(as_uuid=True)
    point_of_sale_id = Column(String, nullable=True)  # UUID(as_uuid=True)
    department_id = Column(String, nullable=True)  # UUID(as_uuid=True)
    last_update = Column(DateTime(timezone=True), default=func.now())
    # is_added = Column(Integer, default=0)


class Payments(Base):
    __tablename__ = 'payments'
    id = Column(BIGINT, primary_key=True, autoincrement=True)
    department_id = Column(String, nullable=True)  # UUID(as_uuid=True)
    shift_id = Column(String, nullable=True)  # UUID(as_uuid=True)
    order_type_id = Column(String, nullable=True)  # UUID(as_uuid=True)
    order_id = Column(String, nullable=True)  # UUID(as_uuid=True)
    order_num = Column(Integer, nullable=True)
    payment_type_id = Column(String, nullable=True)  # UUID(as_uuid=True)
    payment_id = Column(String, index=True, nullable=True)  # UUID(as_uuid=True)
    payment_type_group = Column(String, nullable=True)
    payment_type = Column(String, nullable=True)
    nomenclature_id = Column(String, nullable=True)  # UUID(as_uuid=True)
    nomenclature = Column(String, nullable=True)
    nomenclature_sum = Column(DECIMAL, nullable=True)
    nomenclature_amount = Column(DECIMAL, nullable=True)
    nomenclature_sum_with_discount = Column(DECIMAL, nullable=True)
    discount_sum = Column(DECIMAL, nullable=True)
    increase_sum = Column(DECIMAL, nullable=True)
    full_sum = Column(DECIMAL, nullable=True)
    measure_unit = Column(String, nullable=True)
    close_time = Column(DateTime(timezone=True))
    sold_with_dish_id = Column(String, nullable=True)  # UUID(as_uuid=True)
    sold_with_item_id = Column(String, nullable=True)  # UUID(as_uuid=True)
    cashier_id = Column(String, nullable=True)  # UUID(as_uuid=True)
    guest_num = Column(Integer, nullable=True)
    guest_card = Column(String, nullable=True)
    card_num = Column(String, nullable=True)
    bonus_card = Column(String, nullable=True)
    counteragent = Column(String, nullable=True)
    order_discount_type_id = Column(ARRAY(String), nullable=True)  # UUID(as_uuid=True)
    order_increase_type_id = Column(ARRAY(String), nullable=True)  # UUID(as_uuid=True)
    last_update = Column(DateTime(timezone=True), default=func.now())


# class ProductExpense(Base):
#     __tablename__ = 'product_expense'
#     id = Column(BIGINT, autoincrement=True, primary_key=True)
#     nomenclature_id = Column(UUID(as_uuid=True), nullable=True)  # ForeignKey('nomenclatures.id')
#     category_id = Column(UUID(as_uuid=True), nullable=True)  # ForeignKey('nomenclature_categories.id')
#     group_id = Column(UUID(as_uuid=True), nullable=True)  # ForeignKey('nomenclature_groups.id')
#     department_id = Column(UUID(as_uuid=True), nullable=True)  # ForeignKey('departments.id')
#     date = Column(DateTime(timezone=True))
#     name = Column(String)
#     quantity = Column(Float, nullable=True)
#     main_unit = Column(UUID, nullable=True)  # ForeignKey('reference_units.id')
#     last_update = Column(DateTime(timezone=True), default=func.now())
#     # category = relationship('Categories', back_populates='product_expense')
#     # groups = relationship('Groups', back_populates='product_expense')
#     # nomenclatures = relationship('Nomenclatures', back_populates='product_expense')
#     # department = relationship('Departments', back_populates='product_expense')
