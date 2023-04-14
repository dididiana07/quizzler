from random import choice
import html


class Questions:

    @classmethod
    def next_question(cls, trivia_database_questions):
        """From the Trivia Database API get the 'results' keyword and use the list as an input."""
        chosen_question = choice(trivia_database_questions)
        return html.unescape(chosen_question["question"]), html.unescape(chosen_question["correct_answer"])
