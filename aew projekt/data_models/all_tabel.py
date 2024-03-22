from typing import Optional
from pydantic import BaseModel


class Persons(BaseModel):
    person_id   : Optional[int]
    firstname   : str
    lastname    : str
    sector      : Optional[str]
    gender      : Optional[str]
    status      : Optional[str]

class Labels(BaseModel):
    label_id            : Optional[int]
    description         : Optional[str]
    processting_sector  : Optional[str]


class Tickets(BaseModel):
    tickets_id      :  Optional[int]
    level           :  Optional[int]
    creation_date   :  Optional[str]
    ticket_name     :  str
    ticket_assignee :  int
    label           :  list[Labels]

class Relationship(BaseModel):
    tickets_id      :  Optional[int]
    label_id        :  Optional[int]



class person_ticket(BaseModel):
    firstname   : Optional[str]
    tickets     : list[Tickets]

