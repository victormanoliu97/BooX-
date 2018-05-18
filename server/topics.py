import os,json
def getTopics():
    topicsFile = os.path.join(os.path.dirname(__file__),'topics.json')
    topics = []
    with open(topicsFile,'r',encoding="utf8") as file:
        topics = json.load(file)
    if len(topics)==0:
        return None
    return topics