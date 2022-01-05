import requests
from datetime import datetime


APP_ID="yourapiid"
API_KEY="yourapikey"

URL="https://trackapi.nutritionix.com/v2/natural/exercise"
URL_SHEETY="https://api.sheety.co/dba1aef35ca8dfa2a7d23aad2930c75d/workoutTracking/workouts"

validacion={
    "x-app-id":APP_ID,
    "x-app-key":API_KEY
}

datos={
    "query":input("Tell me which exercises you did: "),
    "gender":"male",
    "weight_kg":71,
    "height_cm":167,
    "age":22
}

respuesta=requests.post(url=URL,json=datos,headers=validacion)
resultados=respuesta.json()
fecha=datetime.now().strftime("%d/%m/%Y")
hora=datetime.now().strftime("%X")

print(resultados)

bearer_header={
    "Authorization": "Bearer yourbearer"
}
for i in resultados["exercises"]:
    excel = {
        "workout": {
            "date": fecha,
            "time":hora,
            "exercise": i["name"].title(),
            "duration": i["duration_min"],
            "calories": i["nf_calories"]
        }
    }

    excel_peticion = requests.post(url=URL_SHEETY, json=excel,headers=bearer_header)

    print(excel_peticion.text)


