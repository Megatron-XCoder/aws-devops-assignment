import csv

def analyze_students(file_path, threshold):
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        print(f"Students with average grade above {threshold}:")
        for row in reader:
            name = row['name']
            grade = float(row['grade'])
            if grade > threshold:
                print(f" - {name} ({grade})")

if __name__ == "__main__":
    file_path = 'students.csv'
    threshold = float(input("Enter the grade threshold: "))
    analyze_students(file_path, threshold)

