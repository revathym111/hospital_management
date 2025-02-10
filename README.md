# Hospital Management System

## Project Overview
The Hospital Management System is designed to handle the records and operations related to patients, doctors, and appointments in a hospital. The system enables administrators to manage data efficiently, streamline hospital operations, and enhance patient care by providing easy access to critical information. 

### Key Features
## What are the various features you would like your project to offer?
- **Manage Patient Records**: Add, update, and delete patient details.
- **Manage Doctor Records**: Add, update, and delete doctor details.
- **Appointments Management**: Schedule, view, and cancel appointments between patients and doctors.
- **Medical History Tracking**: Access a patient's past appointments and treatments.

### Database Details
## Provide a description of the database tables required for the application, including column names, data types, constraints, and foreign keys. Include your database name.
#### Database Name: `hospital_management`

#### Tables

1. **`patients`**
   - **Columns**:
     - `id`: INT, Primary Key
     - `name`: VARCHAR(255), Not Null
     - `dob`: DATE
     - `gender`: VARCHAR(10)
     - `contact_number`: VARCHAR(15)
     - `email`: VARCHAR(255)

2. **`doctors`**
   - **Columns**:
     - `id`: INT, Primary Key
     - `name`: VARCHAR(255), Not Null
     - `specialization`: VARCHAR(255)
     - `contact_number`: VARCHAR(15)
     - `email`: VARCHAR(255)

3. **`appointments`**
   - **Columns**:
     - `id`: INT, Primary Key
     - `patient_id`: INT, Foreign Key (to `patients` table)
     - `doctor_id`: INT, Foreign Key (to `doctors` table)
     - `appointment_date`: TIMESTAMP

---

## API Reference
## What are the API endpoints that  would need to be set up for each feature? List them along with the respective HTTP verb, endpoint URL, and any special details (query parameters, request bodies, headers)

#### **Patients**
- **Create a Patient**: `POST /patients/`
- **View All Patients**: `GET /patients`

#### **Doctors**
- **Create a Doctor**: `POST /doctors/`
- **View All Doctors**: `GET /doctors/`

#### **Appointments**
- **Create an Appointment**: `POST /appointments/`
- **View All Appointments**: `GET /appointments/`
- **Cancel an Appointment**: `DELETE /appointments/<appointment_id>/`

---

## Retrospective

### How did the project's design evolve over time?
The initial design focused on creating a robust system for basic CRUD operations for patients, doctors, and appointments. Over time, additional features like medical history tracking and improved error handling needs to be incorporated based on system requirements.

### Did you choose to use an ORM or raw SQL? Why?
Django ORM was chosen for this project to simplify database operations, improve code readability, and reduce development time. Using an ORM also provides better scalability and maintainability, especially for future enhancements.

### What future improvements are in store, if any?
1. **Authentication & Authorization**: Implement user roles (e.g., admin, doctor, patient) for enhanced security.
2. **Medical Records**: Add functionality to track treatments and prescriptions.
3. **Appointment Reminders**: Integrate notification systems to send reminders via email or SMS.
4. **Analytics Dashboard**: Provide insights into hospital operations and patient statistics.

---
# hospital_management
