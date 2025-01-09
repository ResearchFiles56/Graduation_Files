import sqlite3
import csv

conn = sqlite3.connect("LLM_Education.db")
cursor = conn.cursor()

# List of tables to export and their corresponding file names
tables = [
    ("Papers", "./Papers.csv"),
    ("LLMInfo", "./LLMInfo.csv"),
    ("ObjectResult", "./ObjectResult.csv"),
    ("Methods", "./Methods.csv"),
    ("Assignments", "./Assignments.csv"),
    ("Classes", "./Classes.csv"),
    ("Exams", "./Exams.csv"),
    ("Surveys", "./Surveys.csv"),
    ("Students", "./Students.csv"),
]

for table_name, file_name in tables:
    try:
        # Fetch table data
        cursor.execute(f'SELECT * FROM {table_name}')
        rows = cursor.fetchall()

        # Fetch table headers
        cursor.execute(f'PRAGMA table_info({table_name})')
        headers = [column[1] for column in cursor.fetchall()]

        # Write to CSV file
        with open(file_name, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(headers)  # Write headers
            writer.writerows(rows)    # Write rows

        print(f"Exported table {table_name} to {file_name}")

    except Exception as e:
        print(f"Error exporting table {table_name}: {e}")

conn.close()
print("All tables have been exported successfully.")