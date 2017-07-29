class AnonymousSurvey():
    '匿名调查'
    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_responses(self, new_responses):
        self.responses.append(new_responses)
    def show_results(self):
        print("Survey results:")
        for response in self.responses:
            print('-'+response)

