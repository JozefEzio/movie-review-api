# 🎬 Movie Review API

A Django REST Framework (DRF) project where users can browse movies, write reviews, and rate them. This project demonstrates authentication, filtering, pagination, and CRUD operations with Django and DRF.

---

## 🚀 Features

- User authentication (Register/Login/Logout)
- Add, update, and delete movie reviews
- Rate movies (1–5 stars)
- Search, filter, and order movies
- Token-based authentication for secure API access
- Pagination for listing results
- Like/unlike movies
- Genre management

---

## 🛠️ Tech Stack

- **Backend:** Django, Django REST Framework
- **Database:** SQLite (default, can be changed to PostgreSQL/MySQL)
- **Auth:** Token Authentication + Session Authentication
- **Filtering:** `django-filter`
- **Deployment (optional):** Heroku / Render / PythonAnywhere

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Clone the repository
```bash
git clone https://github.com/JozefEzio/movie-review-api.git
cd movie-review-api
```

### Create and activate a virtual environment
```bash
# On Linux/Mac
python -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Apply migrations
```bash
python manage.py migrate
```

### Create a superuser (admin)
```bash
python manage.py createsuperuser
```

### Run the development server
```bash
python manage.py runserver
```

### Access the API
- API Base URL: `http://127.0.0.1:8000/api/`
- Admin Interface: `http://127.0.0.1:8000/admin/`

---

## 📌 API Endpoints

### Authentication
- `POST /api/auth/register/` - Register new user
- `POST /api/auth/token/` - Login & get token
- `GET /api/api-auth/` - DRF login/logout interface

### Movies
- `GET /api/movies/` - List all movies
- `GET /api/movies/{id}/` - Retrieve a single movie
- `POST /api/movies/` - Add new movie (admin only)
- `PUT /api/movies/{id}/` - Update movie (admin only)
- `DELETE /api/movies/{id}/` - Delete movie (admin only)

### Reviews
- `GET /api/reviews/` - List reviews
- `POST /api/reviews/` - Add review
- `PUT /api/reviews/{id}/` - Update review (owner only)
- `DELETE /api/reviews/{id}/` - Delete review (owner only)

### Likes
- `GET /api/likes/` - List likes
- `POST /api/likes/` - Like a movie
- `DELETE /api/likes/{id}/` - Unlike a movie

### Genres
- `GET /api/genres/` - List all genres
- `GET /api/genres/{id}/` - Retrieve a single genre
- `POST /api/genres/` - Add new genre (admin only)
- `PUT /api/genres/{id}/` - Update genre (admin only)
- `DELETE /api/genres/{id}/` - Delete genre (admin only)

---

## 🔐 Authentication

This API uses token-based authentication. To access protected endpoints:

1. Register a new user: `POST /api/auth/register/`
2. Get your token: `POST /api/auth/token/` with your credentials
3. Include the token in your requests:
   ```
   Authorization: Token your_token_here
   ```

---

## 📝 Usage Examples

### Register a new user
```bash
curl -X POST http://127.0.0.1:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpass123", "email": "test@example.com"}'
```

### Get authentication token
```bash
curl -X POST http://127.0.0.1:8000/api/auth/token/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpass123"}'
```

### Create a review (with token)
```bash
curl -X POST http://127.0.0.1:8000/api/reviews/ \
  -H "Authorization: Token your_token_here" \
  -H "Content-Type: application/json" \
  -d '{"movie": 1, "rating": 5, "comment": "Great movie!"}'
```

---

## 🗄️ Database Schema

The project includes the following models:
- **User** - Django's built-in User model
- **Movie** - Movie information (title, description, release date, etc.)
- **Review** - User reviews with ratings and comments
- **Like** - User likes for movies
- **Genre** - Movie genres

---

## 🚀 Deployment

### Local Development
The project is configured for local development with SQLite database. For production:

1. Change `DEBUG = False` in `settings.py`
2. Set a secure `SECRET_KEY`
3. Configure `ALLOWED_HOSTS`
4. Use a production database (PostgreSQL/MySQL)
5. Set up static file serving

### Environment Variables
Create a `.env` file for sensitive settings:
```
SECRET_KEY=your_secret_key_here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**JozefEzio** - [GitHub Profile](https://github.com/JozefEzio)

---

## 🙏 Acknowledgments

- Django REST Framework for the excellent API framework
- Django community for the robust web framework
- All contributors who help improve this project


