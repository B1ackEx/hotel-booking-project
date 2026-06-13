from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from database import bookings_collection

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


# homepage
@app.get("/")
def home():
    return FileResponse("static/index.html")


# booking endpoint
@app.post("/book")
async def book(
    full_name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    check_in: str = Form(...),
    check_out: str = Form(...),
    room_type: str = Form(...),
    guests: int = Form(...),
    special_requests: str = Form("")
):

    booking = {
        "full_name": full_name,
        "email": email,
        "phone": phone,
        "check_in": check_in,
        "check_out": check_out,
        "room_type": room_type,
        "guests": guests,
        "special_requests": special_requests
    }

    result = await bookings_collection.insert_one(booking)

    return {
        "success": True,
        "booking_id": str(result.inserted_id)
    }