# Flask + SQLite REST API

A clean beginner-to-intermediate backend project built with **Python, Flask, and SQLite** to understand how REST APIs communicate with a relational database.

## Overview

This project demonstrates a complete CRUD API for managing farmers.

The application follows this flow:

```text
Client
  ↓
Flask REST API
  ↓
Python
  ↓
SQLite Database
```

## Features

* REST API with Flask
* CRUD operations
* JSON request and response handling
* SQLite database integration
* Reusable database functions
* Input validation
* Error handling
* HTTP status codes
* Farmer management API

## API Endpoints

| Method   | Endpoint        | Description         |
| -------- | --------------- | ------------------- |
| `GET`    | `/farmers`      | Get all farmers     |
| `GET`    | `/farmers/<id>` | Get a farmer by ID  |
| `POST`   | `/farmers`      | Create a new farmer |
| `PUT`    | `/farmers/<id>` | Update a farmer     |
| `DELETE` | `/farmers/<id>` | Delete a farmer     |

## Example Request

### Create Farmer

**POST** `/farmers`

```json
{
  "name": "Jai",
  "phone": "9876543210"
}
```

### Update Farmer

**PUT** `/farmers/1`

```json
{
  "name": "Jai Updated",
  "phone": "9999999999"
}
```

## Example Response

```json
{
  "message": "Farmer added successfully"
}
```

## Project Structure

```text
Flask_SQLite/
│
├── database.py
├── farmer.py
│
├── 01_app.py
├── 02_routes.py
├── 03_methods.py
├── 04_receive_data.py
├── 05_flask_sqlite.py
├── 06_get_farmers.py
├── 07_get_one_farmer.py
├── 08_update_farmer.py
├── 09_delete_farmer.py
├── 10_validation.py
│
└── farmer_market.db
```

## Installation

Clone the repository and install Flask:

```bash
pip install flask
```

## Running the Application

Run the Flask application:

```bash
python 05_flask_sqlite.py
```

The API will be available at:

```text
http://127.0.0.1:5000
```

## Technologies

* **Python**
* **Flask**
* **SQLite**
* **SQL**
* **REST API**
* **JSON**

## Learning Path

This project is part of a backend learning path:

```text
SQLite
   ↓
Python + SQLite
   ↓
Flask + SQLite
   ↓
SQLAlchemy
   ↓
PostgreSQL
   ↓
Production / Hackathon Projects
```

## Purpose

The purpose of this project is to build a strong understanding of **database operations, REST APIs, and backend development** before moving to SQLAlchemy and PostgreSQL.

---

**Status:** Completed
**Next:** SQLAlchemy
