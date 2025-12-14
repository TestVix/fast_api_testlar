from fastapi import FastAPI, Depends
from .app.database import get_db
from .app.auth import verify_jwt
from .app.schemas import TestCreate, TestDelete
from .app.modals import Testlar
from sqlalchemy.orm import Session

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://127.0.0.1:8001",  # frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],   # GET, POST, OPTIONS ...
    allow_headers=["*"],   # Content-Type, Authorization ...
)

def get_uqique_test_id(db: Session):
    while True:
        import random
        number = random.randint(50000000, 90000000)
        
        existing_test = db.query(Testlar).filter(Testlar.id == number).first()
        if not existing_test:
            return number


@app.post("/testlar/add/")
def add_test(test : TestCreate, db: Session = Depends(get_db), token_data: dict = Depends(verify_jwt)):
    print("Token username:", token_data.get("sub"), flush=True)
    user_id = token_data.get("user_id")
    new_test = Testlar(
        test_id =get_uqique_test_id(db),
        nom=test.nom,
        fan=test.fan,
        tavsif=test.tavsif,
        public=test.public,
        user_id=user_id
    )
    db.add(new_test)
    db.commit()
    db.refresh(new_test)
    return {"message": "Test added successfully", "test": new_test}

@app.post("/testlarim/delete/")
def delete_test(data:TestDelete, db: Session = Depends(get_db), token_data: dict = Depends(verify_jwt)):
    print("Token username:", token_data.get("sub"), flush=True)
    user_id = token_data.get("user_id")
    test = db.query(Testlar).filter(Testlar.test_id == int(data.test_id), Testlar.user_id == user_id).first()
    if not test:
        return {"message": "Bunday test topilmadi yoki sizga tegishli emas", 'status': 'error'}
    
    db.delete(test)
    db.commit()
    return {"message": "O'chirildi"}