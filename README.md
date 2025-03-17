# Django REST Framework Tutorial

This project follows the official Django REST Framework (DRF) tutorial to learn and understand the basics of building APIs with Django.

## Requirements

-   Python 3.9
-   Django
-   djangorestframework

## Installation

1.  **Clone the repository**

```bash
git clone https://github.com/codegeek004/django_rest_framework
cd django_rest_framework

```

2.  **Create a virtual environment and activate it**

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate

```

3.  **Install the dependencies**

```bash
pip install -r requirements.txt

```

## Running the Server

```bash
python manage.py runserver

```

By default, the server will start at `http://127.0.0.1:8000`.

## Project Overview

This project implements:

-   Basic Django models.
-   Serializers for transforming data into JSON.
-   API views using Django REST Framework.
-   URL routing for API endpoints.
-   Browsable API interface provided by DRF.

## API Endpoints

-   `GET /api/items/`: List all items.
-   `POST /api/items/`: Create a new item.
-   `GET /api/items/{id}/`: Retrieve a specific item.
-   `PUT /api/items/{id}/`: Update a specific item.
-   `DELETE /api/items/{id}/`: Delete a specific item.

## Testing the API

You can test the API using tools like:

-   [Postman](https://www.postman.com/)
-   `curl`
-   Browsable API interface at `http://127.0.0.1:8000/api/`

### Example Using Curl

```bash
curl -X GET http://127.0.0.1:8000/api/items/

```

### Example Using Requests in Python

```python
import requests
response = requests.get("http://127.0.0.1:8000/api/items/")
print(response.json())

```

## Note

-   Replace `'127.0.0.1:8000'` with your actual API URL if different.
-   Ensure the server is running before sending requests.

## License

This project is licensed under the MIT License.
