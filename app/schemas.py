from pydantic import BaseModel

class TestCreate(BaseModel):
    nom: str
    fan: str
    tavsif: str
    public: bool

class TestDelete(BaseModel):
    test_id: str