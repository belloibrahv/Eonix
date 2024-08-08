# Eonix Backend

Learning Platform for Career Development and Skill Enhancement

## Features

* Profession Selection with details on demand, remote work possibilities, and required skills
* Personalized Learning Paths with structured topics and subtopics
* Study Resources and Assessments for each topic
* Randomized assessment questions and answers
* User Progress and Assessment Result Tracking

## Technical Specifications

* Backend Framework: Django, Django Rest Framework
* Database: MySQL (default Django setup, to be migrated to PostgreSQL)
* Architecture: Monolithic

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/belloibrahv/Eonix.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Eonix
   ```
3. Install dependencies:
   ```bash
   pipenv install
   ```
4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```
5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## License

Eonix is licensed under the MIT License. See [LICENSE](LICENSE) for details.
