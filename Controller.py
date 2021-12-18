import Model
import View
import psycopg2 as ps

class Controller:

    def __init__(self):
        self.view = View.View()
        self.model= Model.Model()
    def print(self,name):
        if name=='Event':
            self.view.print_event(self.model.get_event())
        elif name=='Event_category':
            self.view.print_event_category(self.model.get_event_category())
        elif name=='Ticket':
            self.view.print_ticket(self.model.get_ticket())
        else:
            self.view.wrong1p()
    def delete(self, table, name, value):
        if table!='Ticket' and table!='Event' and table!='Event_category':
            self.view.wrong1p()
        elif table=='Ticket':
            if self.model.delete_tk(table, name, value)==0:
                self.view.wrongp()
            else:
                self.view.delete()
        elif table=='Event':
            if self.model.delete_ev(table, name, value)==0:
                self.view.wrongp()
            else:
                self.view.delete()
        else:
            self.view.cantdelete()
    def insert1(self,table, id, name, parent):
        a=self.model.check_id_evcat(id, name, parent)
        b=self.model.check_name_evcat(id, name, parent)
        c=self.model.check_parent_evcat(id, name, parent)
        if a==-1 or b==-1 or c==-1:
            self.view.incorrect_type()
        elif a>0 or b>0:
            self.view.cantinsert()
        elif  a==0 and b==0 and c>0:
            if self.model.insert_event_category(id, name, parent)==1:
                self.view.insert()
        else:
            self.view.cantinsert()
    def insert2(self, request2, request3, request4, request5, request6, request7):
        if request2=='Event':
            self.insert_ev(request3, request4, request5, request6, request7)
        elif request2=='Ticket':
            self.insert_tk(request3, request4, request5, request6, request7)
        else:
            self.view.wrong1p()

    def insert_ev(self, id_ev, id_cat, performer, place, date):
        c=0
        if len(date)==10:
            try:
                year=int(f'{date[0]}{date[1]}{date[2]}{date[3]}')
                month=int(f'{date[5]}{date[6]}')
                day=int(f'{date[8]}{date[9]}')
                if(date[4]=='-'and year>2020 and month<13 and month>0 and date[7]=='-' and day>0 and day <32):
                    c=1
            except:
                c=0
        if c==1:
            a=self.model.check_id_ev(id_ev, id_cat, performer, place, date)
            b=self.model.check_id_evcat(id_cat, performer, 2)
            if(a==0 and b>0):
                if self.model.insert_event(id_ev, id_cat, performer, place, date)==1:
                    self.view.insert()
                else:
                    self.view.cantinsert()
            else:
                self.view.cantinsert()
        else:
            self.view.incorrect_date()
    def insert_tk(self, id_tk, id_ev, name,price,rest):
        a=self.model.check_id_tk(id_tk, id_ev, name,price,rest)
        b=self.model.check_id_ev(id_ev, 0, 'performer', 'place', 0)
        c=0
        try:
            y=int(price)
            x=int(rest)
            c=1
        except:
            c=0
        if a==0 and b>0 and c==1:
            if self.model.insert_ticket(id_tk, id_ev, name,price,rest)==1:
                self.view.insert()
            else:
                self.view.cantinsert()
        else:
            self.view.incorrect_type_id()

    def update1(self,table, id, name, parent):
        a=self.model.check_id_evcat(id, name, parent)
        b=self.model.check_name_evcat(id, name, parent)
        c=self.model.check_parent_evcat(id, name, parent)
        if a==-1 or b==-1 or c==-1:
            self.view.incorrect_type()
        elif a==0 or b>0:
            self.view.cantupdate()
        elif  a>0 and b==0 and c>0:
            if self.model.update_event_category(id, name, parent)==1:
                self.view.update()
        else:
            self.view.cantupdate()

    def update2(self, request2, request3, request4, request5, request6, request7):
        if request2=='Event':
            self.update_ev(request3, request4, request5, request6, request7)
        elif request2=='Ticket':
            self.update_tk(request3, request4, request5, request6, request7)
        else:
            self.view.wrong1p()

    def update_ev(self, id_ev, id_cat, performer, place, date):
        c=0
        if len(date)==10:
            try:
                year=int(f'{date[0]}{date[1]}{date[2]}{date[3]}')
                month=int(f'{date[5]}{date[6]}')
                day=int(f'{date[8]}{date[9]}')
                if(date[4]=='-'and year>2020 and month<13 and month>0 and date[7]=='-' and day>0 and day <32):
                    c=1
            except:
                c=0
        if c==1:
            a=self.model.check_id_ev(id_ev, id_cat, performer, place, date)
            b=self.model.check_id_evcat(id_cat, performer, 2)
            if(a>0 and b>0):
                if self.model.update_event(id_ev, id_cat, performer, place, date)==1:
                    self.view.update()
                else:
                    self.view.cantupdate()
            else:
                self.view.cantupdate()
        else:
            self.view.incorrect_date()
    def update_tk(self, id_tk, id_ev, name,price,rest):
        a=self.model.check_id_tk(id_tk, id_ev, name,price,rest)
        b=self.model.check_id_ev(id_ev, 0, 'performer', 'place', 0)
        c=0
        try:
            y=int(price)
            x=int(rest)
            c=1
        except:
            c=0
        if a>0 and b>0 and c==1:
            if self.model.update_ticket(id_tk, id_ev, name,price,rest)==1:
                self.view.update()
            else:
                self.view.cantupdate()
        else:
            self.view.incorrect_type_id()
    def generator(self, table, n):
        if table=='Ticket':
            if self.model.generate_tk(n)==1:
                self.view.generate(n)
            else:
                self.view.cantgenerate()
        elif table=='Event':
            if self.model.generate_ev(n)==1:
                self.view.generate(n)
            else:
                self.view.cantgenerate()
        elif table=='Event_category':
            if self.model.generate_ev_cat(n)==1:
                self.view.generate(n)
            else:
                self.view.cantgenerate()
        else:
            self.view.wrong1p()
    def search2(self,t1,a1,str1,max1,min1, t2,a2,str2,max2,min2, t3,a3,str3,max3,min3,dt11,dt12,dt21,dt22,dt31,dt32):
        key=' '
        key2=' '
        if t1=='Ticket' and t2=='Ticket'and t3=='Event':
            key='id event'
        elif t1=='Event category' and t2=='Event'and t3=='Ticket':
            key='id category'
            key2='id event'
        if dt31==' ' and str3!=' ':
            res=self.model.search1(t1, a1, str1,t2, a2, max2, min2, t3,a3,str3,key)
            if res==0:
                self.view.cantsearch()
            else:
                self.view.search(res)
        elif str3==' ' and dt31==' ':
            res=self.model.search3(t1, a1, str1,t2, a2, str2, t3,a3,max3, min3,key, key2)
            if res==0:
                self.view.cantsearch()
            else:
                self.view.search(res)
        else:
            res=self.model.search2(t1, a1, max1, min1,t2, a2, max2, min2, t3,a3,dt31,dt32,key)
            if res==0:
                self.view.cantsearch()
            else:
                self.view.search(res)
