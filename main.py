from datetime import datetime, timedelta
import httpx
from fastapi import FastAPI, HTTPException

app = FastAPI()

# Aaj se theek 5 din baad ki expiry date automatic set ho jayegi
EXPIRY_DATE = datetime.now() + timedelta(days=5)

# Original APIs ke base URLs
BASE_URL = "https://api.osintxc.com"


def check_expiry():
  if datetime.now() > EXPIRY_DATE:
    raise HTTPException(
        status_code=403,
        detail=(
            "Aapki API ki validity khatam ho chuki hai! Contact Admin:"
            " @VASHUDEVELOPER"
        ),
    )


@app.get("/num")
async def proxy_num(number: str = None, key: str = None):
  check_expiry()
  if not number:
    raise HTTPException(
        status_code=400, detail="Query parameter 'number' zarouri hai."
    )

  async with httpx.AsyncClient() as client:
    try:
      response = await client.get(
          f"{BASE_URL}/num?number={number}&key={key}", timeout=10.0
      )
      data = response.json()
    except Exception as e:
      raise HTTPException(
          status_code=500, detail=f"Original API error: {str(e)}"
      )

  # Purana credit/owner hata kar apna developer tag lagana
  if "credit" in data:
    del data["credit"]
  data["developer"] = "@VASHUDEVELOPER"
  return data


@app.get("/email")
async def proxy_email(value: str = None, key: str = None):
  check_expiry()
  if not value:
    raise HTTPException(
        status_code=400, detail="Query parameter 'value' zarouri hai."
    )

  async with httpx.AsyncClient() as client:
    try:
      response = await client.get(
          f"{BASE_URL}/email?value={value}&key={key}", timeout=10.0
      )
      data = response.json()
    except Exception as e:
      raise HTTPException(
          status_code=500, detail=f"Original API error: {str(e)}"
      )

  if "credit" in data:
    del data["credit"]
  data["developer"] = "@VASHUDEVELOPER"
  return data


@app.get("/aadhaar")
async def proxy_aadhaar(value: str = None, key: str = None):
  check_expiry()
  if not value:
    raise HTTPException(
        status_code=400, detail="Query parameter 'value' zarouri hai."
    )

  async with httpx.AsyncClient() as client:
    try:
      response = await client.get(
          f"{BASE_URL}/aadhaar?value={value}&key={key}", timeout=10.0
      )
      data = response.json()
    except Exception as e:
      raise HTTPException(
          status_code=500, detail=f"Original API error: {str(e)}"
      )

  if "credit" in data:
    del data["credit"]
  data["developer"] = "@VASHUDEVELOPER"
  return data
  
