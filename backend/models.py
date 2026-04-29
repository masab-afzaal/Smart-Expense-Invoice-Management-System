from sqlalchemy import Integer, Column, String, ForeignKey, DateTime, Text, Numeric
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    invoices = relationship("Invoice", back_populates="user")
    expenses = relationship("Expense", back_populates="user")

class Invoice(Base):

    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id") )
    invoice_number = Column(Integer, unique=True)
    date = Column(DateTime, default=datetime.now)
    total_amount = Column(Numeric(10, 2))

    user = relationship("User", back_populates="invoices")
    items = relationship("InvoiceItem", back_populates="invoice")

class InvoiceItem(Base):

    __tablename__ = "invoice_items"

    id = Column(Integer, primary_key=True)
    invoice_id = Column(Integer, ForeignKey("invoices.id"))
    description = Column(Text,)
    quantity = Column(Integer)
    unit_price = Column(Numeric(10, 2))

    invoice = relationship("Invoice", back_populates="items")

class Expense(Base):

    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    amount = Column(Numeric(10, 2))
    category = Column(String)
    date = Column(DateTime, default=datetime.now)

    user = relationship("User", back_populates="expenses")
