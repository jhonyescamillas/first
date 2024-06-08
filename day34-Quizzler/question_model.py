class Question:
    """A class representing each question that will go in a list. Takes in a text and an answer attribute."""
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
