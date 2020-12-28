# -*- coding: utf-8 -*-

# == IMPORTATIONS == #

try:
    #- Librairies
    import json

except Exception as e:
    raise e

# == LOGIC PART == #


class Theme:

    def __init__(self, selected_theme):
        '''
            Opening file to acces data
        '''
        with open("resource/themes/" + selected_theme + '.json', 'r') as language_file:
            self.language = json.load(language_file)

    def get_theme_data(self, element):
        return self.language[element]

test = Theme('dark')
print(test.get_theme_data('backgroundColor'))