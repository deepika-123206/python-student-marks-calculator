def calculate_grade(avg):
    if avg >= 90: return "A"
    elif avg >= 75: return "B"
    elif avg >= 60: return "C"
    else: return "Fail"

def main():
    print("=== Student Marks Calculator ===")
    name = input("Student Name: ")
    marks = []
    
    for i in range(5):
        m = int(input(f"Subject {i+1} marks: "))
        marks.append(m)
    
    total = sum(marks)
    avg = total / 5
    grade = calculate_grade(avg)
    
    failed = []
    for i, m in enumerate(marks):
        if m < 35:
            failed.append(f"Subject {i+1}")
    
    print(f"\n--- Result for {name} ---")
    print(f"Total: {total}, Average: {avg}, Grade: {grade}")
    
    if failed:
        print("Failed Subjects:", ", ".join(failed))
    else:
        print("Status: All Clear")
    
    with open("result.txt", "w") as f:
        f.write(f"Student Name: {name}\n")
        f.write(f"Marks: {marks}\n")
        f.write(f"Total: {total}\n")
        f.write(f"Average: {avg}\n")
        f.write(f"Grade: {grade}\n")
        if failed:
            f.write(f"Failed Subjects: {', '.join(failed)}\n")
        else:
            f.write("Status: All Clear\n")
    
    print("\nResult 'result.txt' file lo save aindi!")

main()
