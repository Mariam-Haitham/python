
skills = ["Python", "Java", "C++", "Team Work", "Experience"]

cv = {}

print("Welcome to the special recruitment program, please answer the following questions:")

cv["name"] = input("name: ")
cv["age"] = input("age: ")
cv["experience"] = input("how many years of experience do you have? ")
cv["skills"] = []

print("\nskills:")
counter = 1;
for skill in skills:
    print(str(counter), "-", skill)
    counter += 1
 
while(True):
    first_skill = int(input("choose a skill from above: "))
    if first_skill < 1 or first_skill > len(skills):
        print("Invalid choice!")
        continue;   
    cv["skills"].append(skills[first_skill - 1])
    break;
    
while(True):
    second_skill = int(input("choose another skill from above: "))
    if second_skill < 1 or second_skill > len(skills):
        print("Invalid choice!")
        continue;   
    cv["skills"].append(skills[second_skill - 1])
    break;
    
    
age = int(cv["age"])
experience = int(cv["experience"])

if age < 25 or age > 40 or experience < 3 or (first_skill != 1 and second_skill != 1):
    print("Sorry, you have been declined,", cv["name"], "!")
else:
    print("you have been accepted,", cv["name"], "!")