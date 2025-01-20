import google.generativeai as genai
import json
from rapid_api import train_status, trainavail,pnr
#################################           GEMINI          ###########################################
def gemini_model(prompt):
    try: 
        #print("check2")
        Gemini_API_KEY = 'Gemini key'
        genai.configure(api_key=Gemini_API_KEY)
        model = genai.GenerativeModel(model_name='gemini-1.5-flash-latest')
        #print("reached model")
        response = model.generate_content(prompt)
        #print("I got gemini response")
        if response:
             #print(response)
             return response.text
        else:
             print("Error: No response from Gemini API")
             return None
    except Exception as e:
        print(f"Error loading Gemini model: {e}")
        return None

def Query(user_input, prompt):
    #print("check1")
    prompt = user_input + prompt
    res = gemini_model(prompt)
    return res

###############################  JSON RESPONSE   #######################################################
def js(details):
    if details:
        try:
            new = details[8:-5]
            extracted_details = json.loads(new)
            return extracted_details
        except json.JSONDecodeError as e:
            try:
                extracted_details = eval(details)
            except (SyntaxError, NameError):
                extracted_details = f"Error parsing JSON response: {e}"
                print(f"Error parsing JSON response: {e}")
            return extracted_details
    else:
        print("No extracted details to process")
        return None
    
# def TTS(text, lang):
#     aud_ = tts(text, lang)
#     return aud_
#####################################  PARAMETERS FOR API   ############################################

def train_availability(user_input):
    details = {
        "source": None,
        "destination": None,
        "date": None
    }
    prompt = f"Extract the following details from the user input in this format: {json.dumps(details)}\n\n user input:{user_input}"
    resp = Query(user_input, prompt)
    resp=js(resp)
    print("train details")
    print(resp)
    missed_fields=[]
    for key, value in resp.items():
        if not value:
            missed_fields.append(key)
            print(missed_fields)
    if (len(missed_fields)!=0):
        for i in missed_fields:
            print(f"Please provide your {i}")
            user_input = input("> ").strip()
            resp[i]=user_input
    src=resp['source']
    dest=resp['destination']
    doj=resp['date']
    api_response= trainavail(src,dest,doj)
    data = json.loads(api_response.text)
    api_response=json.dumps(data)
    prompt="This is a response from an api which says the available trains between stations. Give this response in an user understandable description. Give it as a continuous description. Not in bullets and numbering"
    final_response=Query(api_response,prompt)
    return final_response

def pnr_status():
    query = "Please provide your 10-digit PNR number?"
    print(query)
    details = {
        "pnr_number": None
    }
    user_input = input("> ").strip()
    prompt = f"Extract the following details from the user input in this format: {json.dumps(details)}\n\n user input:{user_input}"
    resp = Query(user_input, prompt)
    resp=js(resp)
    pnrNumber=resp['pnr_number']
    #print("pnrmu:",pnrNumber)
    api_response= pnr(pnrNumber)
    # print("response:",api_response)
    prompt="This is a response from an api which says the pnr status of the train. Give this response in an user understandable description. Give it as a continuous description. Not in bullets and numbering"
    final_response=Query(api_response,prompt)
    return final_response

def live_status():
    query = "Please provide your train number?"
    print(query)
    details = {
        "train_number": None
    }
    user_input = input("> ").strip()
    prompt = f"Extract the following details from the user input in this format: {json.dumps(details)}\n\n user input:{user_input}"
    resp = Query(user_input, prompt)
    resp=js(resp)
    print("response:",resp)
    trainNo = resp['train_number']
    api_response= train_status(trainNo)
    data = json.loads(api_response.text)
    api_response=json.dumps(data)
    prompt="This is a response from an api which says the live status of the train. Give this response in an user understandable description. Give it as a continuous description. Not in bullets and numbering"
    final_response=Query(api_response,prompt)
    return final_response

def none_handle():
    print('Please rephrase your question.')
    # user_input = input("> ").strip()
    # prompt = ("which one of the options does the above statement refer to from the given 3 options? "
    #           "(options: 1. Train availability 2. PNR status 3. Live train status). "
    #           "Don't give the explanation, give only what it is referring to from the options. "
    #           "If the statement is completely out of context give it as none.") 
    # resp = Query(user_input, prompt)
    # return resp
    main()

def case(value, user_input):
    if value == 1:
        response = train_availability(user_input)
        return response
    elif value == 2:
        response = pnr_status()
        return response
    elif value == 3:
        response = live_status()
        return response
    else:
        response = none_handle()
        return response
    
############################     MAIN   ######################################################################
def main():
    prompt = ("which one of the options does the above statement refer to from the given 4 options? "
              "(options: 1. Train availability, 2. PNR status, 3. Live train status, 4. None). "
              "Don't give the explanation, give only what it is referring to from the options.Don't give option number. Give only the option text "
              "If the statement is completely out of context or not related to railways give it as None.If there are greetings like hi, how are you? Reply with agreeting and say Ask query related to train information")
    print("Welcome to the Rail Enquiry Chat!")
    option_map = {1: "Train availability", 2: "PNR status", 3: "Live train status", 4: "None"}
    while True:
        user_input = input("> ").strip()
        print(user_input)
        resp = Query(user_input, prompt)
        print("gem:", resp)
        resp = resp.strip()
        if resp == option_map[1]:
            value=1
        elif resp == option_map[2]:
            value=2
        elif resp == option_map[3]:
            value = 3
        else:
            value=4
        # else:
        #     print("response is none")
        
    
        fin_resp = case(value, user_input)
        print(fin_resp)

    
if __name__ == "__main__":
    main()
