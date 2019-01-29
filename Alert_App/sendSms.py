from twilio.rest import Client
 
def sendAlertToPolice(device_id_num,default_msg="Help! There's a school shooter!", default_number="+12404618900",addLocation=False,location_str=""):
	"""Sends an SMS message to Twilio user."""
	#My personal twilio account is used for this 
	ACC_SID = "AC8911c15093a250b00755105c03a9e826"
	AUTH_TOKEN = "67b0a61877335cb96341efc707ac2fc8"
	TWILIO_NUMBER = "+12028582643"
	MY_NUMBER = default_number
	
	MSG = default_msg + "\n Device number: " + str(device_id_num)
	if addLocation:
		MSG = default_msg + location_str

	client = Client(ACC_SID,AUTH_TOKEN)

	message = client.messages \
		.create(
			body= MSG,
			from_= TWILIO_NUMBER,
			to= MY_NUMBER
		)

	print(message)