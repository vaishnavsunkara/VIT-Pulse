# VIT-Pulse – Project Statement

## 1. Problem Statement

In college hostels and campus, students face different problems like Wi-Fi issues, maintenance problems, cleanliness problems, electrical issues, etc. Usually, students have to inform the concerned person directly or through messages.

Because of this, some complaints may be missed or it can become difficult to keep track of them.

VIT-Pulse is a simple complaint management system made using Python. It helps students register their complaints and allows the complaints to be viewed and their status to be updated.

---

## 2. Scope of the Project

The main scope of VIT-Pulse is to make the complaint process easier and more organized.

The project allows users to:

- Create a new complaint.
- Enter the title and description of the complaint.
- Select the category of the complaint.
- Set the priority of the complaint.
- View all the registered complaints.
- Search and filter complaints.
- Update the status of a complaint.
- View complaint statistics.
- Store the complaints in a database.

The current project is mainly focused on basic complaint management. More features can be added to the project in the future.

---

## 3. Target Users

The main users of VIT-Pulse are:

- College students
- Hostel students
- Student representatives
- Hostel or campus management

Students can register their problems, and the concerned person can view the complaints and update their status.

---

## 4. High-Level Features

### 4.1 Create Complaint

The user can create a complaint by entering:

- Title
- Description
- Category
- Priority

The complaint is then stored in the database.

### 4.2 View Complaints

The user can view all the complaints that have been registered.

The system displays details such as:

- Complaint ID
- Title
- Description
- Category
- Priority
- Status

### 4.3 Search and Filter

Users can search complaints using a keyword. Administrators or representatives can also filter complaints by category.

### 4.4 Update Complaint Status

The status of a complaint can be changed according to its progress.

For example:

- Pending
- In Progress
- Resolved

### 4.5 Dashboard

The admin / FR portal provides basic statistics showing:

- Total complaints
- Pending complaints
- In-progress complaints
- Resolved complaints
- High-priority complaints

### 4.6 Database

The project uses a SQLite database to store the complaints. This means the complaints are not lost when the program is closed.

---

## 5. Future Scope

In the future, the project can be improved by adding features like:

- Student login
- Admin login
- Complaint timestamps
- Notifications
- Graphical user interface
- Web-based version
- Different dashboards for students and admins
