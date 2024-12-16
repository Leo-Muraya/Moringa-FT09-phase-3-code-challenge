## Magazine Management System

## Description

This project implements a Magazine Management System using Object-Oriented Python and SQLAlchemy. The system consists of three main models: Author, Article, and Magazine. It demonstrates the relationships between these entities and provides methods to perform CRUD operations, as well as aggregate and association methods to retrieve meaningful data.

## Domain Relationships

An Author has many Articles.

A Magazine has many Articles.

Articles belong to both an Author and a Magazine (many-to-many relationship).

## Features

## Author Model:

Create and manage authors.

Retrieve all articles written by an author.

List magazines an author has contributed to.

## Magazine Model:

Create and manage magazines.

Retrieve all articles for a magazine.

Identify contributors and titles for a magazine.

Find authors with more than 2 contributions.

## Article Model:

Create and manage articles.

Retrieve associated author and magazine for an article.

## Technologies Used

Python: For implementing models and methods.

SQLAlchemy: For database ORM and relationship mapping.

SQLite: As the database for persistent storage.

Pytest: For unit testing.

## Installation

1. Clone the repository:

git clone < https://github.com/Leo-Muraya/Moringa-FT09-phase-3-code-challenge > 

cd <Moringa-FT09-phase-3-code-challenge>

2. Install dependencies using pipenv:

pipenv install
pipenv shell

3. Set up the database:

python database/setup.py

4. Run the application:

python app.py

## Testing

To run tests:

pytest

This will run all the test cases in the tests/ directory to ensure the functionality of the models and methods.

## Contributing

1. Fork the repository.

2. Create a new branch:

git checkout -b feature-branch

3. Commit your changes:

git commit -m "Add feature"

4. Push to the branch:

git push origin feature-branch

5. Open a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Authors

Developed by Leo Muraya.

