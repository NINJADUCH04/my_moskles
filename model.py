from transformers import pipeline 
from pydantic import BaseModel 
from fastapi import FastAPI , HTTPException


app = FastAPI()

classifier = pipeline ("sentiment-analysis")

class disc (BaseModel) : 
    items : str 



@app.post("/analyze-sentiment")
async def analyze_sentiment (item : disc ) : 
    try : 
        res = classifier(item.items) 
        return res
    except :
        raise HTTPException (status_code = 500 , detail = str (e))



def analyze (user_input):
    
    result = classifier (user_input)
    return result
