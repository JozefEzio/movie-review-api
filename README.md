# Movie Review API

A Django REST Framework API for managing movies, reviews, and user interactions.

## 🚀 Features

- **Movies Management**: CRUD operations for movies with genres
- **Review System**: Users can rate and review movies (1-10 scale)
- **Like System**: Users can like reviews
- **Authentication**: Token-based authentication with user registration
- **Filtering & Search**: Advanced filtering, searching, and ordering
- **Nested Routing**: Reviews are nested under movies for better organization
- **CORS Support**: Ready for frontend integration

## 🔧 Issues Fixed

The following problems have been resolved:

1. **Missing Nested Routing**: Added proper nested routing for reviews under movies
2. **Model Validation**: Added rating validation (1-10) and unique constraints
3. **Duplicate Prevention**: Users can only review a movie once and like a review once
4. **Missing Dependencies**: Added CORS headers and nested routers support
5. **Serializer Improvements**: Enhanced serializers with computed fields and validation
6. **Password Security**: Improved user registration with password confirmation
7. **API Structure**: Better organization with nested endpoints

## 📋 Requirements

- Python 3.8+
- Django 5.2.5+
- Django REST Framework 3.14.0+
- Django CORS Headers 4.0.0+
- DRF Nested Routers 0.93.4+

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd movie-review-api
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the server**
   ```bash
   python manage.py runserver
   ```

## 🌐 API Endpoints

### Base URL: `http://localhost:8000/api/`

#### Authentication
- `POST /api/auth/register/` - User registration
- `POST /api/auth/token/` - Get authentication token

#### Movies
- `GET /api/movies/` - List all movies
- `POST /api/movies/` - Create a movie (admin only)
- `GET /api/movies/{id}/` - Get movie details
- `PUT /api/movies/{id}/` - Update movie (admin only)
- `DELETE /api/movies/{id}/` - Delete movie (admin only)
- `GET /api/movies/{id}/reviews/` - Get reviews for a specific movie

#### Reviews
- `GET /api/reviews/` - List all reviews
- `POST /api/reviews/` - Create a review (authenticated users)
- `GET /api/reviews/{id}/` - Get review details
- `PUT /api/reviews/{id}/` - Update review (owner only)
- `DELETE /api/reviews/{id}/` - Delete review (owner only)

#### Genres
- `GET /api/genres/` - List all genres
- `POST /api/genres/` - Create a genre (admin only)

#### Likes
- `GET /api/likes/` - List all likes
- `POST /api/likes/` - Like a review (authenticated users)

## 🔍 Advanced Features

### Filtering
- Filter movies by genre: `/api/movies/?genres=Action`
- Filter movies by release date: `/api/movies/?release_date=2024-01-01`

### Searching
- Search movies by title or description: `/api/movies/?search=avengers`

### Ordering
- Order movies by release date: `/api/movies/?ordering=-release_date`
- Order movies by title: `/api/movies/?ordering=title`

### Pagination
- Customize page size: `/api/movies/?page_size=20`
- Navigate pages: `/api/movies/?page=2`

## 📱 Usage Examples

### 1. User Registration
```bash
curl -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "securepass123",
    "password_confirm": "securepass123"
  }'
```

### 2. Get Authentication Token
```bash
curl -X POST http://localhost:8000/api/auth/token/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "password": "securepass123"
  }'
```

### 3. Create a Review (with token)
```bash
curl -X POST http://localhost:8000/api/reviews/ \
  -H "Authorization: Token YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{
    "movie": 1,
    "rating": 8,
    "comment": "Great movie! Highly recommended."
  }'
```

### 4. Get Movie Reviews
```bash
curl http://localhost:8000/api/movies/1/reviews/
```

## 🗄️ Database Models

### Movie
- `title`: Movie title (max 200 chars)
- `description`: Movie description
- `release_date`: Release date
- `genres`: Many-to-many relationship with Genre
- `created_at`: Creation timestamp
- `updated_at`: Last update timestamp

### Review
- `user`: Foreign key to User
- `movie`: Foreign key to Movie
- `rating`: Integer 1-10
- `comment`: Optional text comment
- `created_at`: Creation timestamp
- `updated_at`: Last update timestamp

### Genre
- `name`: Genre name (unique, max 100 chars)

### Like
- `user`: Foreign key to User
- `review`: Foreign key to Review
- `created_at`: Creation timestamp

## 🔒 Security Features

- **Password Validation**: Minimum 8 characters, confirmation required
- **Token Authentication**: Secure API access
- **Permission System**: Role-based access control
- **Unique Constraints**: Prevents duplicate reviews and likes
- **Input Validation**: Rating validation (1-10 scale)

## 🧪 Testing

Run the test script to verify API functionality:
```bash
python test_api.py
```

## 🚨 Important Notes

- **CORS is enabled for development** - Configure properly for production
- **Debug mode is enabled** - Disable for production
- **SQLite database** - Consider PostgreSQL for production
- **Secret key exposed** - Generate new secret key for production

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🆘 Support

If you encounter any issues:
1. Check the Django logs
2. Verify all dependencies are installed
3. Ensure migrations are applied
4. Check the API endpoints with the test script


