class Question:
    def __init__(self, _text, _answer):
        self.text = _text
        self.answer = _answer

    def __str__(self):
        return f"Question is '{self.text}', Answer is {self.answer} "
