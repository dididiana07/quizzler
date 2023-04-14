from quizzlet_window import QuizzWindow
import requests

URL = "https://opentdb.com/api.php?amount=10&category=23&difficulty=easy&type=boolean"
trivia_response = requests.request("GET", URL)
data = trivia_response.json()["results"]


quizzler = QuizzWindow(data_list_questions=data)

