
#Dwayne Winn Class Project week 9

def main():
    c_user() #I moved this to admin only access used here to create first admin accont 
    e_detail = []
    emp_name = ""
    emp_list = []
    e_totals = {}
    t_tax = 0
    t_emp = 0
    #_____________________________________________________________
    u_role = login()
    if u_role == "none":
       print("Invalid login")
    elif u_role  == "user":
       s_date = start_date()
       emp_details = read_emp_details(s_date)
    elif u_role == "admin": 
      #add menu for options - users or data entery
      #moved this here becaue for security reasons
      # c_user()
 #_______________________________________________________________     
       while emp_name != 'end':
          print("))))))))))))))))Employee Data Entry(((((((((((((((")
          print()
          emp_name = empName()
          if (emp_name.lower() == "end"):
             break 
          else:
             s_date,e_date = d_worked()
             if (len(s_date.split('/'))) != 3 or (len(e_date.split('/'))) != 3:
                print("invalid date try again")
                s_date,e_date = d_worked()  
             hours = h_worked()
             p_rate = pay_rate()
             t_rate = tax_rate()
       
             #add to employee to list
             e_detail.insert(0, s_date)
             e_detail.insert(1, e_date)
             e_detail.insert(2, emp_name)
             e_detail.insert(3, hours)
             e_detail.insert(4, float(p_rate)
             e_detail.insert(5, t_rate)
   
            #write file
            write_emp_list(e_detail)
       print()
       #function to get date or all
       s_date = start_date
       emp_details = read_emp_details(s_date)
  

#_______________________________________________________________#
def user_id():
    u_id = input("Enter user id or end to quit: ")
    return u_id
#----------------------------------------------------------------#
def user_pwd():
   u_pwd = input("Enter password: ")
   return u_pwd
#_____________________________________________________________
def user_role():
    u_role = input("Enter role |admin|user|: ")
    while True:
        if u_role == "admin" or u_role == "user":
           return u_role
        else:
           user_role()
#___________________________________________________________________
def c_user():
    
    print("Create New User/role")
    print()
    
    u_file = open("users.txt", "a+")
    while True:
        u_id = user_id()                
        if u_id.lower() == "end":
           break
        u_pwd = user_pwd()
        u_role = user_role()
        u_file.write('{}|{}|{}\n'.format(u_id,u_pwd,u_role))
     
    u_file.close
    s_users()
    return 
#__________________________________________________________________________           
def s_users():
    
    u_file = open("users.txt", "r")
    while True:
        u_info = u_file.readline()
        if not u_info:
            break
        u_info =  u_info.replace("\n", "")
        u_list = u_info.split("|")
        
        u_id = u_list[0]
        u_pwd = u_list[1]
        u_role = u_list[2]
        print()
        print("User ID ",u_id," Password:",u_pwd,"User role:",u_role)
    return  

def login():
    print()
    print(")))))))))))))))LOGIN(((((((((((((((((((((((((((((")
    u_file = open("Users.txt", "r")
    u_list = []
    u_id = input("Enter user ID: ")
    u_pwd = input("Enter Password: ")
    u_role = "none"
    while True:
        u_info = u_file.readline()
        if not u_info:
           return u_role
        u_info = u_info.replace("\n", "")
        u_list = u_info.split("|")
        if u_id == u_list[0] and u_pwd == u_list[1]:
            u_role = u_list[2]  
            return u_role
    return u_role

#________________________________________________________________________

                 
def d_worked():     
     s_date = input("Please enter start date in the following formatMM/DD/YYYY: ")
    
     e_date = input("Please enter end date in the following format MM/DD/YYYY: ")
     return s_date, e_date

def empName():
    emp_name =input("Enter employee name or (end): ")
    return emp_name

def h_worked():
    hours = float(input("Enter hours worked: "))
    return hours

def pay_rate():
    p_rate = float(input("Enter hourly rate: "))
    return p_rate

def tax_rate():
    t_rate = float(input("Enter tax rate: "))
    t_rate = t_rate / 100 
    return t_rate

#write file
def write_emp_list(e_detail):
    file = open('emp_list.txt', 'a')
    file.write('{}|{}|{}|{}|{}|{}\n'.format(e_detail[0],e_detail[1],e_detail[2],e_detail[3],e_detail[4],e_detail[5]))

#caculate employee totals
def c_pay(hours,p_rate,t_rate):
    g_pay = hours * p_rate
    i_tax = float(g_pay) * float(t_rate)
    n_pay = g_pay - i_tax
    return g_pay,i_tax,n_pay

#get user input
def start_date():
    valid = False
    s_date = ""
    while not valid:
          print()   
          print(")))))))))))))))))))))))))))Display employee Information(((((((((((((((((((((((((((((((((((((((((") 
          print("Enter start date (mm/dd/yyyy)")
          s_date = input("or (ALL) for all files :")
          if (len(s_date.split('/'))) != 3 and s_date.upper() != 'ALL':
              print("Date Not Valid")
              print()
          else:
              valid = True
    return s_date

#read file create list
def read_emp_details(s_date):
    emplist = []

    etotals = {}
    emp_list = []
    file = open("emp_list.txt", "r")
    data = file.readlines()
    
    #create the list
   
    if s_date.upper() == 'ALL':
       for emp_list in data:
           emp_list = [x.strip() for x in emp_list.strip().split("|")]
           emplist.append([emp_list[0], emp_list[1], emp_list[2],float(emp_list[3]), float(emp_list[4]), float(emp_list[5])])
       d_info(emplist)
       print("End of record")    
    else:
       for emp_list in data:
           emp_list = [x.strip() for x in emp_list.strip().split("|")]
           if s_date == emp_list[0]:
              emplist.append([emp_list[0],emp_list[1], emp_list[2],float(emp_list[3]), float(emp_list[4]), float(emp_list[5])])
       
       print()
       print("End of record:")
    d_info(emplist)               
  #display employee info snd running total
def d_info(emplist):  
    emp_list = []
    t_emp = 0
    t_hours = 0
    t_gpay = 0
    t_tax = 0
    t_npay  = 0
    etotals = {}
    #set varibles for caculation
    for emp_list in emplist:
        hours = float(emp_list[3])
        p_rate = emp_list[4]
        t_rate = emp_list[5]
        g_pay, i_tax, n_pay = c_pay(hours,p_rate,t_rate)
        t_emp += 1
        t_hours += hours
        t_gpay += g_pay
        t_tax += i_tax
        t_npay += n_pay
    
        print()
        #print data requsted
        print(emp_list[0],"|", emp_list[1],"|", emp_list[2],"|",f"{emp_list[3]:,.2f}","| $",f"{emp_list[4]:,.2f}","|",emp_list[5],"|$",f"{g_pay:,.2f}","|$",f"{i_tax:,.2f},","|$",f"{n_pay:,.2f}")
   
    #running totals
    etotals["TEmp"] = t_emp
    etotals["TGross"] = t_gpay
    etotals["THrs"] = t_hours
    etotals["TTax"] = t_tax
    etotals["TNet"] = t_npay
    #print totals
    print()
    print(f"Total Number of Employees: {etotals['TEmp']}")
    print(f"Total Hours Worked: {etotals['THrs']}")
    print(f"Total Gross Pay: {etotals['TGross']:,.2f}")
    print(f"Total Income Tax: {etotals['TTax']:,.2f}")
    print(f"Total Net Pay: {etotals['TNet']:,.2f}")

    

if __name__ == "__main__":
    main()
