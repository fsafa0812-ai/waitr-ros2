from dataclasses import dataclass
from typing import List 
@dataclass
class Order:
    order_id:int
    table_number:int
    items:List[str]
    priority:str = "Normal"
    status: str ="Pending"