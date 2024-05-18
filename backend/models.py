from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

from database import Base

# Keep this around for (possibly) later
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __composite_values__(self):
        return self.x, self.y
    
    def __repr__(self):
        return f"Point(x={self.x!r}, y={self.y!r})"

class Spot(Base):
    __tablename__ = "spots"

    id = Column(Integer, primary_key=True)
    map_id = Column(Integer)
    point_x = Column(Integer)
    point_y = Column(Integer)
    clip = Column(Integer)
    bait = Column(String)