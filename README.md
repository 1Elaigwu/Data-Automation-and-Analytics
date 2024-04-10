 # Hotel Management Automation

This project automates data updates and analytics for a hotel management system using Python and SQL Server.

## Features

- **Data Updates**: Automatically update room rates based on predefined rules.
- **Analytics**: Perform analytics on bookings and payments.

## Security Measures

### 1. Secure Database Connection
- Database credentials are stored securely using environment variables (`DB_HOST`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`).

### 2. Parameterized Queries
- All SQL queries use parameterized statements (`pyodbc`) to prevent SQL injection attacks.

### 3. Role-Based Access Control
- Database users have limited privileges (`least privilege principle`) required for the application.

## Usage

### Prerequisites
- Install Python 3.x and required packages (`pip install -r requirements.txt`).
- Set up a SQL Server database (SSMS) with the provided schema.

### Configuration
- Create a `.env` file and set the environment variables (`DB_HOST`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`).

### Running the Script
-- ```bash
python src/main.py
Examples
Update Room Rate
# Update room rate for room_id 5 to 90.00
db = Database()
db.update_room_rate(5, 90.00)

Perform Analytics
# Perform analytics (e.g., fetch bookings)
db = Database()
db.perform_analytics()

License
This project is licensed under the MIT License - see the LICENSE file for details.


### 4. Additional Considerations
- **Environment Variables**: Use a `.env` file or set environment variables to securely store sensitive information like database credentials.
- **Error Handling**: Implement robust error handling and logging to capture and handle exceptions gracefully.
- **Testing**: Conduct thorough testing to validate data update and analytics functionalities.
- **Version Control**: Use Git for version control and host your project on GitHub for collaboration and documentation.

By following this structured approach, you can develop and document a secure Python script that interacts with a SQL Server database (SSMS) for automating data updates and analytics within a hotel management system. Documenting practical examples in your README.md will enhance usability and understanding for users and contributors of your project.
