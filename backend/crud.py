from sqlalchemy.orm import Session

import models, schemas

def create_spot(db: Session, spot: schemas.SpotCreate):
    db_spot = models.Spot(map_id=spot.map_id, point_x=spot.point_x, point_y=spot.point_y, clip=spot.clip, bait=spot.bait)
    db.add(db_spot)
    db.commit()
    db.refresh(db_spot)
    return db_spot

def get_spot(db: Session, spot_id: int):
    return db.query(models.Spot).filter(models.Spot.id == spot_id).one()

def get_spots_per_map(db: Session, map_id: int):
    return db.query(models.Spot).filter(models.Spot.map_id == map_id)

def update_spot(db: Session, old_spot_id: int, new_spot: schemas.SpotUpdate):
    db_spot = db.query(models.Spot).filter(models.Spot.id == old_spot_id).one()
    if db_spot:
        update_data = new_spot.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_spot, key, value)
        db.commit()
        db.refresh(db_spot)
    return db_spot

def delete_spot(db: Session, spot: schemas.SpotDelete):
    db.delete(spot)
    db.commit()
    return