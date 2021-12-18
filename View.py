
class View:
    def __init__(self):
        self.a=None

    def blank(self):
        print("No commands")
    def blank2(self):
        print("This function needs parametr")
    def blank3(self):
        print("This function needs second parametr")
    def blank4(self):
        print("This function needs third parametr")
    def blank5(self):
        print("This function needs fourth parametr")
    def blank6(self):
        print("This function needs fifth parametr")
    def blank7(self):
        print("This function needs sixth parametr")

    def print_event(self,rows):
        for r in rows:
            print(f"id event {r[0]} -- id category {r[1]} -- performer {r[2]} -- place {r[3]} -- date {r[4]}")
    def print_event_category(self,rows):
        for r in rows:
            print(f"id category {r[0]} -- name {r[1]} -- parent category {r[2]}")
    def print_ticket(self,rows):
        for r in rows:
            print(f"id ticket type {r[0]} -- id event {r[1]} -- name {r[2]} -- price {r[3]} -- rest {r[4]}")
    def wrong1p(self):
        print("First parametr is incorrect")
    def wrongp(self):
        print("Parametrs are incorrect")
    def delete(self):
        print("Deleting complete!")
    def cantdelete(self):
        print("This line cannot be deleted because deleting it will cause the database to crash")
    def insert(self):
        print("Inserting complete!")
    def cantinsert(self):
        print("Unable to insert this data into the table")
    def incorrect_type(self):
        print("Incorrect data type")
    def incorrect_date(self):
        print("Incorrect date Correct: [year]-[month]-[day]")
    def incorrect_type_id(self):
        print("Incorrect data type or id")
    def update(self):
        print("Updating complete!")
    def cantupdate(self):
        print("Unable to update this data")
    def generate(self,n):
        print(f"Generated {n} lines!")
    def cantgenerate(self):
        print("Unable to generate")
    def wronginput(self):
        print("Wrong input")
    def search(self, res):
        print('search result:')
        for r in res:
            print(r)
    def cantsearch(self):
        print('Problem in searching')
