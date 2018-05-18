import os,json
def getTopics():
    topicsFile = os.path.join(os.path.dirname(__file__),'topics.json')
    topicsDict = {}
    with open(topicsFile,'r',encoding="utf8") as file:
        topicsDict = json.load(file)
    topics = []
    for topic in topicsDict:
        topics.append(topicsDict[topic])

    if len(topics)==0:
        return None
    return topics