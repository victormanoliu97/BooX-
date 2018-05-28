import os,json
def getLanguages():
    languagesFile = os.path.join(os.path.dirname(__file__),'isoLanguages.json')
    languagesDict = {}
    with open(languagesFile,'r',encoding="utf8") as file:
        languagesDict = json.load(file)
    languages = []
    for language in languagesDict:
        languages.append(languagesDict[language]['name'])

    if len(languages)==0:
        return None
    return languages


def getLanguageFromRegion(region):
    languagesFile = os.path.join(os.path.dirname(__file__),'isoLanguages.json')
    languagesDict = {}
    with open(languagesFile,'r',encoding="utf8") as file:
        languagesDict = json.load(file)
    for language in languagesDict:
        if language==region:
            return languagesDict[language]['name']
    return 'Unknown'
