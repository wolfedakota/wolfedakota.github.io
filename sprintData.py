import sqlite3
from storyPrioritization import calculate_priority, BacklogItem

# Connect to the database
conn = sqlite3.connect('backlog.db')
cursor = conn.cursor()

# Function to add a new backlog item with user input
def add_backlog_item():
    id = int(input("Enter Backlog Item ID: "))
    description = input("Enter Task Description: ")
    urgency = int(input("Enter Urgency (1-10): "))
    dependencies = int(input("Enter Number of Dependencies: "))
    feedback = int(input("Enter Customer Feedback Score (1-10): "))
    status = input("Enter Status (To Do / In Progress / Completed): ")

    priority = calculate_priority(BacklogItem(id, urgency, dependencies, feedback))
    
    cursor.execute("""
        INSERT INTO BacklogItems (id, description, urgency, dependencies, customer_feedback, priority_score, status)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (id, description, urgency, dependencies, feedback, priority, status))
    conn.commit()
    print(f"Backlog item '{description}' added successfully!")

# Function to create a new sprint with user input
def create_sprint():
    sprint_id = int(input("Enter Sprint ID: "))
    start_date = input("Enter Sprint Start Date (YYYY-MM-DD): ")
    end_date = input("Enter Sprint End Date (YYYY-MM-DD): ")

    cursor.execute("""
        INSERT INTO Sprints (sprint_id, start_date, end_date, velocity, completed_tasks)
        VALUES (?, ?, ?, 0, 0)
    """, (sprint_id, start_date, end_date))
    conn.commit()
    print(f"Sprint {sprint_id} created successfully!")

# Function to assign backlog item to a sprint with user input
def assign_task_to_sprint():
    sprint_id = int(input("Enter Sprint ID: "))
    backlog_id = int(input("Enter Backlog Item ID to Assign: "))

    cursor.execute("""
        INSERT INTO SprintBacklog (sprint_id, backlog_id)
        VALUES (?, ?)
    """, (sprint_id, backlog_id))
    conn.commit()
    print(f"Backlog item {backlog_id} assigned to Sprint {sprint_id}.")

# Function to update sprint progress with user input
def update_sprint_progress():
    sprint_id = int(input("Enter Sprint ID to Update: "))
    completed_tasks = int(input("Enter Number of Completed Tasks: "))

    cursor.execute("""
        UPDATE Sprints
        SET completed_tasks = ?
        WHERE sprint_id = ?
    """, (completed_tasks, sprint_id))
    conn.commit()
    print(f"Sprint {sprint_id} progress updated.")

# **Main Menu for User Interaction**
def main():
    while True:
        print("\n--- Agile Backlog Management ---")
        print("1. Add Backlog Item")
        print("2. Create Sprint")
        print("3. Assign Backlog Item to Sprint")
        print("4. Update Sprint Progress")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_backlog_item()
        elif choice == "2":
            create_sprint()
        elif choice == "3":
            assign_task_to_sprint()
        elif choice == "4":
            update_sprint_progress()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Run the interactive menu
if __name__ == "__main__":
    main()

# Close the database connection when done
conn.close()
