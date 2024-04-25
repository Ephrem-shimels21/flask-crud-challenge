from flask import Blueprint, jsonify, request
from storage.book_storage import BookStorage
from datetime import datetime
import json

books_blueprint = Blueprint("books", __name__)
book_storage = BookStorage()


def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        raise ValueError("Invalid date format (must be YYYY-MM-DD)")


@books_blueprint.app_errorhandler(ValueError)
def handle_value_error(error):
    response = jsonify({"error": str(error)})
    response.status_code = 400
    return response


@books_blueprint.route("/books", methods=["GET"])
def get_books():
    return jsonify(book_storage.get_books()), 200


@books_blueprint.route("/books/<book_id>", methods=["GET"])
def get_book(book_id):
    book = book_storage.get_book_by_id(book_id)
    if book:
        return jsonify(book), 200
    return jsonify({"error": "Book not found"}), 404


@books_blueprint.route("/book", methods=["POST"])
def add_book():
    data = request.get_json()
    # Parse publication_year from JSON and ensure it's a valid date
    publication_year = parse_date(data.get("publication_year", ""))

    new_book = book_storage.add_book(
        data.get("title"),
        data.get("author"),
        data.get("price"),
        data.get("category"),
        publication_year,
    )
    return jsonify(new_book), 201


@books_blueprint.route("/books/<book_id>", methods=["PUT"])
def update_book(book_id):
    data = request.get_json()
    keys = ["title", "author", "price", "category", "publication_year"]
    updated_data = {key: data.get(key) for key in keys if key in data}

    if "publication_year" in updated_data:
        updated_data["publication_year"] = parse_date(updated_data["publication_year"])

    updated_book = book_storage.update_book(book_id, updated_data)
    if updated_book:
        return jsonify({"updated": updated_book}), 200
    return jsonify({"error": "Book not found"}), 404


@books_blueprint.route("/books/<book_id>", methods=["DELETE"])
def delete_book(book_id):
    if book_storage.delete_book(book_id):
        return jsonify({"message": "Book deleted successfully"}), 200
    return jsonify({"error": "Book not found"}), 404
