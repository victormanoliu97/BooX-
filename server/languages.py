import os,json
def getLanguages():
    languagesFile = os.path.join(os.path.dirname(__file__),'isoLanguages.json')
    languagesDict = {}
    with open(languagesFile,'r',encoding="utf8") as file:
        languagesDict = json.load(file)
    languages = []
    print(languagesDict)
    for language in languagesDict:
        languages.append(languagesDict[language]['name'])

    if len(languages)==0:
        return None
    return languages