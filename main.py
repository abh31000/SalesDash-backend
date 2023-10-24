from fastapi import FastAPI
import pandas as pd

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


df = pd.read_csv("data.csv")

@app.get("/data1")
async def get_data1():
    somme_annee = df.groupby('Année')['Ventes'].sum().reset_index()
    return somme_annee.to_json(orient='records')

@app.get("/data2")
async def get_data2():
    months = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre", "Octobre", "Novembre", "Decembre"]
    df['Mois'] = pd.Categorical(df['Mois'], categories=months, ordered=True)
    somme_mois = df.groupby('Mois')['Ventes'].sum().reset_index()
    return somme_mois.to_json(orient='records')
