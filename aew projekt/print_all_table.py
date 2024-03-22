from configuration import config
import psycopg2
import psycopg2.extras
from data_models.all_tabel import Persons, Labels, Tickets, person_ticket

"""
Tabellen werden von Datenbank ausgegeben. Entweder die ganze Tabelle oder ein bestimmte, teil davon.
"""
class Print_data:
    conn = None
    cur = None
    def print_persons():
        """
        Tabelle Persons wird ausgegeben und alles Liste zurückgegeben.
        """
        try:
            params = config()
            with psycopg2.connect(**params) as conn:
                with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                    cur.execute('SELECT * FROM person')          
                    person = [] 
                    for record in cur.fetchall():
                        person.append (record)
                    conn.commit()                              #Tabelle PERSON wird in List eingespeichert
                    return person
                                    
        except Exception as error:
            print(error)

        finally: 
            if conn is not None:
                    conn.close()
    
    def get_person_by_id(person_id : int):
        """
        Ein Teil von Tabelle Person wird ausgegeben und alles Liste zurückgegeben.
        """
        try:
            params = config()
            with psycopg2.connect(**params) as conn:
                with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur: 
                        
                    cur.execute('SELECT * FROM  person where person_id = {0}  '.format(person_id))   #filtern
                    
                    person_list = []
                    for record   in cur.fetchall():
                        person_list.append(record)
                    
                    for i , person in enumerate(person_list):
                        person_list[i] = Persons(
                        person_id = person[0] ,
                        firstname = person[1],
                        lastname = person[2],
                        sector = person[3],
                        gender = person[4],
                        status = person[5])
                    
                    conn.commit()
                    return person_list
                
        except Exception as error:
            print(error)
        finally: 
            if conn is not None:
                    conn.close()

    def get_person_ticket_with_labels(person_id : int):
        """
        Der Person wird mit dem dazugehörigen Tickets ausgegeben.
        """
        try:
            params = config()
            with psycopg2.connect(**params) as conn:
                with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur: 
                    
                    cur.execute('''SELECT  person.firstname, tickets.*,  label.*
                                   from person INNER JOIN tickets on person.person_id = {0} and tickets.ticket_assignee = {0} 
                                   left JOIN relationship on tickets.tickets_id = relationship.tickets_id 
                                   left Join label on label.label_id = relationship.label_id ;'''.format(person_id))   #filtern / Ausgeben von dem Ticket und die Beschreibung
                    
                    information_for_person = []
                    for record in cur.fetchall():
                        information_for_person.append(record)
                    for i, i_f_p in enumerate(information_for_person):
                        information_for_person[i] = person_ticket(
                            firstname             = i_f_p[0],
                            tickets               = [Tickets(
                            tickets_id            =  i_f_p[1],
                            level                 =  i_f_p[2],
                            creation_date         =  i_f_p[3],
                            ticket_name           =  i_f_p[4],
                            ticket_assignee       =  i_f_p[5],
                            label                 = [Labels(
                            label_id              = i_f_p[6],
                            description           = i_f_p[7],
                            processting_sector    = i_f_p[8]
                            )])])
                        
                    conn.commit()
                    if len(information_for_person) == 0:
                        return "Kein eintrag"
                    else:
                        return information_for_person
        except Exception as error:
            print(error)
        finally: 
            if conn is not None:
                    conn.close()



    def print_labels():
        """
        Tabelle labels wird ausgegeben und alles Liste zurückgegeben.
        """             
        try:
            params = config()
            with psycopg2.connect(**params) as conn:
                with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:                    
                    cur.execute('SELECT * FROM label')  
                    label = []   

                    for record in cur.fetchall():
                        label.append (record)

                    conn.commit()                                   #Tabelle lABEL wird in List eingespeichert
                    return label
               
        except Exception as error:
            print(error)

        finally: 
            if conn is not None:
                conn.close()
    
    def get_label_by_id(label_id : int):
        """
        Ein Teil von Tabelle labels wird ausgegeben und alles Liste zurückgegeben.
        """  
        try:
            params = config()
            with psycopg2.connect(**params) as conn:
                with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:    
                    cur.execute('SELECT * FROM  label where label_id = {0}  '.format(label_id)) #filtern
                    
                    label_list = []
                    for record in cur.fetchall():
                        label_list.append(record)

                    """
                    Tabelle wird in json umgewandelt
                    """
                
                    for i , label in enumerate(label_list):
                        label_list[i] = Labels(
                        label_id  = label[0] ,
                        description = label[1],
                        processting_sector = label[2])
                    conn.commit()
                    return label_list
                
        except Exception as error:
            print(error)

        finally: 
            if conn is not None:
                    conn.close()

                  
    def print_tickets():
        """
        Tabelle tickets wird ausgegeben und alles Liste zurückgegeben.
        """
        try:
            params = config()
            with psycopg2.connect(**params) as conn:
                with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur: 
                        
                    cur.execute(''' SELECT distinct tickets.*,  label.*
                                    from tickets INNER JOIN relationship on tickets.tickets_id = relationship.tickets_id  
                                    left Join label on label.label_id = relationship.label_id ;''') 
                    tickets = []  
                    for record in cur.fetchall():
                        tickets.append(record)
                    conn.commit()
                    
                    return tickets
                
        except Exception as error:
            print(error)

        finally: 
            if conn is not None:
                    conn.close()
    
    def get_ticket_by_id(tickets_id : int):

        """
        Ein Teil von Tabelle tickets wird ausgegeben und alles Liste zurückgegeben.
        """
        try:
            params = config()
            with psycopg2.connect(**params) as conn:
                with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:            
                    cur.execute('SELECT * FROM  tickets where tickets_id = {0}  '.format(tickets_id)) #filtern
                    tickets_list = []
                    for record in cur.fetchall():
                       tickets_list.append(record)
                    

                    """
                    Tabelle wird in json umgewandelt
                    """

                    for i , row_tickets in enumerate(tickets_list):

                        tickets_list[i]     = Tickets(
                        tickets_id          = row_tickets[0],
                        level               = row_tickets[1],
                        creation_date       = row_tickets[2],
                        ticket_name         = row_tickets[3],
                        ticket_assignee     = row_tickets[4],
                        label               = [])
                    conn.commit()    
                    return tickets_list                         
        except Exception as error:
            print(error)

        finally: 
            if conn is not None:
                    conn.close()



    def print_labels_from_ticket():
        """
        Tabelle tickets wird ausgegeben und alles Liste zurückgegeben.
        """
        try:
            params = config()
            with psycopg2.connect(**params) as conn:
                with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur: 
                        
                    cur.execute('SELECT * FROM  relationship') 
                    relationship = []  
                    for record in cur.fetchall():
                        relationship.append(record)
                    conn.commit()
                    
                    return relationship
                
        except Exception as error:
            print(error)

        finally: 
            if conn is not None:
                    conn.close()
    
    