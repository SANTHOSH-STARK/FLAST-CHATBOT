from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load the saved model using pickle
model_filename = "responser.pkl"
with open(model_filename, 'rb') as model_file:
    loaded_model = pickle.load(model_file)

@app.route('/process_message', methods=['POST'])
def process_message():
    data = request.get_json()
    user_message = data.get('message', '')

    # Predict response using the loaded model
    predicted_response = loaded_model.predict([user_message])
    print(predicted_response)
    return jsonify({'response': predicted_response[0]})

if __name__ == '__main__':
    app.run(debug=True)
