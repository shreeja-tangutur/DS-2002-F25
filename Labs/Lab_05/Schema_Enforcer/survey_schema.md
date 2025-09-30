# Survey Data Schema 

Structure of the clean_survey_data.csv

| Column Name | Required Data Type | Brief Description |
| :--- | :--- | :--- |
| `student_id` | `INT` | Unique identifier for the student. |
| `major` | `VARCHAR(50)` | Primary discipline student is studying. |
| `GPA` | `FLOAT` | Student's grade point average. |
| `is_cs_major` | `BOOL` | Indicates if a student is studying Computer Science. |
| `credits_taken` | `FLOAT` | Total number of credits taken by student. |