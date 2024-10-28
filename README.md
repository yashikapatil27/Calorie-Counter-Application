# Calorie Counter Application
CIS552- Project Work for Summer 2024: Calorie Counter Application using MongoDB for food tracking and caloric analysis.

This repository contains the source code and project report for a Calorie Counter Application which utilizes MongoDB for efficient data management, allowing users to track food intake, log calories, and gain insights into their nutritional consumption patterns.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Database Schema](#database-schema)
7. [Report](#report)
8. [Acknowledgements](#acknowledgements)

---

## Project Overview
This project focuses on creating a calorie counter application that provides users with the ability to:
- Log their daily food intake
- Track caloric intake over time
- Receive nutritional breakdowns based on their logs

The primary goal is to offer a simple, intuitive tool for personal health management by storing and retrieving dietary data from a MongoDB database.

## Features
- **User Registration**: Simple registration and authentication to maintain personalized logs.
- **Food Log**: Add and manage food entries with calorie counts and nutritional values.
- **Caloric Analysis**: Calculate and analyze daily, weekly, and monthly caloric intake.
- **MongoDB Backend**: Efficient data storage and retrieval using MongoDB to support scalability.

## Technologies Used

- **Python**: The primary programming language used for the application logic and backend operations.
- **Kivy**: A Python framework for developing multi-touch applications, used for creating the graphical user interface (GUI) of the application.
- **MongoDB**: A NoSQL database for storing user information, meal entries, and food database, providing efficient data retrieval and storage.
- **BSON**: Binary JSON format used for data storage and retrieval in MongoDB.
- **hashlib**: Python library for secure password hashing using SHA-256 algorithm.
- **datetime**: Python module for handling date and time, used to manage meal entries and calculate total calories consumed on specific dates.

## Features

- **User Registration**: Users can create accounts with a username and password, ensuring secure access to their meal data.
- **User Login**: Allows registered users to log in and access their meal tracking functionalities.
- **Meal Tracking**:
  - **Add Meal**: Users can log meals by entering the meal name, calorie count, and date.
  - **View Meals**: Users can view all meals logged for a specific date, with options to edit or delete meal entries.
  - **Edit Meal**: Users can update existing meal entries to correct any mistakes or changes in caloric values.
  - **Delete Meal**: Allows users to remove meal entries from their log.
- **Calorie Calculation**:
  - **Total Calorie Count**: Users can retrieve the total calories consumed on a given date.
  - **Feedback on Caloric Intake**: Provides feedback based on the total calorie count, helping users adjust their diet for better health.
- **Food Database**: 
  - **Search Functionality**: Users can search a pre-defined food database for nutritional information.
  - **Add Food from Database**: Users can easily log food items from the search results into their meal logs.
- **Responsive UI**: The application features a user-friendly interface with a responsive layout that adjusts to various screen sizes.
- **Visual Feedback**: Clear messages and visual elements provide users with immediate feedback on their actions (e.g., meal added, user logged in).

## Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
2. Install the required Python packages:
  ```bash
  pip install -r requirements.txt
  ```
3. To start the application, run:
  ```bash
  python CIS552-Code.py
  ```
4. Follow the on-screen instructions to register, log in, and begin tracking meals.

## Report
For a detailed overview of the project, please refer to the [Project Report](CIS552-Report.pdf).


## References

- **Kivy Documentation**: [Kivy Official Documentation](https://kivy.org/doc/stable/) 

- **MongoDB Documentation**: [MongoDB Official Documentation](https://docs.mongodb.com/)

- **PyMongo Documentation**: [PyMongo Official Documentation](https://pymongo.readthedocs.io/en/stable/)  

- **Python Documentation**: [Python Official Documentation](https://docs.python.org/3/)  

- **NumPy Documentation**: [NumPy Official Documentation](https://numpy.org/doc/stable/)  

- **Pandas Documentation**: [Pandas Official Documentation](https://pandas.pydata.org/docs/)  

- **Hashlib Documentation**: [Hashlib Official Documentation](https://docs.python.org/3/library/hashlib.html)
