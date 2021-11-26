from flask import Flask,jsonify,request
app = Flask(__name__)
tasks =[
    {
        'id':1,
        'title': u'Buy Groceries',
        'description': u'Milk,Chesse,Fruit',
        'done':False
    },
    {
        'id':2,
        'title': u'Learn Python',
        'desciption': u'Learning about How to create a Web Api',
        'done':False
    }
]
@app.route('/add-data',methods=['POST'])
def add_task():
    if not request.json:
        return jsonify({
            'status':'error',
            'message':'Please provide the Data'
        },400)
    task = {
        'id': tasks[-1]['id']+1,
        'title': request.json['title'],
        'description':request.json.get('description',""),
        'done':False

    }   
    tasks.append(task)
    return jsonify({
        'status':'success',
        'message':'Taks added Successfully'
    }) 
@app.route('/get-data')
def get_task():
    return jsonify({
        'data':tasks
    })
if(__name__=='__main__'):
    app.run(debug = True)    