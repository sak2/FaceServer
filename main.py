import pickle

from fastapi import FastAPI, File, UploadFile
from deepface import DeepFace
import sqlite3
import asyncio
from hypercorn.config import Config
from hypercorn.asyncio import serve
from fastapi.staticfiles import StaticFiles

# conn = sqlite3.connect(':memory:')
# cursor = conn.cursor()
# sql = '''
# CREATE TABLE IF NOT EXISTS DETECTION(
#    FACE_ID INTEGER PRIMARY KEY,
#    TS TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#    AGE INT,
#    GENDER CHAR(1),
#    NATIONALITY FLOAT,
#    EMOTION CHAR(20),
#    RAW_JSON VARCHAR
# )
# '''
#
# cursor.execute(sql)
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    obj = DeepFace.analyze(img_path="img.png", actions=['age', 'gender', 'race', 'emotion'])
    entry = (obj['age'], obj['gender'], obj['dominant_race'], obj['dominant_emotion'], pickle.dumps(obj))
    # cursor.execute('''INSERT INTO DETECTION(AGE, GENDER, NATIONALITY, EMOTION, RAW_JSON)
    #    VALUES (?, ?, ?, ?, ?)''', entry)
    return {"message": "Hello World",
            "result": obj}


@app.post("/capture/")
async def create_upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    with open(file.filename, "wb") as f:
        f.write(contents)
    print("recieved")
    return {"filename": file.filename}

# Commit your changes in the database
# conn.commit()

# Closing the connection
# conn.close()

if __name__ == '__main__':
    asyncio.run(serve(app, Config()))
