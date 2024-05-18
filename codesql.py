import sqlite3

# Connect to SQLite database (create it if not exists)
conn = sqlite3.connect('clinic_database.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS Patients (
    PatientID INTEGER PRIMARY KEY,
    Name TEXT,
    Age INTEGER,
    Gender TEXT,
    Contact TEXT,
    Address TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Doctors (
    DoctorID INTEGER PRIMARY KEY,
    Name TEXT,
    Specialty TEXT,
    Contact TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Appointments (
    AppointmentID INTEGER PRIMARY KEY,
    PatientID INTEGER,
    DoctorID INTEGER,
    AppointmentDate DATE,
    StartTime TIME,
    EndTime TIME,
    Notes TEXT,
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID),
    FOREIGN KEY (DoctorID) REFERENCES Doctors(DoctorID)
)
''')

# Insert sample data
cursor.executemany('''
INSERT INTO Patients (Name, Age, Gender, Contact, Address)
VALUES (?, ?, ?, ?, ?)
''', [
    ('John Doe', 35, 'Male', '1234567890', '123 Main St'),
    ('Jane Smith', 28, 'Female', '0987654321', '456 Elm St')
])

cursor.executemany('''
INSERT INTO Doctors (Name, Specialty, Contact)
VALUES (?, ?, ?)
''', [
    ('Dr. Smith', 'Cardiologist', '1112223333'),
    ('Dr. Johnson', 'Pediatrician', '4445556666')
])

cursor.executemany('''
INSERT INTO Appointments (PatientID, DoctorID, AppointmentDate, StartTime, EndTime, Notes)
VALUES (?, ?, ?, ?, ?, ?)
''', [
    (1, 1, '2024-05-17', '10:00:00', '11:00:00', 'Heart checkup'),
    (2, 2, '2024-05-18', '09:30:00', '10:30:00', 'Routine checkup')
])

# Commit changes and close the connection
conn.commit()
conn.close()

# Connect again to retrieve and print data
conn = sqlite3.connect('clinic_database.db')
cursor = conn.cursor()

# Retrieve and print data
cursor.execute('SELECT * FROM Patients')
print("Patients:")
for row in cursor.fetchall():
    print(row)

cursor.execute('SELECT * FROM Doctors')
print("\nDoctors:")
for row in cursor.fetchall():
    print(row)

cursor.execute('SELECT * FROM Appointments')
print("\nAppointments:")
for row in cursor.fetchall():
    print(row)

# Close the connection
conn.close()
