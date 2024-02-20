from flask import Flask, request, jsonify

app = Flask(__name__)

def is_valid_api_key(key):
# Placeholder for actual database lookup
  return key == "LONg_hot_Summer_57@1"
  #return key == "test"

@app.route('/api/message', methods=['GET'])

#Example call
#/api/message?api_key=LONg_hot_Summer_57@1&arg='1'

def get_message():

  # Making a GET request

  message = request.args.get('arg')
  print(message)
  
  api_key = request.args.get('api_key')
  print(api_key)
  print(is_valid_api_key(api_key))
  if not api_key or not is_valid_api_key(api_key):
      return jsonify({"error": "Invalid or missing API key"}), 403

    
    # Retrieve the message from the query parameter
#    message = request.args.get('message', 'Hello, World!')
  if "12345" in message.lower():
      outdat=({"name": "Bill Payer", "monthly_income": "4500", "loan_repayment": "1500"})
  elif "1" in message.lower():
      outdat=({"name": "Penny Pincher", "monthly_income": "2500", "loan_repayment": "500"})
  elif "2" in message.lower():
      outdat=({"name": "Cash O'Demand", "monthly_income": "4000", "loan_repayment": "2500"})
  else:
      outdat=({"name": "Lottie Bucks", "monthly_income": "9500", "loan_repayment": "1000"})
  return jsonify({'message': outdat})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


# Include the message after the get
# example usage: http://<your-replit-url>/api/message?message=YourCustomMessage
