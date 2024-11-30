from fastapi import FastAPI,Request, UploadFile,File
#import keras
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import datetime
import os
from helper.chat import chain

print(chain.invoke({"input":"who are you"}))
app= FastAPI(title="Gauava deacease prediction")
app.mount("/static", StaticFiles(directory="static"), name="static")

temp= Jinja2Templates(directory="templates")
#model=keras.saving.load_model("age.keras")

@app.get("/",response_class=HTMLResponse)
async def home(request: Request):
    return temp.TemplateResponse(request=request, name="imdex.html", context={"id": id})


@app.get("/chat",response_class=HTMLResponse)
async def home(request: Request):
    return temp.TemplateResponse(request=request, name="chat.html", context={"id": id})

@app.post("/predict")
async def endreProfilbilde(images: UploadFile = File(...)):
    path=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    file_location = f"images/t{path}-{images.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(images.file.read())
    return {"status":200,"disease":'ams'}

    