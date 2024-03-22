import json
from database import Data
from print_all_table import Print_data
from data_models.all_tabel import Persons, Labels, Tickets, Relationship


"""
Tabellen werden in json umgewandelt
"""

def get_all_persons():
    """
    Tabelle wird in json umgewandelt
    """
    person_list = Print_data.print_persons()
    for i , person in enumerate(person_list):
        person_list[i]      = Persons(
        person_id           = person[0],
        firstname           = person[1],
        lastname            = person[2],
        sector              = person[3],
        gender              = person[4],
        status              = person[5])

    return person_list

    
def get_all_labels():
    """
    Tabelle wird in json umgewandelt
    """
    label_list = Print_data.print_labels()
    for i , label in enumerate(label_list):
        label_list[i]       = Labels(
        label_id            = label[0],
        description         = label[1],
        processting_sector  = label[2])
    return label_list


def get_all_tickets():
    """
    Tabelle wird in json umgewandelt
    """
    in_all_tickets = False
    index = 0
    all_tickets  = []
    tickets_list = Print_data.print_tickets()
    for i , row_tickets in enumerate(tickets_list):
        in_all_tickets = False
        for t, tickets in enumerate(all_tickets):
            if tickets.tickets_id == row_tickets[0]:
                in_all_tickets = True
                index = t
        if not in_all_tickets : 
            all_tickets.append( Tickets(
            tickets_id          = row_tickets[0],
            level               = row_tickets[1],
            creation_date       = row_tickets[2],
            ticket_name         = row_tickets[3],
            ticket_assignee     = row_tickets[4],
            label               = []))
            index               = len(all_tickets)-1
        all_tickets[index].label.append(Labels(label_id        = row_tickets[5],   
                                            description        = row_tickets[6],
                                            processting_sector = row_tickets[7]))
    return all_tickets

def get_all_labels_from_ticket():
    """
    Tabelle wird in json umgewandelt
    """
    relation_list = Print_data.print_labels_from_ticket()
    for i , relationship in enumerate(relation_list):
        relation_list[i]    = Relationship(
        tickets_id          = relationship [0],
        label_id            = relationship [1])
    return relation_list

