from pydantic import BaseModel

from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator

class Suppliers(models.Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
    surname = fields.TextField()
    address = fields.TextField()
    created_by = fields.IntField()
    created_at = fields.DatetimeField(auto_now_add=True)


Supplier_Pydantic = pydantic_model_creator(Suppliers, name='Supplier')

class SupplierIn_Pydantic(BaseModel):
    name: str
    surname: str
    address: str
