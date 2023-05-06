import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

appcreds = credentials.ApplicationDefault()
firebase_admin.initialize_app(appcreds, {
  'projectId': 'minion-385821',
})

db = firestore.client()
def CallFunction(request):
    request = request.args

    refer = db.collection("MinTable")
    minions = refer.get()
    
    list_of_minions = []
    for doc in minions:
        list_of_minions.append(doc.to_dict())

    required = {}
    for m in list_of_minions:
        if m["ID"] == int(request["ID"]):
            required = m
            break
    if not required:
        return "Given Minion ID is not found"
    
    return required
