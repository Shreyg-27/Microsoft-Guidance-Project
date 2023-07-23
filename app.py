# import pandas as pd
# from flask import Flask, render_template, request
# from transformers import pipeline
#
# app = Flask(__name__)
#
# # Load the dataset
# csv_file_path = "Microsoft-Guidance (1).csv"
# data = pd.read_csv(csv_file_path)
# data.columns = data.columns.str.strip()
# questions = data["Questions"].tolist()
# answers = data["Answers"].tolist()
# question_answer_map = dict(zip(questions, answers))
#
# # Load the GPT-2 generator
# generator = pipeline("text-generation", model="gpt2")
#
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
#
# @app.route('/generate', methods=['POST'])
# def generate():
#     query = request.form['question']
#
#     # Query the GPT-2 model to generate a response
#     response = generator(query, max_length=200, num_return_sequences=1)[0]['generated_text']
#
#     # Trim the response to the nearest full stop
#     end_index = response.find(".", 0, 200)
#     if end_index != -1:
#         trimmed_response = response[:end_index + 1]
#     else:
#         trimmed_response = response
#
#     # Find the matching question in the dataset
#     matching_question = next((q for q in question_answer_map.keys() if q.lower() in response.lower()), None)
#
#     if matching_question:
#         matching_answer = question_answer_map[matching_question]
#         return render_template('result.html', query=query, answer=matching_answer)
#     else:
#         return render_template('result.html', query=query, answer=trimmed_response)
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

import pandas as pd
from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Read the CSV file into a pandas DataFrame
csv_file_path = "Microsoft-Guidance (1).csv"
data = pd.read_csv(csv_file_path)

# Extract the questions and answers from the DataFrame
data.columns = data.columns.str.strip()
questions = data["Questions"].tolist()
answers = data["Answers"].tolist()
question_answer_map = dict(zip(questions, answers))

# Load the GPT-2 generator
generator = pipeline("text-generation", model="gpt2")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    query = request.form['question']

    # Query the augmented LLMs using Hugging Face's pipeline
    num_responses = 5
    responses = generator(query, max_length=200, num_return_sequences=num_responses)

    # Filter and choose the most appropriate response
    filtered_responses = []
    for res in responses:
        generated_text = res['generated_text']
        matching_question = next((question for question in question_answer_map.keys() if question.lower() in generated_text.lower()), None)
        if matching_question:
            filtered_responses.append((matching_question, question_answer_map[matching_question]))

    if filtered_responses:
        # Sort the filtered responses based on relevance (optional)
        filtered_responses.sort(key=lambda x: len(x[0]), reverse=True)

        # Choose the most relevant response from the filtered responses
        matching_question, response = filtered_responses[0]
        return render_template('result.html', query=query, answer=response)
    else:
        # If no matching question is found, choose the first generated response
        response = responses[0]['generated_text']
        return render_template('result.html', query=query, answer=response)

if __name__ == '__main__':
    app.run(debug=True)

