# FAQ Backend Development

This project implements a backend system to manage FAQs with multilingual support using Django, `django-ckeditor` for rich text formatting, Google Translate API for automatic translations, and Redis for caching translated questions.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies](#technologies-used)
- [Installation Instructions](#installation-instructions)
- [API Usage](#api-usage)
- [Testing](#testing)

## Overview

This project allows users to manage Frequently Asked Questions (FAQs) in multiple languages. It includes:

- A **FAQ model** with api to hint the command and seprate in Hindi and Bengali.
- **WYSIWYG (What You See Is What You Get) editor** integration using `django-ckeditor` for easy formatting of answers.
- **REST API** to manage FAQs and support language selection.
- **Caching mechanism** using Redis to store translations and improve performance.
- **Automatic translation** of questions to Hindi and Bengali using Google Translate API.
- **Admin panel** for easy management of FAQs.
- **Unit tests** to verify the functionality.

## Features

- **Multilingual FAQ support**: Supports English, Hindi, and Bengali questions.
- **Rich text answers**: Answers can be formatted using a WYSIWYG editor.
- **Caching with Redis**: Cached translations for better performance.
- **Automatic translation**: Automatically generates Hindi and Bengali translations.
- **REST API**: Allows fetching FAQs with support for different languages.
- **Django Admin panel**: Easily manage FAQs and their translations.
- **Unit tests**: To proper running of all features.

## Technologies Used

- **Django**: Python-based web framework.
- **django-ckeditor**: For rich text editing in answers.
- **Redis**: For caching translated questions.
- **Django Rest Framework**: To build REST APIs.
- **Docker** (Optional): For containerization.

## Installation Instructions

Follow the steps below to get the project up and running on your local machine:

### Prerequisites

- Python 3.x
- pip (Python package installer)
- Redis (for caching)

### Step-by-Step Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/repositoryname.git
   cd repositoryname

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt

3. **Set up Redis**:
   ```
   docker run -d --name redis-server -p 6379:6379 redis

4. **Run migrations**:
    ```bash
    python manage.py migrate

5. **Create a superuser (for Django Admin)**:
    ```bash
    python manage.py createsuperuser
   
6. **Run the development server**:

    ```bash
    python manage.py runserver
   
7. **Open http://localhost:8000/admin/ in your browser to access the Django admin panel. Log in with the superuser credentials you created and start managing your FAQs.**

## API Usage
### 1. Fetch FAQs (English by default)

    curl http://localhost:8000/api/faqs/

#### Response:

    [
        {
            "question": "What is the return policy?",
            "answer": "<p>You can return items within 30 days of purchase.</p>"
        },
        ...
    ]

### 2. Fetch FAQs in Hindi
 
    curl http://localhost:8000/api/faqs/?lang=hi
**Response**:
    
    [
        {
            "question": "रिटर्न नीति क्या है?",
            "answer": "<p>आप खरीदारी के 30 दिनों के भीतर आइटम वापस कर सकते हैं।</p>"
        },
        ...
    ]
### Fetch FAQs in Bengali
 
    curl http://localhost:8000/api/faqs/?lang=bn
**Response**:
     
    [
        {
            "question": "রিটার্ন নীতি কি?",
            "answer": "<p>আপনি কেনাকাটার ৩০ দিনের মধ্যে আইটেম ফেরত দিতে পারেন।</p>"
        },
        ...
    ]
## Testing

To run unit tests and ensure the functionality is working as expected:

#### Run tests:
    python manage.py test

Tests are written to check the following:

- Model methods (save() and get_translated_question()).
- API responses for different language queries.


