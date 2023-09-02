from pydantic import BaseModel


class SupplierForm(BaseModel):
    name: str
    surname: str
    address: str



class SupplierResponse(BaseModel):
    id: int
    name: str
    surname: str
    address: str
    created_by: int
    created_at: str