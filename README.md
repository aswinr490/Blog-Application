Simple Blog Application
This project is a simple blog application built using Django. It allows users to create, edit, delete, and view blog posts with rich text editing support via django-ckeditor.

Table of Contents
Features
Installation
Setup
Running the Application
Running Tests
Usage
License

Features
Create, edit, and delete blog posts.
View a list of all blog posts.
Rich text editing for blog content using django-ckeditor.
Basic unit testing for views.

Installation
Follow these steps to install and set up the project on your local machine:

Prerequisites
Ensure you have the following installed:

Python 3.x
pip (Python package installer)
Virtualenv (optional but recommended)

Clone the Repository
Clone this repository to your local machine using the following command:

git clone <repository-url>
cd blog_project

Set Up a Virtual Environment (Optional but Recommended)
To create and activate a virtual environment:

python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

Install Dependencies
Install the required Python packages using pip:

pip install -r requirements.txt

If requirements.txt is not available, you can manually install the necessary packages:
pip install django django-ckeditor

Setup
Database Migrations
Run the following commands to apply database migrations:
python manage.py makemigrations
python manage.py migrate

Create a Superuser (Optional)
To access the Django admin panel, create a superuser account:
python manage.py createsuperuser

Static Files Collection
If you plan to deploy the application or use static files in production, collect the static files:


Running the Application
To start the development server, run:
python manage.py runserver

Open your web browser and navigate to   http://127.0.0.1:8000/
 to access the application.

Running Tests
To run the unit tests:
python manage.py test
This will run the tests defined in blog/tests.py and output the results.

Usage
Create a Post: Click on the "New Post" link on the homepage to create a new blog post.
Edit a Post: On the post detail page, click the "Edit" button to modify the content.
Delete a Post: On the post detail page, click the "Delete" button to remove the post.
