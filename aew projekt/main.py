from fastapi import FastAPI
from data_models.all_tabel import Persons, Labels, Tickets
import converter as cv

app = FastAPI()


@app.get("/api")
async def root():
    return{"hello":"world"}

@app.get("/api/v1/person")
async def fetch_person():
    return cv.get_all_persons();

@app.get("/api/v1/person/id")
async def fetch_person_by_id(person_id):
    return cv.Print_data.get_person_by_id(person_id);

@app.get("/api/v1/person/tickets")
async def fetch_person_ticket(person_id):
    return cv.Print_data.get_person_ticket_with_labels(person_id);

@app.post("/api/v1/person/add")
async def add_person(person : Persons):
    return  cv.Data.insert_new_person(person);

@app.delete("/api/v1/person/delete/{person_id}")
async def delete_person(person_id : int):
    return cv.Data.delete_person(person_id)



@app.get("/api/v1/label")
async def fetch_label():
    return  cv.get_all_labels();

@app.get("/api/v1/label/id")
async def fetch_label_by_id(label_id):
    return  cv.Print_data.get_label_by_id(label_id);

@app.post("/api/v1/label/add")
async def add_label(label : Labels):
    return  cv.Data.insert_new_label(label);

@app.delete("/api/v1/label/delete/{label_id}")
async def delete_plabel(label_id : int):
    return cv.Data.delete_label(label_id)



@app.get("/api/v1/tickets")
async def fetch_tickets():
    return cv.get_all_tickets();

@app.get("/api/v1/tickets/{id}")
async def fetch_tickets_by_id(id): 
    return cv.Print_data.get_ticket_by_id(id);

@app.get("/api/v1/ticket/label")
async def fetch_ticket_label():
    return cv.get_all_labels_from_ticket();

@app.post("/api/v1/ticket/add")
async def add_ticket(ticket : Tickets):
    return  cv.Data.insert_new_ticket(ticket);

@app.delete("/api/v1/ticket/delete/{ticket_id}")
async def delete_ticket(ticket_id : int):
    return cv.get_all_labels_from_ticket(ticket_id)


    