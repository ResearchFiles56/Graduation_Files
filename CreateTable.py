import sqlite3

def create_database():
    conn = sqlite3.connect("LLM_Education.db")
    cursor = conn.cursor()

    # Create Papers table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Papers (
            PaperID INTEGER PRIMARY KEY,
            PaperTitle TEXT,
            PublishYear INTEGER,
            LLMInfoID INTEGER,
            ORID INTEGER,
            MethodID INTEGER
        )
    ''')

    # Create LLMInfo table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS LLMInfo (
            LLMInfoID INTEGER PRIMARY KEY,
            PaperID INTEGER,
            LLMK TEXT,
            ToolLLM TEXT,
            LLMU TEXT,
            LLMTD TEXT,
            FOREIGN KEY (PaperID) REFERENCES Papers (PaperID)
        )
    ''')

    # Create ObjectiveResult table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ObjectResult (
            ORID INTEGER PRIMARY KEY,
            PaperID INTEGER,
            Objective TEXT,
            Result TEXT,
            Limitation TEXT,
            FOREIGN KEY (PaperID) REFERENCES Papers (PaperID)
        )
    ''')

    # Create Methods table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Methods (
            MethodID INTEGER PRIMARY KEY,
            PaperID INTEGER,
            SampleSizeAll INTEGER,
            FOREIGN KEY (PaperID) REFERENCES Papers (PaperID)
        )
    ''')

    # Create Assignments table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Assignments (
            AssignmentID INTEGER PRIMARY KEY,
            MethodID INTEGER,
            AssignmentDetail TEXT,
            FOREIGN KEY (MethodID) REFERENCES Methods (MethodID)
        )
    ''')

    # Create Classes table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Classes (
            ClassID INTEGER PRIMARY KEY,
            MethodID INTEGER,
            ClassC TEXT,
            FOREIGN KEY (MethodID) REFERENCES Methods (MethodID)
        )
    ''')

    # Create Exams table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Exams (
            ExamID INTEGER PRIMARY KEY,
            MethodID INTEGER,
            ExamC TEXT,
            FOREIGN KEY (MethodID) REFERENCES Methods (MethodID)
        )
    ''')

    # Create Surveys table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Surveys (
            SurveyID INTEGER PRIMARY KEY,
            MethodID INTEGER,
            QuestionnaireD TEXT,
            QuestionnaireN INTEGER,
            InterviewD TEXT,
            InterviewN INTEGER,
            FOREIGN KEY (MethodID) REFERENCES Methods (MethodID)
        )
    ''')

    # Create Students table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Students (
            StudentsID INTEGER PRIMARY KEY,
            MethodID INTEGER,
            StudentD TEXT,
            ExperimentalGroupN INTEGER,
            ExperimentalGroupD TEXT,
            ControlGroupN INTEGER,
            ControlGroupD TEXT,
            FOREIGN KEY (MethodID) REFERENCES Methods (MethodID)
        )
    ''')

    conn.commit()
    conn.close()
    print("Database and tables created successfully.")

if __name__ == "__main__":
    create_database()
