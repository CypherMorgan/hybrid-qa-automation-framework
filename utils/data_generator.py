from faker import Faker
import random

fake = Faker()

# products that exist on demowebshop.tricentis.com
KNOWN_PRODUCTS = [
    "build your own computer",
    "simple computer",
    "laptop",
    "smartphone",
    "tablet",
    "camera",
    "book",
    "jeans",
    "shirt",
    "shoes"
]

def user_profile():
    """registration-ready user data"""
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "password": "Password123"
    }

def existing_user():
    """returns creds from config/data for convenience"""
    from config.config_reader import ConfigReader
    return {
        "email": ConfigReader.get_username(),
        "password": ConfigReader.get_password()
    }

def shipping_address():
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "company": fake.company(),
        "street": fake.street_address(),
        "city": fake.city(),
        "state": fake.state_abbr(),
        "zip": fake.zipcode(),
        "country": "United States",
        "phone": fake.phone_number()
    }

def billing_address():
    """same shape as shipping, but can differ in real flows"""
    return shipping_address()

def product_search_term():
    return random.choice(KNOWN_PRODUCTS)

def product_review():
    """random review text for product pages that support it"""
    ratings = [1, 2, 3, 4, 5]
    titles = [
        "great product",
        "does the job",
        "not bad",
        "exactly what i needed",
        "could be better"
    ]
    return {
        "title": random.choice(titles),
        "text": fake.paragraph(nb_sentences=2),
        "rating": random.choice(ratings)
    }
