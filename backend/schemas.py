from pydantic import BaseModel

class SpotBase(BaseModel):
    map_id: int
    point_x: int
    point_y: int
    clip: int
    bait: str

    # {"map": "Mosquito Lake", 
    #  "coords": (50, 60)
    #  "clip": 10
    #  "bait": "Nightcrawler"}

class SpotCreate(SpotBase):
    pass

class SpotUpdate(SpotBase):
    pass

class SpotDelete(SpotBase):
    pass

class Spot(SpotBase):
    id: int

    class Config:
        orm_mode = True