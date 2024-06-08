import requests

# GLOBAL CONSTANTS
DIFFICULTIES = ["Any", "Easy", "Medium", "Hard"]


class Data:
    """A class representing the data that will be used to set the parameters of the quiz namely, categories, difficulty
    and number of questions."""
    def __init__(self):
        self.url = "https://opentdb.com/api.php"
        self.parameters = {"amount": 10, "type": "boolean"}
        self.question_num_sel = None
        self.cat_sel = None
        self.diff_sel = None
        res = requests.get("https://opentdb.com/api_category.php")
        res.raise_for_status()
        category_data = res.json()["trivia_categories"]
        self.categories = [category_data[x]["name"] for x in range(len(category_data))]
        ids = [category_data[x]["id"] for x in range(len(category_data))]
        self.category_dict = dict(zip(self.categories, ids))
        self.difficulty = DIFFICULTIES
