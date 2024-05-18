class Star_Cinema:
    Hall_list=[]

    def entry_hall(self,hall):
        self.Hall_list.append(hall)

class Hall:
    def __init__(self,rows,cols,hall_no) -> None:
        self.__seats={}
        self.__show_list=[]
        self.rows=rows
        self.cols=cols
        self.hall_no=hall_no
    
    
    def entry_show(self,show_id,movie_name,time):
        show_ditails=(show_id,movie_name,time)
        self.__show_list.append(show_ditails)
        for row in range(1,self.rows+1):
            for col in range(1,self.cols+1):
                seat=(row,col)
                self.__seats[seat]="FREE"

        
    def book_seats(self,show_id,row,col):
        show_ids=False
        for show in self.__show_list:
            if show[0] == show_id:
                show_ids = True
                break
        if not show_ids:
            print("Invalid show ID.")
            return
        
        seat=(row,col)
        if seat in self.__seats:
            if self.__seats[seat]=="FREE":
                self.__seats[seat]=show_id
                print(f"Seat{seat} Booked Successfully For Show {show_id}")
                return
            else:
                print(f"Seat{seat} is already booked")
                return
        else:
            print(f"Seat{seat} does not exit in this hall.\n Please Inter Valid Seats Number: row<={self.rows} and col<={self.cols}")
            

    def view_show_list(self):
        for show_id,move_name,time in self.__show_list:
            print(f"Show ID: {show_id}  Movie Name: {move_name}  Time: {time}")


    def view_available_seat(self,show_id):
        show_ids=False
        for show in self.__show_list:
            if show[0] == show_id:
                show_ids = True
                break

        if not show_ids:
              print("Invalid show ID.")
              return
        
        print(f"\nAvailable Seats For Show {show_id}:")
        for row in range(1,self.rows+1):
            for col in range(1,self.cols+1):
                seat=(row,col)
                if self.__seats[seat]=="FREE":
                    print("0",end=" ")
                else:
                    print("1",end=" ")
            print()
                
        

    
    
cinema=Star_Cinema()
hall=Hall(8,11,50)
hall.entry_show('1','Danki',"16/5/2024  4:00 PM")
hall.entry_show("2","RRR","16/05/2024   7:00 PM")
hall.entry_show('3',"Pather Panchali","16/05/2024  9:00 PM")
# hall.view_show_list()
# hall.book_seats(1,2,5)


run=True

while True:
    print("\n Options:")
    print("1. VIEW ALL SHOW TODAY ")
    print("2. VIEW AVAILABLE SEATS ")
    print("3. BOOK TICKECT ")
    print("4. Exit ")

    op=int(input("Enter Option: "))

    if op==1:
         print("-----------")
         hall.view_show_list()
         print("-----------")
    
    elif op==2:
        show_id=input("ENTER SHOW ID: ")
        print("---------")
        hall.view_available_seat(show_id)
        print("---------")

    elif op==3:
        show_id=input("Enter Show ID: ")
        row=int(input("Enter Row Number:"))
        col=int(input("Enter Col Number: "))
        print("--------")
        hall.book_seats(show_id,row,col)
        print("-------")
    
    elif op==4:
        print("Exiting program.")
        break
         
        
    
        


