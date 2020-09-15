import requests
import json
import datetime

URI = 'http://codeforces.com/api/user.status'

def beuautify(jsonObj):
    return json.dumps(jsonObj, indent=1)

def get(url, params):
    res = requests.get(url, params)
    
    obj = json.loads(res.text)

    if obj['status'] == 'OK':
        return None, obj['result']

    return obj['comment'], None
    
def recentSubmission(handle, currentTime):
    params = {'handle':handle, 'from':1, 'count':10}
    err, obj = get(URI, params)
    
    if err != None:
        print(err)
        return None, None
    
    newTime = currentTime
    res = []
    for submission in obj:
        if submission['verdict'] != 'OK':
            continue
    
        timestamp = int(submission['creationTimeSeconds'])
        if timestamp <= currentTime:
            continue
        
        newTime = max(newTime, timestamp)
        res.append(submission['problem'])
    return newTime, res
