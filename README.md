# **Eonix Backend**

A platform for career exploration and development through personalized learning paths.

## **Project Overview**

Eonix provides a backend system for managing careers, courses, and learning paths, enabling users to explore various career options and track their progress. The platform is designed to be fully backend-focused with APIs for career management.

## **Core Features**

- **Career Exploration**: Users can explore career options with detailed descriptions.
- **Admin Control**: Admins can create and update careers, while all users can view them.
- **Learning Paths and Topics**: Structured paths for learning, linking courses and topics (planned feature).
- **User Progress Tracking**: Track learning progress for registered users (planned feature).

## **Technical Specifications**

- **Backend Framework**: Django, Django Rest Framework (DRF)
- **Database**: SQLite (default setup, potential migration to PostgreSQL)
- **Architecture**: Monolithic structure

## **Getting Started**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/belloibrahv/Eonix.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd Eonix
   ```

3. **Install dependencies**:
   ```bash
   pipenv install
   ```

4. **Apply database migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

## **License**

Eonix is licensed under the MIT License. See [LICENSE](LICENSE) for more details.
