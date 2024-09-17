## Why should I learn?
- It is a flexible way to store data
- It is important knowledge to complement the toolkit when developing backend applications

## Initial steps

1. Run MongoDB service with Docker Compose:
```sh
docker compose up -d mongo # Set up MongoDB
```
2. [Set up a virtual environment](https://docs.google.com/document/d/1QI9jc3wl92B6KOrpgS-xi9OnOO1kkAm6g4pHx42Mwsk/edit#heading=h.v74wpoyxy3z)
3. Install dependencies
```sh
pip install -r requirements.txt
```
4. There is a [Python script](./server.py) that interacts with MongoDB using the pymongo library