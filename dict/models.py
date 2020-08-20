from django.db import models

# Create your models here.
class Word:
    def get_phonetics(self, phonetics):
        empty_list = [{}]
        return " Not available" if phonetics == empty_list else phonetics

    def get_meaning(self, meaning):
        return meaning

    def get_gender(self):
        for key in self.meaning:
            self.gender = key

    def get_definitions(self):
        definitions = self.meaning[self.gender]
        self.definitions = [WordDefinition(d) for d in definitions]

    def __init__(self, json_data):
        self.word = json_data["word"]
        self.phonetics = self.get_phonetics(json_data["phonetics"])
        self.meaning = self.get_meaning(json_data["meaning"])
        self.get_gender()
        self.get_definitions()

    def return_dict(self):
        return {
            'word': self.word,
            'phonetics': self.phonetics,
            'gender': self.gender,
            'definitions': self.definitions,
        }


class WordDefinition:
    def __init__(self, json):
        self.definition = json["definition"]
        try:
            self.example = json["example"]
        except KeyError:
            self.example = "No example available"

        s = ' '.join(json["synonyms"])
        a = ' '.join(json["antonyms"])
        self.synonyms = "No synonyms available" if not s else s
        self.antonyms = "No antonyms available" if not a else a
