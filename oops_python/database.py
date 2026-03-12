import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URL = "mongodb://localhost:27017"

client = AsyncIOMotorClient(MONGO_URL)

db = client["library_db"]

books_collection = db["books"]
users_collection = db["users"]
loans_collection = db["loans"]
async def check_db_connection():
    try:
        await client.admin.command("ping")
        print("✅ MongoDB connection successful")
    except Exception as e:
        print("❌ MongoDB connection failed")
        print(e)