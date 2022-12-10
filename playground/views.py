#PURPOSE OF FILE: Views in django is another of way saying request -> response. It is an action you take. You can create functions that will return responses to the server.

from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector

# Connect to the database
conn = mysql.connector.connect(user='root',
                              password='Champion2118!',
                              host='localhost',
                              database='family_members')

# Create a cursor to query data.
cursor = conn.cursor()
# Execute a SQL statement
cursor.execute('SELECT * from family')
# Fetch the results
family = cursor.fetchall()

#Function that will print database family_members info.
def family_members(request):
    #print out the results.
    return HttpResponse(family)

#Function that will request a webpage.
def personal_page(request):
    #return HttpResponse("Hello World!")
    return render(request,"hello.html",{'name':'Camilooo'})


# Close the cursor and connection to the database in mysql.
cursor.close()
conn.close()