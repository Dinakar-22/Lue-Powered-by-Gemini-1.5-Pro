**Title** : Streamlit Chatbot Using Gemini 1.5 Pro API

**Description**

This project sets up a Streamlit application to create a chatbot using the Gemini 1.5 Pro API. Streamlit is an open-source app framework in Python used to create and share custom web apps. The Gemini 1.5 Pro API is used to handle natural language processing tasks.

Table of Contents

* Prerequisites
* Installation
* Configuration
* Running the Application
* Project Structure
* Contributing
* License

**Prerequisites**

Before you begin, ensure you have met the following requirements:

You have installed Python 3.7 or later.
You have a basic understanding of Python, Streamlit, and REST APIs.
You have a valid API key for the Gemini 1.5 Pro API.
Installation

**Clone the Repository**

`git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name`

**Create a Virtual Environment**

It is recommended to use a virtual environment to manage your dependencies.

`python -m venv venv`

source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

**Install Dependencies**

Use pip to install the necessary dependencies from the requirements.txt file.

`pip install -r requirements.txt`

**Configuration**

Set Up Environment Variables

Create a .env file in the root directory of the project and add your Gemini 1.5 Pro API key:

`GEMINI_API_KEY=your_gemini_api_key`

**Update config.py**

Ensure your config.py file correctly reads the API key from the .env file:


```import os
from dotenv import load_dotenv
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
```
**Running the Application**

Once the dependencies are installed and the configuration is set, you can start the Streamlit server.


`streamlit run app.py`

This command will start a local server, and you can view the application by navigating to http://localhost:8501 in your web browser.

**Project Structure**
A brief overview of the project structure:

```your-repository-name/
├── app.py                # Main application file
├── config.py             # Configuration file for API keys
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── .env                  # Environment variables
└── .gitignore            # Git ignore file
```

**License**

This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to reach out if you have any questions or need further assistance!

Happy coding! 🚀
