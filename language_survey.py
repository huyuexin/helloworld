from survey import AnonymousSurvey

question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)
my_survey.show_question()

print("Enter Q to exit?")
while True:
    response=input('language?')
    if response == 'q':
        break
    my_survey.store_responses(response)
print("\n Thank your to everyone who participated in the survey")
my_survey.show_results()