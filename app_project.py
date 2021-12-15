from flask import Flask, jsonify,request
app= Flask(__name__)
contact = [ 
    { 'id': 12200
    'Name': Ribhav,
    'Contact':+56473892,
    'done':True
    }] 
@app.route("/add-data",methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data!"
        },400)
    contact = [{ 'id': tasks[-1]['id']+1,'Name':request.json['Name'],'Contact':request.json.get('Contact',""),'done':False}] 
    tasks.append(task) 
    return jsonify({ "status":"success", "message": "Task added succesfully!" })

@app.route("/get-data") 
def get_task(): 
    return jsonify({ "data" : tasks })

if __name__  == '__main__':
    app.run(debug = True)  