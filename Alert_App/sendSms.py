from twilio.rest import Client

def sendAlertToPolice():
	"""Sends an SMS message to Twilio user."""
	#My personal twilio account is used for this 
	ACC_SID = "AC8911c15093a250b00755105c03a9e826"
	AUTH_TOKEN = "67b0a61877335cb96341efc707ac2fc8"
	TWILIO_NUMBER = "+12028582643"
	MY_NUMBER = "+12404618900"
	MSG = "Help! There's a school shooter!"
	
	client = Client(ACC_SID,AUTH_TOKEN)
	
	message = client.messages \
		.create(
			body= MSG,
			from_= TWILIO_NUMBER,
			to= MY_NUMBER
		)
	
	print(message)
	