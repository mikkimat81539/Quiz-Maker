import random, json, bisect, pathlib

try:
	# DEFINE JSON FILE
	p = pathlib.Path(__file__) # call the path class and define

	# filename = p.absolute() # turns file into absolute path
	filename = p.resolve().with_name("questions.json")

	# filename = "questions.json"

	print(filename)

	# OPEN JSON FILE
	with open(filename, "r") as f:
		data = json.load(f)

	# STORE QUESTIONS
	question_list = []

	for i in data:
		# print(f"{i}\n")
		# print(len(data)) # number of questions 
		
		question = f"Question: {i["question"]}"
		A = f"A: {i["A"]}"
		B = f"B: {i["B"]}"
		C = f"C: {i["C"]}"
		D = f"D: {i["D"]}"
		answer = i["answer"]

		question_list.append([question, A, B, C, D, answer])

	# GRADING
	correct = [] # this list stores correct answers

	# SELECT RANDOM QUESTIONS
	num_questions = abs(int(input("Enter number of questions you want on the test (max number is 547): ")))


	print(f"\n\nTHIS IS A {num_questions} QUESTION TEST\n")

	for i in range(num_questions):
		random_questions = random.choice(question_list)
		# print(random_questions[0])

		response = input(f"{random_questions[0]}\n{random_questions[1]}\n{random_questions[2]}\n{random_questions[3]}\n{random_questions[4]}\n\nwrite your answer: ").upper().strip()

		# print("TEST TEST", random_questions[5])

		if response == random_questions[5]:
			print("Correct\n")
			correct.append("CORRECT")

		else:
			print(f"Wrong, the answer was {random_questions[5]}\n")
			# incorrect.append("WRONG")


	num_correct = len(correct) # this is the number of incorrect answers
	# print(num_correct)

	# TOTAL POINTS
	total_points = num_questions

	score = (num_correct/total_points)*100 # You grade score

	# print(score)

	def grade(score):
		i = bisect.bisect([60, 70, 80, 90], score)
		return "FDCBA"[i]

	grade = grade(score)

	print(f"Your Score is {grade}")

except KeyboardInterrupt:
	print("\nProgram terminated by user.")
