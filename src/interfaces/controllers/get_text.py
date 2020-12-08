# == IMPORTATIONS == #

try:
    #- Librairies
    import json

    #- Files
    settings_path = 'resource/data/settings.json'
    with open(settings_path, 'r') as settings_file:
        settings = json.load(settings_file)

    languages_path = 'resource/i18n/' + settings["language"] + '.json'
    with open(languages_path, 'r') as languages_file:
        language = json.load(languages_file)

except Exception as e:
    raise e

# == LOGIC PART == #

def get_text(text):
    return language[text]
