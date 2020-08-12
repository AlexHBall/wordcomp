from django.db import models

# Create your models here.
class Word:
    def __init__(self,json_data):
        self.word = json_data["word"]
        self.phonetics = json_data["phonetics"]
        self.meaning = json_data["meaning"]
        for key in self.meaning:
                self.gender = key
        self.definitions = self.meaning[self.gender]

    def return_dict(self):
        return {
            'word' : self.word,
            'phonetics' : self.phonetics,
            'gender' : self.gender,
            'definitions' : self.definitions,
            }