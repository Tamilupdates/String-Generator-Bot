from motor.motor_asyncio import AsyncIOMotorClient as MongoCli

import config


mongo = MongoCli(config.DATABASE_URL)
db = mongo.StringGen
