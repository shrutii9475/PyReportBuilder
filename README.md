# PyReportBuilder

## Python Tkinter Application with Login, Signup, and Home Windows

This repository contains a Python Tkinter application that provides a user-friendly interface with essential features such as login, signup, and home windows. It is designed to streamline user authentication and navigation within the application.

### Features

1. **Login and Signup**: The application allows users to securely log in using their credentials or create a new account through the signup window. User information is securely stored in a MySQL database.

2. **MySQL Database Integration**: The application seamlessly connects to a MySQL database, providing a reliable and scalable storage solution for user credentials and data. The integration ensures data integrity and allows for efficient retrieval and management of information.

3. **Excel Upload and Database Interaction**: Users can upload Excel files directly to the MySQL database using the application's built-in functionality. This feature simplifies data management by enabling users to easily import and organize data in the database.

4. **Auto-Generated Document Reports**: The application leverages the data stored in the MySQL database to automatically generate document reports. By fetching the required data, it streamlines the process of creating reports, saving time and effort.

### Requirements

To run this application, ensure you have the following dependencies installed:

- Python (version 3.6 or above)
- Tkinter library
- MySQL Connector library

### Getting Started

1. Clone this repository to your local machine using the following command:
   ```
   git clone https://github.com/shrutii9475/PyReportBuilder.git
   ```

2. Install the required dependencies using pip:
   ```
   pip install tkinter mysql-connector-python
   ```

3. Configure the MySQL database connection by updating the necessary credentials in the application's source code.

4. Run the application by executing the main Python file:
   ```
   python main.py
   ```

