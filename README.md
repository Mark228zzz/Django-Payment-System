# Django Payment System

## Overview

This Django-based payment system integrates Stripe to handle subscriptions. Users can subscribe to a plan and manage their payments securely.

## Features

* Stripe subscription integration
* Secure payment processing
* Django backend

## Installation

Clone the repository:

```bash
git clone https://github.com/Mark228zzz/Django-Payment-System.git
cd Django-Payment-System
```

Create a virtual environment:

```bash
pipenv install django stripe
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## Configuration

Set up environment variables. Create a `.env` file and add:

```bash
STRIPE_PUBLIC_KEY=your_stripe_public_key
STRIPE_SECRET_KEY=your_stripe_secret_key
STRIPE_PRICE_ID=your_stripe_price_id
```

Apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

Running the Application:

```bash
python manage.py runserver
```

## Usage

1. Open http://127.0.0.1:8000/

2. Click the Subscribe button

3. Complete the payment using Stripe checkout

## License

MIT License
