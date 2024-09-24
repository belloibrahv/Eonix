# Eonix

## Description
Eonix is a career exploration and learning platform designed to make career guidance accessible to everyone. The platform enables users to browse various career paths, select relevant courses, access high-quality resources, and take assessments to test their knowledge. The backend is built with Django and Django Rest Framework (DRF), with a focus on API usability for both mobile and web applications.

## Why? (Motivation/Goal/Problem to solve)
The motivation behind Eonix stems from the lack of centralized and accessible career information, especially for individuals looking to enter or transition within different industries. Many people struggle with finding relevant career resources or understanding which skills are necessary for a specific career path. Eonix solves this by offering curated paths, courses, and assessments to guide users on their career journey.

## Quick Start
To get Eonix running on your local machine, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/belloibrahv/Eonix
   cd Eonix
   ```

2. Set up a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pipenv install
   ```

4. Apply database migrations
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Run the application:
   ```bash
   python manage.py runserver
   ```

## Usage
The primary functionalities include:

- **Browse Career Paths:** Users can explore various career paths and see the skills and courses recommended for each path.
- **Course Selection:** Users can enroll in courses relevant to their chosen career paths.
- **Assessments:** Users can take assessments to evaluate their progress and knowledge.
- **Filtering:** Filter courses or topic based on completion status (completed, incomplete, all).

API Endpoints:
- `/api/careers/`: Get a list of career paths.
- `/api/courses/`: List courses and filter by completion status.
  - `/api/courses/?query=completed`: Get completed courses.
  - `/api/courses/?query=in-complete`: Get incomplete courses.
  - `/api/courses/?query=all`: Get all courses.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes. Make sure to follow the contribution guidelines listed in the `CONTRIBUTING.md` file.
