from flask import Flask
from routes.books import books_blueprint
from middlewares.cors import init_cors
from handlers.error_handlers import handle_404, handle_500

app = Flask(__name__)

# Initialize CORS
init_cors(app)

# Register blueprints
app.register_blueprint(books_blueprint)

# Error handling
app.register_error_handler(404, handle_404)
app.register_error_handler(500, handle_500)

if __name__ == "__main__":
    app.run(debug=True)
