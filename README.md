# Hospital Management System Project Description

# Er diagram

![Screenshot 2024-05-19 002644](https://github.com/rahulgit64/DBMS-project/assets/150422604/b2f216f0-6cf6-417f-9f57-f7fec2bdf541)

# Schema diagram

![Screenshot 2024-05-19 102715](https://github.com/rahulgit64/DBMS-project/assets/150422604/c9621a7b-869d-40a0-8c52-163283cec003)




# Overview
The Hospital Management System (HMS) is a comprehensive software solution designed to streamline the operations and management of a hospital. This system facilitates efficient handling of patient information, doctor details, and appointment scheduling, ensuring smooth and effective healthcare service delivery.

# Database Design
The HMS database comprises three primary tables: Patients, Doctors, and Appointments. These tables are interconnected through foreign keys to maintain relational integrity and support efficient data retrieval.

# Patients Table

PatientID: An integer serving as the primary key to uniquely identify each patient.
Name: The patient's full name, stored as a string of up to 50 characters.
Age: The age of the patient.
Gender: The patient's gender, stored as a string.
Contact: The contact number of the patient.
Address: The patient's address

![Screenshot 2024-05-18 101731](https://github.com/rahulgit64/DBMS-project/assets/150422604/c47bd283-c3d6-4e9a-9b5c-2559f5c7ee82) 



# Doctors Table

DoctorID: An integer serving as the primary key to uniquely identify each doctor.
Name: The doctor's full name.
Specialty: The doctor's medical specialty.
Contact: The contact number of the doctor

![Screenshot 2024-05-18 102138](https://github.com/rahulgit64/DBMS-project/assets/150422604/68a300bf-3adf-4c5f-8ca1-cd487c9498f3)

# Appointments Table

AppointmentID: An integer serving as the primary key to uniquely identify each appointment.
PatientID: A foreign key linking to the PatientID in the Patients table.
DoctorID: A foreign key linking to the DoctorID in the Doctors table.
AppointmentDate: The date of the appointment.
StartTime: The start time of the appointment.
EndTime: The end time of the appointment.
Notes: Additional notes about the appointment.

![Screenshot 2024-05-18 102441](https://github.com/rahulgit64/DBMS-project/assets/150422604/e19d8040-3d7e-4c4e-bfe2-3133c1b4575e) 

# Data Insertion
Initial data is inserted into the tables to provide sample records for testing and demonstration purposes.

![Screenshot 2024-05-18 102718](https://github.com/rahulgit64/DBMS-project/assets/150422604/56d6eab8-3d3b-442e-b038-38aa7c43d3f8)

# Output

![Screenshot 2024-05-18 200448](https://github.com/rahulgit64/DBMS-project/assets/150422604/ce991590-a286-4fe4-838a-bc9209b4bb98)




# Conclusion
The Hospital Management System is designed to enhance the administrative efficiency of hospitals by managing patient and doctor information, and facilitating appointment scheduling. The system ensures data integrity through well-defined relationships and supports various database operations, making it a robust solution for healthcare management.

# Compile

https://paiza.io/en/languages/python3



