import psycopg2 as ps
from random import seed
from random import randint
class Model:
    def __init__(self):
        self.con = None
        self.con = ps.connect(host="localhost", database="postgres", user="postgres", password="123")


    def get_event(self):
        cur=self.con.cursor()
        cur.execute("select * from public.\"Event\"")
        rows = cur.fetchall()
        cur.close()
        return rows
    def get_event_category(self):
        cur=self.con.cursor()
        cur.execute("select * from public.\"Event category\"")
        rows = cur.fetchall()
        cur.close()
        return rows
    def get_ticket(self):
        cur=self.con.cursor()
        cur.execute("select * from public.\"Ticket\"")
        rows = cur.fetchall()
        cur.close()
        return rows

    def delete_tk(self, table, name, value):
        if name=='id_ticket_type':
            name='id ticket type'
        if name=='id_event':
            name='id event'

        cur=self.con.cursor()
        str=f"DELETE FROM public.\"{table}\" WHERE \"{name}\"={value};"""
        print(str)
        try:
            cur.execute(str)
            self.con.commit()
            cur.close()
            return 1
        except(Exception, ps.DatabaseError, ps.ProgrammingError) as error:
            return 0

    def delete_ev(self, table, name, value):
        if name!='id_event':
            return 0
        else:
            cur=self.con.cursor()
            str=f"DELETE FROM public.\"{table}\" WHERE \"id event\"={value};"""
            str1=f"DELETE FROM public.\"Ticket\" WHERE \"id event\"={value};"""
            print(str)
            print(str1)
            try:
                cur.execute(str1)
                cur.execute(str)
                self.con.commit()
                cur.close()
                return 1
            except(Exception, ps.DatabaseError, ps.ProgrammingError) as error:
                return 0

    def check_id_evcat(self, id, name, parent):
        cur=self.con.cursor()
        str=f"select count(*) from public.\"Event category\" where \"id category\"={id};"""
        print(str)
        try:
            cur.execute(str)
            n=cur.fetchone()
            cur.close()
            return n[0]
        except(Exception, ps.DatabaseError, ps.ProgrammingError) as error:
            return -1
    def check_name_evcat(self, id, name, parent):
        cur=self.con.cursor()
        str=f"select count(*) from public.\"Event category\" where name=\'{name}\';"""
        print(str)
        try:
            cur.execute(str)
            n=cur.fetchone()
            cur.close()
            return n[0]
        except(Exception, ps.DatabaseError, ps.ProgrammingError) as error:
            return -1
    def check_parent_evcat(self, id, name, parent):
        if parent==0:
            return 0
        cur=self.con.cursor()
        str=f"select count(*) from public.\"Event category\" where \"id category\"={parent};"""
        print(str)
        try:
            cur.execute(str)
            n=cur.fetchone()
            cur.close()
            return n[0]
        except(Exception, ps.DatabaseError, ps.ProgrammingError) as error:
            return -1
    def insert_event_category(self, id, name, parent):
        cur=self.con.cursor()
        str=f"insert into public.\"Event category\" (\"id category\", name, \"parent category id\") VALUES ({id}, \'{name}\', {parent});"""
        print(str)
        try:
            cur.execute(str)
            self.con.commit()
            cur.close()
            return 1
        except(Exception, ps.DatabaseError, ps.ProgrammingError) as error:
            return 0
    def check_id_ev(self, id_ev, id_cat, performer, place, date):
        cur=self.con.cursor()
        str=f"select count(*) from public.\"Event\" where \"id event\"={id_ev};"""
        print(str)
        try:
            cur.execute(str)
            n=cur.fetchone()
            cur.close()
            return n[0]
        except(Exception, ps.DatabaseError, ps.ProgrammingError) as error:
            return -1
    def insert_event(self, id_ev, id_cat, performer, place, date):
        cur=self.con.cursor()
        str=f"insert into public.\"Event\" (\"id event\", \"id category\", performer, place, date) VALUES ({id_ev}, {id_cat}, \'{performer}\', \'{place}\', \'{date}\');"""
        print(str)
        try:
            cur.execute(str)
            self.con.commit()
            cur.close()
            return 1
        except(Exception, ps.DatabaseError, ps.ProgrammingError) as error:
            return 0
    def check_id_tk(self, id_tk, id_ev, name,price,rest):
        cur=self.con.cursor()
        str=f"select count(*) from public.\"Ticket\" where \"id ticket type\"={id_tk};"""
        print(str)
        try:
            cur.execute(str)
            n=cur.fetchone()
            cur.close()
            return n[0]
        except(Exception, ps.DatabaseError, ps.ProgrammingError) as error:
            return -1
    def insert_ticket(self, id_tk, id_ev, name,price,rest):
        cur=self.con.cursor()
        str=f"insert into public.\"Ticket\" (\"id ticket type\", \"id event\", name, price, rest) VALUES ({id_tk}, {id_ev}, \'{name}\', {price}, {rest});"""
        print(str)
        try:
            cur.execute(str)
            self.con.commit()
            cur.close()
            return 1
        except(Exception, ps.DatabaseError, ps.ProgrammingError) as error:
            return 0
    def update_event_category(self, id, name, parent):
        cur=self.con.cursor()
        str=f"Update public.\"Event category\" SET  name=\'{name}\', \"parent category id\"={parent} WHERE \"id category\"={id};"
        print(str)
        try:
            cur.execute(str)
            self.con.commit()
            cur.close()
            return 1
        except(Exception, ps.DatabaseError, ps.ProgrammingError) as error:
            return 0
    def update_event(self, id_ev, id_cat, performer, place, date):
        cur=self.con.cursor()
        str=f"Update public.\"Event\" SET  \"id category\"={id_cat}, performer=\'{performer}\', place=\'{place}\', date=\'{date}\' WHERE \"id event\"={id_ev};"
        print(str)
        try:
            cur.execute(str)
            self.con.commit()
            cur.close()
            return 1
        except(Exception, ps.DatabaseError, ps.ProgrammingError) as error:
            return 0
    def update_ticket(self, id_tk, id_ev, name,price,rest):
        cur=self.con.cursor()
        str=f"Update public.\"Ticket\" SET \"id event\"={id_ev}, name=\'{name}\', price={price}, rest={rest} WHERE \"id ticket type\"={id_tk};"
        print(str)
        try:
            cur.execute(str)
            self.con.commit()
            cur.close()
            return 1
        except(Exception, ps.DatabaseError, ps.ProgrammingError) as error:
            return 0
    def generate_ev_cat(self, n):
        i=int(n)
        while i>0:
            cur=self.con.cursor()
            cur.execute("SELECT MAX(\"id category\") from public.\"Event category\"")
            n=cur.fetchone()
            str=f"INSERT INTO public.\"Event category\" VALUES ({n[0]+1}, chr((65 + round(random() * 25)) :: int)||chr((65 + round(random() * 25)) :: int)||chr((65 + round(random() * 25)) :: int), (RANDOM()*({n[0]}-1)+1::integer));"
            cur.execute(str)
            self.con.commit()
            cur.close()
            i=i-1
        return 1
    def check_id_evcat_r(self, id, name, parent):
        cur=self.con.cursor()
        str=f"select count(*) from public.\"Event category\" where \"id category\"={id};"""
        try:
            cur.execute(str)
            n=cur.fetchone()
            cur.close()
            return n[0]
        except(Exception, ps.DatabaseError, ps.ProgrammingError) as error:
            return -1
    def generate_ev(self, n):
        i=int(n)
        j=1
        while i>0:
            cur=self.con.cursor()
            cur.execute("SELECT MAX(\"id category\") from public.\"Event category\"")
            max_cat=cur.fetchone()
            cur.execute("SELECT MAX(\"id event\") from public.\"Event\"")
            max_ev=cur.fetchone()
            seed(1)
            q=0
            id_cat=0
            while q<=0:
                id_cat=randint(j, max_cat[0])
                q=self.check_id_evcat_r(id_cat, 1, 1)
                j=j+1
            varchar='qwertyuiop'
            str=f"INSERT INTO public.\"Event\" VALUES ({max_ev[0]+1}, {id_cat}, chr((65 + round(random() * 25)) :: int)||chr((65 + round(random() * 25)) :: int)||chr((65 + round(random() * 25)) :: int), chr((65 + round(random() * 25)) :: int)||chr((65 + round(random() * 25)) :: int)||chr((65 + round(random() * 25)) :: int), timestamp \'2022-01-10 00:00:00\' + random() * (timestamp \'2023-01-20 00:00:00\' - timestamp \'2022-01-10 00:00:00\'));"
            cur.execute(str)
            self.con.commit()
            cur.close()
            i=i-1
        return 1

    def check_id_ev_r(self, id_ev):
        cur=self.con.cursor()
        str=f"select count(*) from public.\"Event\" where \"id event\"={id_ev};"""
        try:
            cur.execute(str)
            n=cur.fetchone()
            cur.close()
            return n[0]
        except(Exception, ps.DatabaseError, ps.ProgrammingError) as error:
            return -1
    def generate_tk(self, n):
        i=int(n)
        j=1
        while i>0:
            cur=self.con.cursor()
            cur.execute("SELECT MAX(\"id ticket type\") from public.\"Ticket\"")
            max_tk=cur.fetchone()
            cur.execute("SELECT MAX(\"id event\") from public.\"Event\"")
            max_ev=cur.fetchone()
            seed(1)
            q=0
            id_ev=0
            while q<=0:
                id_ev=randint(j, max_ev[0])
                q=self.check_id_ev_r(id_ev)
                j=j+1
            str=f"INSERT INTO public.\"Ticket\" VALUES ({max_tk[0]+1}, {id_ev}, chr((65 + round(random() * 25)) :: int)||chr((65 + round(random() * 25)) :: int)||chr((65 + round(random() * 25)) :: int), (RANDOM()*(1000-100)+100::integer), (RANDOM()*(500-5)+5::integer));"
            cur.execute(str)
            self.con.commit()
            cur.close()
            i=i-1
        return 1
    def search1(self,t1, a1, str1,t2, a2, max2, min2, t3,a3,str3,key):
        cur=self.con.cursor()
        str=f"select * from public.\"{t1}\" as one inner join public.\"{t3}\" as two on one.\"{key}\"=two.\"{key}\" where one.{a1} LIKE \'{str1}\' and {min2}<one.{a2} and one.{a2}<{max2} and two.{a3} LIKE \'{str3}\'"
        print(str)
        try:
            cur.execute(str)
            rows = cur.fetchall()
            cur.close()
            return rows
        except(Exception, ps.DatabaseError, ps.ProgrammingError) as error:
            return 0
    def search2(self, t1, a1, max1, min1,t2, a2, max2, min2, t3,a3,dt31,dt32,key):
        cur=self.con.cursor()
        str=f"select * from public.\"{t1}\" as one inner join public.\"{t3}\" as two on one.\"{key}\"=two.\"{key}\" where {min1}<one.{a1} and one.{a1}<{max1} and {min2}<one.{a2} and one.{a2}<{max2} and two.{a3} BETWEEN \'{dt31}\' AND \'{dt32}\'"
        print(str)
        try:
            cur.execute(str)
            rows = cur.fetchall()
            cur.close()
            return rows
        except(Exception, ps.DatabaseError, ps.ProgrammingError) as error:
            return 0
    def search3(self, t1, a1, str1,t2, a2, str2, t3,a3,max3, min3,key, key2):
        cur=self.con.cursor()
        str=f"select * from public.\"{t1}\" as one inner join public.\"{t2}\" as two on one.\"{key}\"=two.\"{key}\" inner join public.\"{t3}\" as three on two.\"{key2}\"=three.\"{key2}\" where one.{a1} LIKE \'{str1}\' and two.{a2} LIKE \'{str2}\' and {min3}<three.{a3} and three.{a3}<{max3}"
        print(str)
        try:
            cur.execute(str)
            rows = cur.fetchall()
            cur.close()
            return rows
        except(Exception, ps.DatabaseError, ps.ProgrammingError) as error:
            return 0
