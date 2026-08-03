import random, json


filename = "QA.json"

with open(filename, "r") as file:
	data = json.load(file)

question_list = []

for question in data[f"question"]:
	question_list.append(question)

# print(question_list)

question_num = abs(int(input("Enter number of questions for quiz (max is 5): ")))

random_question = random.choice(question_list)

if question_num > 5 or question_num < 1:
	print("enter number between 1 and 5")
else:
	for i in range(question_num):
		random_question = random.choice(question_list)

		user_answer = int(input(f"question {i + 1}: {random_question}: "))
				
		print(data[random_question])

#		if user_answer == data[i]:
#			print(True)
#			print(f"Answer is {data[i]}")
