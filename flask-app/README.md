# Flask Jackpot Game

This project is a simple Flask web application that simulates a jackpot game. Users can visit the web application, and the server will randomly determine if they win a jackpot based on a rolling mechanism.

## Project Structure

```
flask-app
├── app.py                # Main entry point of the Flask application
├── templates
│   └── index.html       # HTML template for rendering the output
├── static
|   |── images           # Holds images for the app
|   |── audio            # Holds audio for the app
│   ├── css              # Directory for CSS files
│   └── js               # Directory for JavaScript files
├── requirements.txt      # Lists dependencies for the project
└── README.md             # Documentation for the project
```

## Requirements

To run this application, you need to have Python and Flask installed. You can install the required packages using the following command:

```
pip install -r requirements.txt
```

## Running the Application

1. Navigate to the project directory:

   ```
   cd flask-app
   ```

2. Run the application:

   ```
   python app.py
   ```

3. Open your web browser and go to `http://127.0.0.1:5000/` to see the application in action.

## Features

- Randomly rolls a number to determine if the user wins a jackpot.
- Displays results dynamically using Jinja2 templating.
- Simple and interactive user interface.

## License

This project is open-source and available under the MIT License.