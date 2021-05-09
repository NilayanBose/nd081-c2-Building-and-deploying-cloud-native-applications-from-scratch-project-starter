import azure.functions as func
import pymongo

def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()

    if request:
        try:
            url = "mongodb://testdb-cosmos:N7COIxSwtqVlCFLLAz5ZsbKMj0OkP8ecnfnJ26v79wAODOWelcvVaOw19Ta7uELKyCyLNfsqyWmO573cLWWoMw==@testdb-cosmos.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@testdb-cosmos@"
            client = pymongo.MongoClient(url)
            database = client['db']
            collection = database['advertisements']
            print(request)
            rec_id1 = collection.insert_one(eval(request))

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )