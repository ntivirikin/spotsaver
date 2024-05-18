from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models,schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Depends function
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Send spot information to the map
@app.post("/maps/", response_model=schemas.Spot)
def post_map(spot: schemas.SpotCreate, db: Session = Depends(get_db)):
    # Check if map_name is a part of map_names list
    return crud.create_spot(db, spot)

# Send the map name to the database and retrieve the information related (all spots with MapName == map_name)
@app.get("/maps/{map_id}", response_model=list[schemas.Spot]) # This should return a list of schemas.Spot
def read_map(map_id: int, db: Session = Depends(get_db)):
    return crud.get_spots_per_map(db, map_id)

@app.patch("/spots/{spot_id}")
def update_spot(spot_id: int, new_spot: schemas.SpotUpdate, db: Session = Depends(get_db)):
    db_spot = crud.get_spot(db, spot_id)
    if db_spot is None:
        raise HTTPException(status_code=400, detail="That spot does not exist!")
    return crud.update_spot(db, spot_id, new_spot)

# Delete the specified spot from the database
@app.delete("/spots/{spot_id}")
def delete_spot(spot_id: int, db: Session = Depends(get_db)):
    db_spot = crud.get_spot(db, spot_id)
    if db_spot is None:
        raise HTTPException(status_code=400, detail="That spot does not exist!")
    return crud.delete_spot(db, db_spot)