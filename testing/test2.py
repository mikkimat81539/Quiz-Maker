import json, random

with open("QA.json", "r") as f:
	data = json.load(f)

question_list = []

points = 5
deduct = 4


for i in data["questions"]:
	question_list.append(i)

	random_question = random.choice(question_list)
	
	for q, a in random_question.items():
		user_answer = int(input(f"{q}: "))
		
		if user_answer == a:
			print("CORRECT")
		else:
			print(f"WRONG the answer is {a}")
			points = (deduct / 5)*100
			deduct -= 1
			
print(f"Total grade for the test is {points} %")
