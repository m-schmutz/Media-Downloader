#!./web-env/bin/python3

#################################################################
# Server Imports 

from lib import create_app


#################################################################
# Flask app

app = create_app()


#################################################################
# Main Function

if __name__ == '__main__':
    # run flask app in debug mode
    app.run(debug=True)