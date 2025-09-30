# Normalized Course Catalog Schema

Structure and schema of the clean_course_catalog.csv

| Column Name | Required Data Type | Brief Description |
| :---------- | :---------------- | :---------------- |
| `name`      | `VARCHAR(80)`     | Instructor's full name. |
| `role`      | `VARCHAR(20)`      | Instructor's role in the course.
| `course_id` | `VARCHAR(20)`      | Course identifier with department and number. |
| `title`     | `VARCHAR(100)`     | Course title. |
| `level`     | `INT`              | Course Level |
| `section`   | `VARCHAR(10)`      | Section identifier for the course. |