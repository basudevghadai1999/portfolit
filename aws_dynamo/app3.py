from flask import Flask, render_template, request
import boto3
app = Flask(__name__)

client = boto3.client('dynamodb')


@app.route('/process_form', methods=['POST'])
def process_form():
    name = request.form['name']
    email = request.form['email']
    year =request.form['year']
    message =request.form['message']
    print('name',name )
    print()
    print('email',email)
    # Do something with the form data

    #def put_user_data(year, email, address, message):
    response = client.put_item(
       TableName='user_data',
       Item={
            'year': {
                'N': "{}".format(year),
            },
            'email': {
                'S': "{}".format(email),
            },
            'address': {
                'S': "{}".format(name),
            },
            'message': {
                'S': "{}".format(message),
            }
        }
    )
    return response
    return 'Form submitted successfully!'



def create_user_data():
    table = client.create_table(
        TableName='user_data',
        KeySchema=[
            {
                'AttributeName': 'year',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'email',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'year',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'email',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return 

def put_user_data(year, email, address, message):
    response = client.put_item(
       TableName='user_data',
       Item={
            'year': {
                'N': "{}".format(year),
            },
            'email': {
                'S': "{}".format(email),
            },
            'address': {
                'S': "{}".format(address),
            },
            'message': {
                'S': "{}".format(message),
            }
        }
    )
    return response
def get_user_data(year, email):
    
    try:
        response = client.get_item(       
                TableName='user_data',
                Key={
                        'year': {
                                'N': "{}".format(year),
                        },
                        'email': {
                                'S': "{}".format(email),
                        }
                    }
                )
        return response
    except:
        return 'error'
        
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    #     ## Create DynamoDB
    # user_data = create_user_data()
    # print("Create DynamoDB succeeded............")
    # print("Table status:{}".format(user_data))


    #  #  Insert in to DynamoDB
    # puser_data = put_user_data(1999, "demo@gamil.com","Jajpur Odisha", "tis is a new message")
    # print("Insert in to DynamoDB succeeded............")
    # print(puser_data)

    uuser_data = get_user_data(1999,"ghadaibasudev1234@gmail.com")
    print('user data ',uuser_data)
    if uuser_data:
       print("Get an item from DynamoDB succeeded............")
       print(uuser_data)                          
    app.run(debug=True)


