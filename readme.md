# Web Push Demo

Based on [this article](https://felixgerschau.com/web-push-notifications-tutorial/#the-technology-behind-web-push-notifications).

### Run Backend

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

### Run Frontend

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
