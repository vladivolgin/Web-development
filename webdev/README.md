# Hotel Booking Application

## Overview

This project is a hotel booking application built with **Flask** and **SQLAlchemy**. It allows users to view, create, update, and delete hotel bookings.

## Requirements

- **Python 3.x**
- **Flask**
- **Flask-SQLAlchemy**
- **Flask-WTF**
- **SQLite** (or any other database of your choice)

## Setup
Clone the Repository:
bash

git clone <repository-url>
cd <repository-folder>
Create a Virtual Environment:
bash

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Dependencies:
bash

pip install -r requirements.txt
Database Initialization: Run the following command to create the database and the necessary tables:
bash

python app.py

Running the Application

Start the Flask Development Server:
bash

flask run
By default, the application runs on http://127.0.0.1:5000/.
Access the Application: Open your web browser and navigate to http://127.0.0.1:5000/.
Features

Home Page: Displays a welcome message and links to other sections.
View All Bookings: Lists all current bookings with options to edit or delete.
Create a New Booking: A form to input new booking details.
Update Booking: Allows users to modify existing booking information.


