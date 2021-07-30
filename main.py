from flask import Flask,jsonify, request

app =Flask(__name__)
tasks=[
    {
        'id':1,
        'name':u"Aathmika",
        "contact":9841041487,
        "done":False
    },
    {
        'id':2,
        'name':u"Anierudh",
        'contact':9841041487,
        'done':False
    }
]
@app.route("/addData",methods=["POST"])
 
def addTask():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data !"
        },400)
    task={
        "id":tasks[-1]["id"]+1,
        "name":request.json["name"],
        "contact":request.json.get("Contact",""),
        "done":False
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message":"task added successfully"
    })

@app.route("/getData")
def getTask():
    return jsonify({
        "data":tasks
    })

if (__name__=="__main__"):
    app.run(debug=True)