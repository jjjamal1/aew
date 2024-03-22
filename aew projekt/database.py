import psycopg2
import names 
import random
import psycopg2.extras
from configuration import config
from data_models.all_tabel import Persons, Labels, Tickets
class Data:
    conn = None
    cur = None
              
    def create_persons():
        """
        Die Tabelle „Person“ wird erstellt und mit zufälligen Werten eingefühlt
        """
        try:
            params = config()
            with psycopg2.connect(**params) as conn:
                with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                    cur.execute('DROP TABLE IF EXISTS person CASCADE')      #Tabelle PERSON wird gelöscht
                    create_script_person= ''' CREATE TABLE IF NOT EXISTS person (       
                                        person_id   SERIAL PRIMARY KEY,
                                        firstname   varchar(35) NOT NULL,
                                        lastname    varchar(35) NOT NULL,
                                        sector      varchar(50) NOT NULL,
                                        gender      varchar(20) NOT NULL,
                                        work_status varchar(200)
                                        ) '''   #Tabelle PERSON wird erstellt
                    cur.execute(create_script_person)
                    cur.execute('TRUNCATE TABLE person CASCADE') #Werte werden gelöscht aber die Tabelle nicht
                    insert_script_person = 'INSERT INTO person ( firstname, lastname, gender, work_status, sector ) VALUES (  %s, %s, %s, %s, %s)' 

                    for i in range(1,11):
                        work_status_now = ("busy", "vacation", "available")
                        work_status = random.choice(work_status_now)
                        sectors = ("logistics", "develop", "systen integration")
                        sector = random.choice(sectors)   

                        if i % 2 == 0:
                            insert_value_person = ( names.get_first_name('female'), names.get_last_name(), "female", work_status, sector)

                        else:
                            insert_value_person = ( names.get_first_name('male'), names.get_last_name(), "male", work_status, sector)

                        cur.execute(insert_script_person, insert_value_person)
                    
                    conn.commit()

        except Exception as error:
            print(error)

        finally: 
            if conn is not None:
                conn.close() 

    def insert_new_person(person : Persons):  # Ein Person wird hinzugefügt
        guy = None
        try:
            params = config()
            with psycopg2.connect(**params) as conn:             
                with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                    #cur.execute('ALTER SEQUENCE person_person_id_seq RESTART WITH order by person_id desc limit 1;')                   
                    insert_script_person = 'INSERT INTO person ( firstname, lastname, gender, work_status, sector ) VALUES (  %s, %s, %s, %s, %s) returning *'                     
                    insert_value_person = ( person.firstname, person.lastname, person.gender, person.status, person.sector)
                    cur.execute(insert_script_person,insert_value_person)                    
                    guy = cur.fetchone()
                    conn.commit()

        except Exception as error:
            print(error)

        finally: 
            if conn is not None:
                conn.close() 
        print(guy)  
     
    def delete_person(person_id : int): # Ein Person wird gelöcht
        print(person_id)
        try:
            params = config()
            with psycopg2.connect(**params) as conn:
                with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur: 
                        
                    cur.execute('DELETE  FROM  person where person_id = {0}  '.format(person_id))   #filtern                    
                
        except Exception as error:
            print(error)

        finally: 
            if conn is not None:
                    conn.close()


    def create_labels():
        """
        Die Tabelle "Label“ wird erstellt und mit zufälligen Werten eingefühlt.
        """
        try:
            params = config()
            with psycopg2.connect(**params) as conn:
                with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                    cur.execute('DROP TABLE IF EXISTS label CASCADE')        #Tabelle LABEL wird gelöscht

                    create_script_label = ''' CREATE TABLE IF NOT EXISTS label (
                                        label_id            SERIAL PRIMARY KEY,
                                        description         varchar(255) NOT NULL,
                                        processting_sector  varchar(30) NOT NULL
                                        )'''             #Tabelle LABEL wird erstellt
                    cur.execute(create_script_label)
                    cur.execute('TRUNCATE TABLE label CASCADE')        #Werte werden gelöscht aber die Tabelle nicht
                    insert_script_label = 'INSERT INTO label ( description, processting_sector) VALUES (  %s, %s)'
                    
                    for i in range(1,11):
                        description_labels = ("Musst be done in a month","Musst be done in tow weeks", "Musst be done in three days" )
                        description_label = random.choice(description_labels)

                        processting_sectors_label = ("develop", "systen integration", "logistics")
                        processting_sector_label = random.choice(processting_sectors_label)
                        insert_value_label = (  description_label, processting_sector_label)
                        cur.execute(insert_script_label, insert_value_label)
                    conn.commit()
                    
        except Exception as error:
            print(error)

        finally: 
            if conn is not None:
                    conn.close()             
    
    def insert_new_label(label : Labels): # Ein Label wird hinzugefügt
        describe = None
        try:
            params = config()
            with psycopg2.connect(**params) as conn:
                with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                    
                    insert_script_label = 'INSERT INTO label (description, processting_sector) VALUES (%s, %s) returning *' 
                    insert_value_label = (label.description, label.processting_sector)
                    cur.execute(insert_script_label, insert_value_label)
                    describe = cur.fetchone()
                    conn.commit()

        except Exception as error:
            print(error)

        finally: 
            if conn is not None:
                conn.close() 
        print(describe)  
   
    def delete_label(label_id : int): # Ein Label wird gelöcht
        print(label_id)
        try:
            params = config()
            with psycopg2.connect(**params) as conn:
                with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur: 
                        
                    cur.execute('DELETE  FROM  label where label_id = {0}  '.format(label_id))   #filtern
                    
        except Exception as error:
            print(error)

        finally: 
            if conn is not None:
                    conn.close()     


    def create_tickets():
        """
        Die Tabelle "tickets" wird erstellt und mit zufälligen Werten eingefühlt.
        """
        try:
            params = config()
            with psycopg2.connect(**params) as conn:
                with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:    
                    cur.execute('DROP TABLE IF EXISTS tickets CASCADE ')
                    create_script_tickets = ''' CREATE TABLE IF NOT EXISTS tickets (
                                        tickets_id          int PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
                                        level               int,
                                        creation_date       varchar(35) NOT NULL,
                                        ticket_name         varchar(40) NOT NULL,
                                        ticket_assignee     int ,
                                        CONSTRAINT FK_ticket_assignee FOREIGN KEY (ticket_assignee) REFERENCES person (person_id)
                                        )'''
                    cur.execute(create_script_tickets)
                    cur.execute('TRUNCATE TABLE tickets CASCADE')        #Werte werden gelöscht aber die Tabelle nicht
                    cur.execute('TRUNCATE TABLE tickets RESTART IDENTITY')
                    insert_script_tickets = 'INSERT INTO tickets (level, creation_date, ticket_name, ticket_assignee) VALUES ( %s, %s, %s, %s)' 
                    range_size=11
                    for i in range(1,range_size):
                        levels_tickets = ("1", "2", "3")
                        level_tickets = random.choice(levels_tickets)
                        range_size=range_size-1
                        random_num_1= random.randint(1,range_size)                    
                        creation_date = ("now", "for 4h", "for 4days","for two weeks")
                        creation_date_tickets = random.choice(creation_date)
                        ticket_names = ("Software", "repair", "transport")
                        ticket_name = random.choice(ticket_names)  
                        insert_value_tickets = ( level_tickets, creation_date_tickets, ticket_name, random_num_1)
                        cur.execute(insert_script_tickets, insert_value_tickets)
                    conn.commit()

        except Exception as error:
            print(error)

        finally: 
            if conn is not None:
                    conn.close()      
    
    def insert_new_ticket(ticket : Tickets):    # Ein Ticket wird hinzugefügt

        ticket_print = None
        try:
            params = config()
            with psycopg2.connect(**params) as conn:
                with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                    insert_script_tickets = 'INSERT INTO tickets (level, creation_date, ticket_name, ticket_assignee) VALUES ( %s, %s, %s) returning *' 
                    insert_value_tickets = (ticket.level, ticket.creation_date, ticket.ticket_name, ticket.ticket_assignee )
                    cur.execute(insert_script_tickets, insert_value_tickets)
                    ticket_print = cur.fetchone()
                    conn.commit()

        except Exception as error:
            print(error)

        finally: 
            if conn is not None:
                conn.close() 
        print(ticket_print)  

    def delete_ticket(ticket_id : int): # Ein Ticket wird gelöcht
        print(ticket_id)
        try:
            params = config()
            with psycopg2.connect(**params) as conn:
                with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur: 
                        
                    cur.execute('DELETE  FROM  tickets where tickets_id = {0}  '.format(ticket_id))   #filtern
                
        except Exception as error:
            print(error)

        finally: 
            if conn is not None:
                    conn.close()  
    
    def create_relationship_tickets_labels():
        """
        Die Tabelle "tickets" wird erstellt und mit zufälligen Werten eingefühlt.
        """
        try:
            params = config()
            with psycopg2.connect(**params) as conn:
                with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:    
                    cur.execute('DROP TABLE IF EXISTS relationship CASCADE ')
                    create_relationship_tickets_labels = ''' CREATE TABLE IF NOT EXISTS relationship (
                                        tickets_id          int,
                                        label_id            int,
                                        CONSTRAINT FK_ticket_id FOREIGN KEY (tickets_id) REFERENCES tickets (tickets_id),
                                        CONSTRAINT FK_label_id FOREIGN KEY (label_id) REFERENCES label (label_id)
                                        )'''
                    cur.execute(create_relationship_tickets_labels)
                    cur.execute('TRUNCATE TABLE relationship CASCADE')        #Werte werden gelöscht aber die Tabelle nicht
                    insert_script_relationship_tickets_labels = 'INSERT INTO relationship (tickets_id, label_id) VALUES (%s, %s)'
                    
                    cur.execute('select tickets_id from tickets')
                    list_of_tickets_id =[]
                    for record in cur.fetchall():
                        list_of_tickets_id.append(record)

                    cur.execute('select label_id from label')
                    list_of_label_id =[]
                    for record in cur.fetchall():
                        list_of_label_id.append(record)

                    for sublist in list_of_tickets_id:
                        random_num_for_choices = random.randint(0,len(list_of_label_id))
                        random_from_list = random.choices(list_of_label_id,k=random_num_for_choices)
                        for i in random_from_list:
                            insert_values_relationship_tickets_labels = (sublist[0],i[0])
                            cur.execute(insert_script_relationship_tickets_labels, insert_values_relationship_tickets_labels)
                    conn.commit()
        except Exception as error:
            print(error)

        finally: 
            if conn is not None:
                    conn.close()  

