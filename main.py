from quizzlet_window import QuizzWindow
import requests

parameters = {
  "amount": "10",
  "type: "boolean"
}

URL = "https://opentdb.com/api.php"
trivia_response = requests.request("GET", URL, params=parameters)
data = trivia_response.json()["results"]


quizzler = QuizzWindow(data_list_questions=data)

