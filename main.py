from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from database import bookings_collection

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


# HOME PAGE
@app.get("/")
def home():
    return FileResponse("static/index.html")


# BOOKING API
@app.post("/book")
async def book(
    full_name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    check_in: str = Form(...),
    check_out: str = Form(...),
    room_type: str = Form(...),
    guests: int = Form(...)
):

    booking = {
        "full_name": full_name,
        "email": email,
        "phone": phone,
        "check_in": check_in,
        "check_out": check_out,
        "room_type": room_type,
        "guests": guests
    }

    result = await bookings_collection.insert_one(booking)

    return {
        "success": True,
        "booking_id": str(result.inserted_id)
    }

import os

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))