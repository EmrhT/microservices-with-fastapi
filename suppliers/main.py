from typing import List

from fastapi import FastAPI, Header
from tortoise.contrib.fastapi import register_tortoise

from models import Supplier_Pydantic, SupplierIn_Pydantic, Suppliers

app = FastAPI()


@app.get('/api/suppliers', response_model=List[Supplier_Pydantic])
async def get_suppliers():
    return await Supplier_Pydantic.from_queryset(Suppliers.all())


@app.post('/api/suppliers', response_model=Supplier_Pydantic)
async def create_supplier(supplier: SupplierIn_Pydantic,
                      request_user_id: str = Header(None)):
    data = supplier.dict()
    data.update({'created_by': request_user_id})

    supplier_obj = await Suppliers.create(**data)
    return await Supplier_Pydantic.from_tortoise_orm(supplier_obj)


register_tortoise(
    app,
    db_url='sqlite://:memory:',
    modules={'models': ['models']},
    generate_schemas=True,
    add_exception_handlers=True,
)
