from Question_18 import Question

question_prompts = [
    "What color are bananas?\n(a)Red\n(b)Green\n(c)Purple\n(d)Yellow\n\n",
    "What color are apples?\n(a)Red/Green\n(b)Blue\n(c)Purple\n(d)Yellow\n\n",
    "What color are strawberries?\n(a)Red\n(b)Green\n(c)Purple\n(d)Yellow\n\n"
]

questions = [
    Question(question_prompts[0], "d"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "a")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("Your Score is " + str(score) + "/" + str(len(questions)))


run_test(questions)
