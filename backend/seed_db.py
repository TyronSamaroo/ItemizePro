import argparse
from sqlalchemy.orm import Session
from database import SessionLocal, User, Item

def seed_db(delete: bool):
    db = SessionLocal()

    if delete:
        # Delete all users and items
        db.query(User).delete()
        db.query(Item).delete()

    # Create some users
    users = [
        {"name": "Alice", "email": "alice@example.com"},
        {"name": "Bob", "email": "bob@example.com"},
    ]

    for user in users:
        db_user = db.query(User).filter(User.email == user["email"]).first()
        if not db_user:
            db_user = User(name=user["name"], email=user["email"])
            db.add(db_user)

    # Create some items
    items = [
        {"name": "Item1", "description": "This is item 1"},
        {"name": "Item2", "description": "This is item 2"},
        {"name": "Item3", "description": "This is item 3"},
        {"name": "Item4", "description": "This is item 4"},

    ]

    for item in items:
        db_item = db.query(Item).filter(Item.name == item["name"]).first()
        if not db_item:
            db_item = Item(name=item["name"], description=item["description"])
            db.add(db_item)

    db.commit()
    db.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Seed the database.')
    parser.add_argument('-d', '--delete', action='store_true', help='Delete all data before seeding')
    args = parser.parse_args()

    seed_db(args.delete)