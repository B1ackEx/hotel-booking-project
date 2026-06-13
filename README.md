# 🏨 Hotel Booking System (FastAPI + MongoDB Atlas)

A modern full-stack **Hotel Booking Web Application** built using **FastAPI**, **HTML/CSS**, and **MongoDB Atlas**.  
Users can easily submit hotel booking details through a stylish form, and all data is securely stored in a cloud database.

---

## ✨ Features

- 📝 Beautiful responsive booking form
- ⚡ FastAPI high-performance backend
- ☁️ MongoDB Atlas cloud database integration
- 🔐 Secure environment variable configuration
- 📡 REST API endpoint for bookings
- 🌐 Fully deployment-ready (Vercel compatible)

---

## 🛠 Tech Stack

- **Frontend:** HTML5, CSS3  
- **Backend:** FastAPI (Python)  
- **Database:** MongoDB Atlas (Cloud NoSQL)  
- **Server:** Uvicorn  
- **Deployment:** Vercel  

---

## 📁 Project Structure


hotel-booking-project/
│
├── main.py
├── database.py
├── requirements.txt
├── .env
│
├── static/
│ ├── index.html
│ └── style.css
│
└── README.md


---

## 🚀 How to Run Locally

### 1️⃣ Clone the repository
```bash
git clone <your-repo-url>
cd hotel-booking-project

2️⃣ Create virtual environment
python -m venv .venv
.venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Setup environment variables

Create a .env file in root directory:
MONGO_URL=your_mongodb_atlas_connection_string

5️⃣ Run the server
uvicorn main:app --reload

Open in browser:

http://127.0.0.1:8000
📡 API Endpoint
➤ POST /book

This endpoint receives booking form data and stores it in MongoDB.

📦 Database Schema
{
  "full_name": "John Doe",
  "email": "john@email.com",
  "phone": "123456789",
  "check_in": "2026-06-15",
  "check_out": "2026-06-18",
  "room_type": "Deluxe",
  "guests": 2,
  "special_requests": "Near window"
}

🌐 Deployment (Vercel)
Steps:
Push project to GitHub
Import repository in Vercel
Add environment variable:
MONGO_URL
Click Deploy
Done 🚀
```

🎯 What I Learned

Building REST APIs using FastAPI Connecting Python with MongoDB Atlas Handling HTML form submissions Structuring full-stack projects Deploying real-world applications

## 👨‍💻 Author

M. Waleed Ishaq - F2024408217
OSSD Y9 Assignment
University of Management and Technology
