# Web Push Demo

_Can be tested on multiple desktop devices in same local network._
_Will not work on mobile devices due to https protocol requirement_
_in order to accept notifications._

Based on [this article](https://felixgerschau.com/web-push-notifications-tutorial/#the-technology-behind-web-push-notifications).

## How to run

### Backend

_prerequisites:_

Install Python 3.10

```
cd backend
pip install -r requirements.txt
```

_run:_

```
python -m uvicorn main:app --port 5000 --host 0.0.0.0 --reload
```

### Frontend

_prerequisites:_
Install Node 18

```
cd frontend
npm install
```

_run:_

```
npm run dev
```
