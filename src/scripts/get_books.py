import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore
import pprint

pp = pprint.PrettyPrinter(indent=4)
cred = credentials.Certificate('')
app = firebase_admin.initialize_app(cred)

store = firestore.client()
doc_ref = store.colleciton(u'routes')

try:
    docs = doc_ref.get()
    for doc in docs:
        doc_data = doc.to_dict()
        pp.pprint(doc_data)
        print('document id | ', doc.id)
        print('printing one record | ' + doc.get('path_json'))
        print('\n')
except google.cloud.exceptions.NotFound:
    print(u'missing data')
