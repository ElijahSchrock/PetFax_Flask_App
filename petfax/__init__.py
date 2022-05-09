# Config
from flask import Flask

# Factory
def create_app():
    # Create Flask class instance || app instance
    app = Flask(__name__)
    # Create a route on the app instance
    @app.route('/') # The @ denotes the use of a decorater, which is a function that extends the functionality of an existing function
    def hello():
        return 'Hello, PetFax!'
    
    from . import pet
    app.register_blueprint(pet.bp)

    from . import fact
    app.register_blueprint(fact.bp)

    #return the app
    return app
