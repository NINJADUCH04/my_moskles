from fastapi import FastAPI ,  Query
from typing import Annotated
app = FastAPI()

@app.get("/items/")
async def read_items (q : str | None = Query (default=None, max_length= 5)  ) : 
     results = {"items" : [{"items_id" : "Foo"} , {"item_id" : "Bar"}]}
     if q :
          results.update({"q" : q })
    
     return results
