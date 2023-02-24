from flask import Flask, render_template, request
import boto3
app = Flask(__name__)

client = boto3.client('dynamodb')


newl=[]

global temp

@app.route('/process_form', methods=['POST'])
def process_form():
    temp=''
    name2 = request.form['name']
    slno = request.form['slno']
    name2 = slno+" "+name2
    
    print('name',name2 )
    print()
    if name2=="":
        pass
    elif name2 not in newl:
        newl.append(name2)
        temp =name2

    return render_template('home.html',name2=newl)

@app.route('/delete',methods=['POST'])
def delete():
    indexno = request.form['name1']
    newindex = int(indexno)
    newindex = newindex-1

    newl.pop(newindex)
    #print(indexno)
    return render_template('home.html',name2=newl)


@app.route('/edititem',methods=['POST'])
def edititem():
    indexno = request.form['name1']
    edata = request.form['edata']
    print(indexno)
    print(edata)
    intindex = int(indexno)
    newl[intindex]=edata
    return render_template('home.html',name2=newl)
    return 'Form Deleted successfully!'


    # Do something with the form data

    #def put_user_data(year, email, address, message):
    # response = client.put_item(
    #    TableName='user_data',
    #    Item={
    #         'address': {
    #             'S': "{}".format(name),
    #         }
    #     }
    # )
    # return response
    
    




if __name__ == '__main__':
    @app.route('/')
    def index():
        return render_template('home.html')
    app.run(debug=True)