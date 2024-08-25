from pydantic import BaseModel
from datetime import datetime

class Row(BaseModel):
    date: datetime
    devId: str
    humidity: float
    alcConc: float  
    temperature: float
    distance: float