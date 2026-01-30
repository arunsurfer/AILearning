def agent_response(user_message):
    try:
        response =  f"Agent response: you said -> {user_message}"
        return response
    except Exception as e:
        return f"An error occurred: {str(e)}"
    

user_input = input("Enter your message: ")


result = agent_response(user_input)

print(result)