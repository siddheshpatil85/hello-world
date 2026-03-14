#pip install fastapi uvicorn
#To Run: PS D:\Profession\pythonProject\vsCode\hello-world\API> uvicorn recast:app --reload
#To Test 
# PS D:\Profession\pythonProject\vsCode\hello-world\API> PS D:\Profession\pythonProject\vsCode\hello-world> Invoke-RestMethod -Uri "http://127.0.0.1:8000/remap" -Method POST -Headers @{"Content-Type"="application/json"} -Body '{"col1": null, "col2": "", "col3": 123}' 
#col1  col2 col3
#----  ---- ----
#Test1       123
#Local_v1

from fastapi import FastAPI
from typing import Dict, Any

# This is the "app" that Uvicorn is looking for!
app = FastAPI()

def apply_remapping_rules(data: Dict[str, Any]) -> Dict[str, Any]:
    remapped_data = data.copy()
    
    # Rule 1: If 'col1' exists and is null, change it to 'Test1'
    if "col1" in remapped_data and remapped_data["col1"] is None:
        remapped_data["col1"] = "Test1"

    return remapped_data

@app.post("/remap")
async def remap_values(payload: Dict[str, Any]):
    processed_data = apply_remapping_rules(payload)
    return processed_data
