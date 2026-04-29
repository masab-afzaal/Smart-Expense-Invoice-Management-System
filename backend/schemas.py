from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str

class InvoiceCreate(BaseModel):
    user_id: int
    invoice_number: int
    total_amount: float

class InvoiceResponse(BaseModel):
    id: int
    invoice_number: str
    total_amount: float

    class Config:
        from_attributes = True

class InvoiceItemCreate(BaseModel):
    invoice_id: int
    description: str
    quantity: int
    unit_price: float

class ExpenseCreate(BaseModel):
    amount: float
    category: str

class ExpenseResponse(BaseModel):
    id: int
    amount: float
    category: str

    class Config:
        from_attributes = True
