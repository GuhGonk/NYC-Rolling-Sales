import ollama

import requests
import json

import time

# def process_column_names(column_names, func_parameters):
#     prompt = f"""
#     I have the following dataframe columns that need to be parsed:
#     {column_names}
    
#     Function signature: {func_parameters}

#     Please return a json matching the pertinent information from the data as the parameters for the function.function
#     """
#     response = ollama.generate(
#         model='llama3.1:8b',
#         prompt=prompt
#     )

#     return response['response']

def query_ollama(data, function_info):
    url = "http://localhost:11434/api/generate"
    
    prompt = f"""
    Only output a JSON. Only output a JSON. Only output a JSON. Only output a JSON. Only output a JSON. Only output a JSON. Only output a JSON.
    Your response cannot exceed 100 words.
    Respond only with JSON, no explanations.
    I need to parse this data and identify the correct parameters for a function.
    
    Data to parse: {data}
    
    Function signature: {function_info}
    
    Do not explain your thought process. Do not create any extraneous text.
    Only output a JSON.
    """
    
    payload = {
        "model": "deepseek-r1",
        "prompt": prompt,
        "stream": False
    }
    
    response = requests.post(
        url,
        headers={"Content-Type": "application/json"},
        data=json.dumps(payload)
        # response_format={"type":"json_object"}
    )
    
    if response.status_code == 200:
        return response.json()["response"]
    else:
        return f"Error: {response.status_code}, {response.text}"

data = ["BOROUGH", "NEIGHBORHOOD", "BUILDING CLASS CATEGORY", "SALE PRICE", "SALE DATE"]
function_info = "makePlot(chart, data, x, y, title, xticks, xlabel, xrot, ylabel, leg_on, leg_pos, leg_outer, leg_labels, hue, palette, ax, leg_bbox)"

if __name__ == '__main__':
    start = time.time()
    result = query_ollama(data, function_info)
    print(result)
    print(f'\n{time.time() - start}')
