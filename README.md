# Pet Clinic Web Application

This is a simple web application for managing pet clinic data, including **owners**, **pets**, and **appointments**. The app allows users to add their details, view their pets, and manage appointments for their pets.

## Features

- **Owner Registration**: Users can register their details, including name and contact information.
- **Pet Management**: Users can add pets associated with themselves (owner), including pet name and type.
- **Appointment Scheduling**: Users can schedule appointments for their pets.
- **Data Storage**: All data is stored in an SQLite database, which includes information about owners, pets, and appointments.

## Technologies Used

- **Flask**: A Python web framework used for building the application.
- **SQLAlchemy**: An ORM used for managing database operations.
- **SQLite**: A lightweight database engine to store pet clinic data.
- **HTML/CSS**: For frontend design and styling.
- **Jinja2**: Templating engine for dynamically generating HTML pages.
- **Python 3.x**: Programming language used to implement the app.

## Setup and Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- pip (Python package installer)
- SQLite3 (comes pre-installed with Python)

### Step-by-Step Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/DhaneshGore/pet_Dr.git
   cd pet_Dr


2. **Create a virtual environment (optional but recommended)**:
   bash
   Copy code
   **python -m venv venv**

3. Activate the virtual environment:

   On Windows:
   bash
   Copy code
   **.\venv\Scripts\activate**

   On macOS/Linux:
   bash
   Copy code
   **source venv/bin/activate**

4. Install the required dependencies:
   bash
   Copy code
   **pip install -r requirements.txt**

5. Initialize the database: The application uses SQLAlchemy to create tables. If they are not already created, run the following command:
   bash
   Copy code
   **flask db upgrade**

6. Run the Flask application:
   bash
   Copy code
   **flask run**
   The application will be available at http://127.0.0.1:5000/.

                                                                  ***Endpoints***
/user_form: A form for users to submit their details (owner, pet, appointment).
/pets: A list of pets in the clinic.
/appointments: A list of upcoming appointments for pets.
/: A list of owners registered in the clinic.
Example Screenshots
Include screenshots of your application here (optional).

Owner List

Pet List

Appointment List

Future Improvements
Authentication: Implement user authentication to allow multiple users to manage their own pets and appointments.
Error Handling: Add more robust error handling and validation for form inputs.
Responsive Design: Improve the design to be more responsive on different screen sizes.
Advanced Features: Implement features like pet health tracking, reminders for appointments, etc.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
Flask: Web framework used in this application.
SQLAlchemy: ORM for interacting with the SQLite database.
Jinja2: Templating engine used in Flask for dynamic HTML rendering.
