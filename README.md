🌍 Peer-to-Peer International Delivery Platform
This is a Django-based backend API for a peer-to-peer international delivery service. It connects travelers moving between countries with requesters who need goods delivered from those countries.

✈️ Project Overview
This platform enables:

Travelers to create travel plans and offer to carry items.

Requesters to post delivery requests for items they want from other countries.

Secure matching of travelers and requesters.

Authentication, email verification, and profile management.

🛠️ Tech Stack
Backend Framework: Django, Django REST Framework (DRF)

Database: PostgreSQL

Authentication: JWT (JSON Web Token) with email verification

Environment: Python 3.10+, Django 4+

Deployment: Docker-ready (optional)

📦 Key Features
User Registration & Login with Email Verification

JWT Authentication

Traveler Route Planning

Delivery Request Posting

Matching Travelers to Delivery Requests

Profile Update (including passport or ID verification)

Secure Transactions (future scope)

📁 Folder Structure
peer2peer_delivery/
│
├── delivery/               # Core app logic
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
│
├── user_account/           # Custom user model & auth
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
│
├── config/                 # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── requirements.txt
🔐 Authentication Endpoints
Method	Endpoint	Description
POST	/api/auth/signup/	Register a new user
POST	/api/auth/login/	Login and receive JWT
POST	/api/auth/logout/	Logout and invalidate token
GET	/api/auth/verify/	Email verification

📦 Delivery & Travel APIs
Method	Endpoint	Description
POST	/api/travels/	Create a new travel plan
GET	/api/travels/	List all available travel plans
POST	/api/requests/	Post a delivery request
GET	/api/requests/	View open delivery requests
PUT	/api/profile/	Update user profile
GET	/api/matches/	See matched traveler-request pairs
▶️ Getting Started
Clone the repo

git clone https://github.com/yourusername/peer2peer-delivery.git
cd peer2peer-delivery
Create virtual environment

python -m venv venv
source venv/bin/activate
Install dependencies

pip install -r requirements.txt
Apply migrations and run

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
🧪 Testing with Postman
You can test the APIs using Postman:

Import the API collection (.json file) or manually set endpoints.

Register a user using /api/auth/signup/.

Check your email inbox (if configured) for a verification link.

Login to receive a JWT token.

Use that token in Authorization: Bearer <token> for further requests.

📌 To Do
 Add rating system for travelers and requesters

 Add payment integration

 Add real-time chat

 Deploy on Render/Heroku/DigitalOcean

🤝 Contributing
Fork this repo

Create a feature branch: git checkout -b feature/your-feature

Commit your changes: git commit -m 'Add feature'

Push to your branch: git push origin feature/your-feature

Create a pull request

