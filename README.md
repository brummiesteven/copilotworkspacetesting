# copilotworkspacetesting

## Quiz App

This is a basic quiz app that asks for the user's name and then presents a random set of 10 questions. The questions are fetched from an external API. The app will then give the user a score out of 10 based on their answers.

### How to Run the Quiz App

1. Make sure you have Python installed on your system.
2. Install the required libraries by running `pip install requests flask`.
3. Run the quiz app by executing `python quiz_app.py` in your terminal.
4. Open your web browser and go to `http://127.0.0.1:5000/` to start the quiz.

### How to Deploy the Quiz App to Azure App Services

1. Create an Azure App Service instance.
2. Configure the App Service to use a Python runtime.
3. Deploy the code to the App Service using your preferred method (e.g., Git, FTP, Azure CLI).
4. Ensure that the `web.config` file is included in the root directory of your deployment.
5. The app should automatically start using Gunicorn as specified in the `web.config` file.
