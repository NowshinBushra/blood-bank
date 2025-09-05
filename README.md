# 🩸 Blood Bank BD - A DRF Project

The Blood Bank aims to provide an intuitive and accessible platform, fostering a 
streamlined connection between blood donors and individuals requiring blood. Its 
goal is to enhance the blood donation experience, ensuring a smooth and 
effective process for both donors and recipients.

## Live Link
* [Backend Project Swagger Documentation Live Link](https://docs.github.com/en/github/writing-on-github)


## 🚀 Features
* **Authentication and Authorization**
* **Blood Requests Management** - CRUD Operation for blood requests. 
* **Donation History** - Users Donation History
* **Donor details** - Users can see all available donors


## 🛠️ Tech Stack
- **Backend:** Django, Django REST Framework
- **Authentication:** Djoser + JWT
- **Database:** SQLite (default), Supabase
- **Filtering & Search:** `django-filter`, DRF SearchFilter/OrderingFilter
- **API Docs:** Swagger/OpenAPI (`drf-yasg`)
- **Deployment:** Vercel

## 📂 Project Structure

* **blood-bank/**
* │── blood_bank/ # Project settings
* │── users/ # Custom User model & authentication
* │── blood_request/ # Blood request CRUD
* │── donation/ # Donation records & status updates
* │── api/ # API routing
* │── requirements.txt
* │── manage.py



## 🖥️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/blood-bank.git
   cd blood-bank

2. **Create & activate virtual environment:**
    ```bash
    python -m venv venv
    source venv/Scripts/activate  # On Windows (bash) 
    source venv/bin/activate    # On Mac

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt

4. **Run migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate

5. **Create a superuser:**
    ```bash
    python manage.py createsuperuser

6. **Run development server:**
    ```bash
    python manage.py runserver

7. **Open API docs in browser:**
    ```arduino
    http://127.0.0.1:8000/swagger/
    


## 🔑 API Endpoints

| Method | Endpoint                          | Description                                | Access        |
|--------|-----------------------------------|--------------------------------------------|---------------|
| **Auth** |
| POST   | `/auth/users/`                    | Register a new user                        | Public        |
| POST   | `/auth/jwt/create/`               | Login with email & password                | Public        |
| POST   | `/auth/jwt/refresh/`              | Refresh access token                       | Public        |
| **Blood Requests** |
| GET    | `/blood_requests/`                | List all blood requests                    | Authenticated |
| POST   | `/blood_requests/`                | Create a new blood request                 | Authenticated |
| GET    | `/blood_requests/my_requests/`    | View requests created by logged-in user    | Authenticated |
| PATCH  | `/blood_requests/{id}/`           | Update a request (creator only)            | Owner/Admin   |
| DELETE | `/blood_requests/{id}/`           | Delete a request (creator only)            | Owner/Admin   |
| **Donations** |
| GET    | `/donations/`                     | List all donations                         | Authenticated |
| POST   | `/donations/`                     | Accept a blood request (become donor)      | Authenticated |
| PATCH  | `/donations/{id}/update_status/`  | Update donation status                     | Admin Only    |
| POST   | `/donations/{id}/cancel/`         | Cancel a donation                          | Donor/Admin   |
| **Donors** |
| GET    | `/donors/`                        | List all available donors                  | Public        |
| GET    | `/donors/?blood_group=O+`         | Filter donors by blood group               | Public        |
| GET    | `/donors/?is_available=true`      | Filter donors by availability              | Public        |


### 📌 Future Improvements

- Payment gateway (Stripe/SSLCommerz).
- Push notifications for urgent requests.
- Geo-location based donor matching.
- Frontend integration (React/Next.js).

