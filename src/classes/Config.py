import json


class Config:

    Characters = {}




    def __init__(self):
        self.load_config()

    def load_config(self):
        try:
            with open("config.json", "r") as f:
                self.Characters = json.load(f)
        except Exception:
            self.Characters = {}

    def write_config(self):
        print(self.Characters)
        with open("config.json", "w") as f:
            json_characters = {str(k): v.to_dict() for k, v in self.Characters.items()}
            json.dump(json_characters, f)


    def get_last_character_id(self):
        try:
            return int(max(self.Characters.keys()))
        except ValueError:
            return 0