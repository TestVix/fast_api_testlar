from pydantic import BaseModel

class TestCreate(BaseModel):
    nom: str
    fan: str
    tavsif: str
    public: bool