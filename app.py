from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        query = request.form["query"].lower()

        if "total revenue" in query:
            response = "Apple had a total revenue of $394.3B in 2022."
        elif "net income" in query and "change" in query:
            response = "Apple's net income increased by 5.4% from 2021 to 2022."
        elif "total assets" in query:
            response = "Tesla reported total assets worth $82.3B in 2022."
        elif "net income" in query and "tesla" in query:
            response = "Tesla's net income in 2022 was $12.6B."
        elif "cash flow" in query and "microsoft" in query:
            response = "Microsoft's operating cash flow in 2022 was $89.0B."
        else:
            response = "Sorry, I can only provide information on predefined queries."

    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
