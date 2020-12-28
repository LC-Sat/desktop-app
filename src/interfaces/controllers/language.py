# -*- coding: utf-8 -*-

# == IMPORTATIONS == #

try:
    #- Librairies
    import json

except Exception as e:
    raise e

# == LOGIC PART == #


class Language:

    def __init__(self, selected_language):
        '''
            Opening file to acces data
        '''
        with open("resource/i18n/" + selected_language + '.json', 'r') as language_file:
            self.language = json.load(language_file)

    def get_text(self, text):
        return self.language[text]
