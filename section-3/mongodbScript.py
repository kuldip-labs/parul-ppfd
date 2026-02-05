import pymongo
from pymongo import MongoClient

# 1. Connection
# Replace the URI if you are using MongoDB Atlas
client = MongoClient("mongodb://localhost:27017/")
db = client["company_db"]
users = db["users"]

def run_crud_demo():
    # # --- CREATE ---
    # print("--- Creating Data ---")
    # user_data = {"name": "Alice", "age": 30, "job": "Engineer"}
    # result = users.insert_one(user_data)
    # print(f"Inserted ID: {result.inserted_id}\n")

    # --- READ ---
    print("--- Reading Data ---")
    # Find one specific user
    user = users.find_one({"name": "Alice"})
    print(f"Found: {user}\n")

    # --- UPDATE ---
    print("--- Updating Data ---")
    # Update Alice's age to 31
    users.update_one({"name": "Alice"}, {"$set": {"age": 31}})
    print("Update complete.\n")

    # --- DELETE ---
    print("--- Deleting Data ---")
    delete_result = users.delete_one({"name": "Alice"})
    print(f"Deleted count: {delete_result.deleted_count}\n")

if __name__ == "__main__":
    run_crud_demo()