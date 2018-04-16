
import boto3
import random
import string




def authenticate(user, passw):
	"""
	User inputs username and password;
	If user does have an account then check if username and password match
	"""
	client = boto3.client('dynamodb')
	response = client.get_item(
		TableName='user_table',
		Key={		
			'Username': {
				'S': user
			}
			'Password': {
				'S': passw
			} 
		}`
	)

	return response


def createUser(user, passw):

	client = boto3.client('dynamodb')
	response = client.put_item(
		TableName='user_table',
		Item={
			'Username':{
				'S': user
			},
			'Password':{
				'S': passw
			}
		}
	)
	return response


def deleteUser(user, passw):
	
	client = boto3.client('dynamodb')
	response = client.delete_item(
		TableName='user_table',
		Key={
			'Username':{
				'S': user
			}
		}
	)
	return response


def createUser_hander(event, context):
	"""
	Handling lambda to create user in the db
	"""
	user = event['user']
	passw = event['passw']
	response = createUser(user, passw)
	return {'Response':response}


def login_handler(event, context):
	"""
	Handling lambda to authenticat user login by checking db
	"""
	user = event['user']
	passw = event['passw']
	response = authenticate(user, passw)
	return {'Response': response}