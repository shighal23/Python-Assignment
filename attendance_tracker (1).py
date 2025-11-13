"""
==============================================================================
Attendance Tracker - Python Assignment 
==============================================================================
Name : Anshika
Roll No : 2501940028
Course : MCA (AI & ML)
Date : 10 November 2025
Assignment : Attendance Tracker System
Description : A comprehensive tool to record and manage student attendance
             with validation, summary generation, and file export features.
==============================================================================
"""


# Welcome message (Task 1)
print("✅ Welcome to the Student Attendance Tracker Tool!")
print("This program allows you to record student names and check-in times.")
print("You will enter how many records you want, validate them, and see a summary.\n")
print("-" * 60)

# Task 2 & 3: Input, Data Collection & Validation
attendance = {}

num_entries = int(input("How many student attendance entries do you want to record? "))

for i in range(num_entries):
    while True:
        name = input("Enter student name: ").strip()

        # Validate student name
        if name == "":
            print("❌ Name cannot be empty. Please enter again.\n")
            continue
        
        # Check duplicate
        if name in attendance:
            print("⚠️ Student already recorded! Enter a different name.\n")
            continue

        time = input("Enter check-in time (e.g., 09:15 AM): ").strip()

        # Validate time entry
        if time == "":
            print("❌ Time cannot be empty. Please enter again.\n")
            continue

        # If all valid, store entry
        attendance[name] = time
        print("✅ Entry recorded successfully!\n")
        break

# Task 4: Attendance Summary

print("\n\n📍 Attendance Summary")
print("Student Name\t\tCheck-in Time")
print("---------------------------------------------")

for student, time in attendance.items():
    print(f"{student}\t\t{time}")

print("---------------------------------------------")
print(f"Total Students Present: {len(attendance)}")

# Task 5: Absentee Validation (Optional)
choice = input("\nDo you want to enter total number of students? (yes/no): ").lower()

if choice == "yes":
    total_students = int(input("Enter total number of students in the class: "))
    absentees = total_students - len(attendance)

    print(f"\n📊 Attendance Report:")
    print(f"Total Present: {len(attendance)}")
    print(f"Total Absent: {absentees}")

# Task 6 (Bonus): Save Report to File
save = input("\nDo you want to save attendance report to 'attendance_report.txt'? (yes/no): ").lower()

if save == "yes":
    with open("attendance_report.txt", "w") as file:
        file.write("Attendance Report\n")
        file.write("---------------------------------\n")
        for student, time in attendance.items():
            file.write(f"{student}\t{time}\n")
        file.write("---------------------------------\n")
        file.write(f"Total Present: {len(attendance)}\n")
        
        print("✅ Attendance report saved as 'attendance_report.txt'")

print("\n🎉 Thank you for using the Attendance Tracker!")