# Replace these values with the actual ones from your cleaned data
financial_data = {
    "total_revenue": "Apple had a total revenue of $394.3B in 2022.",
    "net_income_change": "Apple's net income increased by 5.4% from 2021 to 2022.",
    "total_assets": "Tesla reported total assets worth $82.3B in 2022.",
    "net_income_tesla": "Tesla's net income in 2022 was $12.6B.",
    "cash_flow_microsoft": "Microsoft's operating cash flow in 2022 was $89.0B."
}
# simple_financial_chatbot.py

def simple_chatbot(user_query):
    user_query = user_query.lower()

    if "total revenue" in user_query:
        return "Apple had a total revenue of $394.3B in 2022."
    elif "net income" in user_query and "change" in user_query:
        return "Apple's net income increased by 5.4% from 2021 to 2022."
    elif "total assets" in user_query:
        return "Tesla reported total assets worth $82.3B in 2022."
    elif "net income" in user_query and "tesla" in user_query:
        return "Tesla's net income in 2022 was $12.6B."
    elif "cash flow" in user_query and "microsoft" in user_query:
        return "Microsoft's operating cash flow in 2022 was $89.0B."
    else:
        return "Sorry, I can only provide information on predefined queries."


# CLI interface
if __name__ == "__main__":
    print("Welcome to the Financial Chatbot! Ask a question or type 'exit' to quit.")
    while True:
        query = input("You: ")
        if query.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = simple_chatbot(query)
        print("Chatbot:", response)
