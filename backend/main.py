from json import loads, dumps
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from pywebpush import webpush


PUBLIC_KEY = "BMrfFtMtL9IWl9vchDbbbYzJlbQwplyZ_fbv8Pei8gPNna_Dr1O-Ng7U7fy0LLqz5RKIxEytTIzyk6TLrcKbN30"
PRIVATE_KEY = "E5gpbs9Y6r5TscHC64Ce9-hXojA9I1qQL0kuvX8Jz5Y"

VAPID_CLAIMS = {"sub": "mailto:dupa@test.com"}


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["localhost", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Keys(BaseModel):
    auth: str
    p256dh: str


class Subscription(BaseModel):
    endpoint: str
    expirationTime: int | None
    keys: Keys


@app.post("/subscription")
async def subscribe(subscription: Subscription):
    db_file = open("db.json", "r+")
    db = loads(db_file.read())

    db["subscriptions"].append(subscription.dict())

    db_file.seek(0)
    db_file.write(dumps(db))
    db_file.close()

    return {"success": True}


@app.get("/broadcast")
async def broadcast():
    db_file = open("db.json", "r")
    db = loads(db_file.read())

    subscriptions = db["subscriptions"]

    for subscription in subscriptions:
        wb = webpush(
            subscription,
            data=dumps({"title": "DUPA!", "body": "Dupa from backend"}),
            vapid_private_key=PRIVATE_KEY,
            vapid_claims=VAPID_CLAIMS,
        )
        print(vars(wb))

    db_file.close()

    return {"success": True}
