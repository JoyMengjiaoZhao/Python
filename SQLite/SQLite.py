import sqlite3
from employee import Employee

conn=sqlite3.connect(':memory:') #start fresh eveytime u run
#conn=sqlite3.connect('employee.db')

c=conn.cursor()

c.execute("""CREATE TABLE employee(
          first text,
          last text,
          pay integer
  )""")
def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employee VALUES(:first, :last, :pay)",{'first':emp.first,'last':emp.last,'pay':emp.pay})

def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employee WHERE last=:last",{'last':lastname})
    return c.fetchall()

def update_pay(emp,pay):
    with conn:
        c.execute("""UPDATE employee SET pay=:pay
        where first=:first and last=:last""",{'first':emp.first,'last':emp.last,'pay':pay})

def remove_emp(emp):
    with conn:
        c.execute("DELETE FROM employee WHERE first=:first and last=:last",{'first':emp.first,'last':emp.last})

#c.execute("INSERT INTO employees VALUES ('Joy','Zhao',50000)")
#conn.commit()
emp_1=Employee('Chen','Mu',60000)
emp_2=Employee('Hong','Xiao',70000)

insert_emp(emp_1)
insert_emp(emp_2)
emps=get_emps_by_name('Xiao')
print(emps)
update_pay(emp_1,90000)
#remove_emp(emp_2)
emps=get_emps_by_name('Mu')
print(emps)

#c.execute("INSERT INTO employees VALUES (?,?,?)",(emp_1.first,emp_1.last,emp_1.pay))
#conn.commit()
#c.execute("INSERT INTO employees VALUES(:first, :last, :pay)",{'first':emp_2.first,'last':emp_2.last,'pay':emp_2.pay})
#conn.commit()
#c.execute("SELECT * FROM employees WHERE last=?",('Mu',))
#print(c.fetchall())
#c.execute("SELECT * FROM employees WHERE last=:last",{'last':'Mu'})
#print(c.fetchone())
#c.fetchmany(5) #5 rows
#print(c.fetchall())
#conn.commit()
conn.close()
