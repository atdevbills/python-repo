def calculate_grade(average):
    if average >= 90:
        return "A (Excellent)"
    elif average >= 80:
        return "B (Very Good)"
    elif average >= 70:
        return "C (Good)"
    elif average >= 60:
        return "D (Pass)"
    else:
        return "F (Fail)"

name = input("Enter your name >> ")
scores = []
for i in range(5):
	score = int(input(f"Enter score {i+1} >> "))
	scores.append(score)

result = sum(scores) / 5
if score < 0 or score > 100:
    print("Invalid score! Enter between 0 and 100")
    
 
print("="*25)
print(f"Student : {name}")
print(f"Average Score : {result}")
print(f"Grade : {calculate_grade(result)}")
print("="*25)

