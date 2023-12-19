from flask import Flask, render_template, redirect, session, flash, request, url_for
from db import connect_to_db, create_users_table,create_admins_table, create_tourists_table ,create_destinations_table, create_bookings_table, check_table_exists
from datetime import datetime, date, timedelta

connection = connect_to_db()
cursor = connection.cursor()

app = Flask(__name__)
app.secret_key = 'Dhanush'

try:
    if not check_table_exists(cursor, "users"):
        create_users_table(cursor)
        print("Users Table is Created")
except Exception:
    print("User Table Alredy Exists")

try:
    if not check_table_exists(cursor, "admins"):
        create_admins_table(cursor)
        print("Admins  Table is Created")
except Exception:
    print("Admins Table Already Exists ")

try: 
   
    if not check_table_exists(cursor, "Tourists"):
        create_tourists_table(cursor)
        print("Tourists  Table is Created")
except Exception:
    print("Tourists Table  Already Exists ")


try:
    if not check_table_exists(cursor, "Destinations"):
        create_destinations_table(cursor)
        print("Destinatoins Table is Created")
except Exception:
    print("Destinations Table  Already Exists ")

try:
    if not check_table_exists(cursor, "Bookings"):
        create_bookings_table(cursor)
        print("Bookings Table is Created")
except Exception:
    print("Bookings Table is Already Exists")

try: 
        create_sequence_query = """
            CREATE SEQUENCE destination_seq
            START WITH 1000
            INCREMENT BY 1
            MAXVALUE 9999
            CYCLE
        """
        cursor.execute(create_sequence_query)
        connection.commit()
        print("Sequence destination_seq created.")
except Exception:
    print("Sequence destination_seq Already Exist")

try: 
        create_sequence_query = """
            CREATE SEQUENCE tourist_seq
            START WITH 1000
            INCREMENT BY 1
            MAXVALUE 9999
            CYCLE
        """
        cursor.execute(create_sequence_query)
        connection.commit()
        print("Sequence tourist_seq created.")
except Exception:
    print("Sequence tourist_seq Already Exist")

try: 
        create_sequence_query = """
            CREATE SEQUENCE bookings_seq
            START WITH 1000
            INCREMENT BY 1
            MAXVALUE 9999
            CYCLE
        """
        cursor.execute(create_sequence_query)
        connection.commit()
        print("Sequence bookings_seq created.")
except Exception:
    print("Sequence bookings_seq Already Exist")

    




@app.route('/')
def home():
    return render_template('user_index.html')



# User Authentication Functions
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        cursor.execute("SELECT * FROM users WHERE email = :1", (email,))
        existing_user = cursor.fetchone()

        if existing_user:
            flash('User already exists. Please enter different credentials.', 'error')
            return render_template('sign_up.html')

        cursor.execute("INSERT INTO users (name, email, password) VALUES (:1, :2, :3)", (name, email, password))
        connection.commit()
        
        return redirect('/login')

    return render_template('sign_up.html')

@app.route('/login', methods=['GET', 'POST'] )
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        cursor.execute("SELECT * FROM users WHERE email = :1 AND password = :2", (email, password))
        user = cursor.fetchone()

        if user:
            session['email'] = email  # Set session
            session['name'] = name
            return redirect(url_for('destinations'))
        else:
            flash("Invalid credentials. Try again.")
            return render_template('login.html')
    return render_template('login.html')

@app.route('/dashboard',methods=['GET', 'POST'])
def dashboard():
    if 'email' in session:
        return render_template('dashboard.html')
    else:
        return redirect('/login')
    
@app.route('/logout')
def logout():
    session.pop('email', None)  # Remove email from session
    return redirect('/')

@app.route('/admin_signup', methods=['GET', 'POST'])
def admin_signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        cursor.execute("SELECT * FROM admins WHERE email = :1", (email,))
        existing_user = cursor.fetchone()

        if existing_user:
            flash('User already exists. Please enter different credentials.', 'error')
            return render_template('create_admin.html')

        cursor.execute("INSERT INTO admins (name, email, password) VALUES (:1, :2, :3)", (name, email, password))
        connection.commit()
        
        return redirect('/admin_login')

    return render_template('create_admin.html')

@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login(): 
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']

        # Check if admin exists in the database
        cursor.execute("SELECT * FROM admins WHERE email = :1 AND password = :2", (email, password))
        user = cursor.fetchone()

        if user:
            session['email'] = email  # Set session
            return redirect(url_for('admin_panel', name = name, email = email))
            #return render_template('admin.html', name = name, email = email )
        else:
            flash("Invalid credentials. Try again.")
            return render_template('admin_login.html')
    return render_template('admin_login.html')

#-------------------------------------------------------
@app.route('/admin_panel', methods = ['POST', 'GET'])
def admin_panel():
    name = request.args.get('name')
    email = request.args.get('email')
    return render_template('admin.html', name = name, email = email )

def insert_destination(destination_id, name, description, city, country, cost_per_day):
    try:
        cursor.execute("""
            INSERT INTO Destinations (destination_id, name, description, city, country, cost_per_day)
            VALUES (:1, :2, :3, :4, :5, :6)
        """, (destination_id, name, description, city, country, cost_per_day))
        connection.commit()
        print("Destination inserted successfully.")
    except Exception:
        print("Error inserting destination:")

def insert_tourist(tourist_id, name, email, phone_number, nationality, address):
    try:
        cursor.execute("""
            INSERT INTO Tourists (tourist_id, name, email, phone_number, nationality, address)
            VALUES (:1, :2, :3, :4, :5, :6)
        """, (tourist_id, name, email, phone_number, nationality, address))
        connection.commit()
        print("Tourist inserted successfully.")
    except Exception as e:
        print("Error inserting tourist:", e)

def insert_booking(cursor, connection, booking_id, tourist_id, destination_id, check_in_date, check_out_date, total_cost, people, days_to_add):
    try:
        cursor.execute("""
            INSERT INTO Bookings (booking_id, tourist_id, destination_id, check_in_date, check_out_date, total_cost, number_of_people, number_of_days)
            VALUES (:1, :2, :3, :4, :5, :6, :7, :8)
        """, (booking_id, tourist_id, destination_id, check_in_date, check_out_date, total_cost, people, days_to_add))
        connection.commit()
        print("Booking inserted successfully.")
    except Exception as e:
        print("Error inserting booking:", e)

@app.route('/show_my_orders', methods=['POST', 'GET'])
def show_my_orders():
    if request.method == 'POST':
        tourist_id = request.form['TouristID']
        query = '''
        SELECT 
            b.booking_id,
            t.name,
            t.email,
            t.phone_number,
            t.nationality,
            t.address,
            d.name,
            b.check_in_date,
            b.check_out_date,
            b.total_cost,
            b.number_of_people,
            b.number_of_days
        FROM 
            Tourists t
        INNER JOIN 
            Bookings b ON t.tourist_id = b.tourist_id
        INNER JOIN 
            Destinations d ON b.destination_id = d.destination_id
        WHERE 
            b.booking_id = :tourist_id
        '''
        print(tourist_id)
        cursor.execute(query, {'tourist_id': tourist_id})
        results = cursor.fetchall()
        return render_template('order.html', results=results)
    return render_template('order.html', results=[])  # Handling GET requests




@app.route('/add_destinations', methods = ['GET', 'POST'])
def add_destinations():

    if request.method == 'POST':

      destination_name = request.form['destinationName']
      city = request.form['city']
      country = request.form['country']
      description = request.form['description']
      costPerDay = request.form['costPerDay']
      cursor.execute("SELECT DESTINATION_SEQ.NEXTVAL FROM dual")
      next_val = cursor.fetchone()[0]
      destination = (f'D{next_val}', destination_name, description, city, country, costPerDay)
      insert_destination(*destination)
      
    return render_template('add_dest.html')

@app.route('/remove_destinations')
def remove_destinations():
    cursor.execute("SELECT * FROM Destinations")
    print("Select Destinations are Selected ")
    destinations_data = cursor.fetchall()
    return render_template('remove_dest.html', destinations_data = destinations_data)

@app.route('/remove')
def remove():
    destination_id = request.args.get('id')
    sql = "DELETE FROM Destinations WHERE destination_id = :id"
    
    try:
        cursor.execute(sql, id=destination_id)
        connection.commit()
    except Exception:
        # Handle error, rollback transaction if needed
        print( f"Error occurred")
    cursor.execute("SELECT * FROM Destinations")
    print("Select Destinations are Selected ")
    destinations_data = cursor.fetchall()
    return render_template('remove_dest.html', destinations_data = destinations_data)

@app.route('/revenue', methods = ['POST', 'GET'])
def revenue():
    return render_template('revenue.html')
 
@app.route('/show_revenue_date', methods = ['POST', 'GET'])
def show_revenue_date():
    if request.method == 'POST':
        start_day = request.form['startDay']
        start_month = request.form['startMonth']
        start_year = request.form['startYear']

        end_day = request.form['endDay']
        end_month = request.form['endMonth']
        end_year = request.form['endYear']

        # Convert to string format
        start_date = f"{start_year}-{start_month}-{start_day}"
        end_date = f"{end_year}-{end_month}-{end_day}"
        print(start_date, end_date)

        # Parse the input string into a datetime object
        start_date = datetime.strptime(start_date, '%Y-%b-%d')
        end_date = datetime.strptime(end_date, '%Y-%b-%d')

        # Format the dates into 'DD-MMM-YY' format
        formatted_start_date = start_date.strftime('%d-%b-%y').upper()
        formatted_end_date = end_date.strftime('%d-%b-%y').upper()

        # SQL query to calculate total cost
        sql = """
        SELECT SUM(total_cost) FROM Bookings
        WHERE check_in_date >= TO_DATE(:start_date, 'YYYY-MM-DD') 
        AND check_in_date <= TO_DATE(:end_date, 'YYYY-MM-DD')
        """
        
        # Execute the SQL query with parameters
        cursor.execute(sql, {'start_date': start_date.strftime('%Y-%m-%d'), 'end_date': end_date.strftime('%Y-%m-%d')})

        total_cost = cursor.fetchone()[0] or 0  # Fetch the result or default to 0 if no result

        result = f'The total cost between {formatted_start_date} and {formatted_end_date} is: {total_cost}'
        print(f'The total cost between {formatted_start_date} and {formatted_end_date} is: {total_cost}')
        return render_template('revenue_show.html', result = total_cost , formatted_start_date = formatted_start_date, formatted_end_date = formatted_end_date )
        
@app.route('/tourist_data', methods = ['POST', 'GET'])
def tourist_data():
    return render_template('tourist_fetch.html')      

@app.route('/tourist_fetch', methods = ['POST', 'GET'] ) 
def tourist_fetch():
    if request.method == 'POST':
        start_day = request.form['startDay']
        start_month = request.form['startMonth']
        start_year = request.form['startYear']

        end_day = request.form['endDay']
        end_month = request.form['endMonth']
        end_year = request.form['endYear']

        # Convert to string format
        start_date = f"{start_year}-{start_month.zfill(2)}-{start_day.zfill(2)}"
        end_date = f"{end_year}-{end_month.zfill(2)}-{end_day.zfill(2)}"

        # SQL query to retrieve tourist information within the date range
        sql = """
        SELECT t.name, t.email, t.phone_number, t.nationality, t.address, b.check_in_date, b.check_out_date, b.total_cost,
        d.name
        FROM Tourists t
        INNER JOIN Bookings b ON t.tourist_id = b.tourist_id
        INNER JOIN Destinations d ON d.destination_id = b.destination_id
        WHERE TRUNC(b.check_in_date) >= TO_DATE(:start_date, 'YYYY-MM-DD')
            AND TRUNC(b.check_in_date) <= TO_DATE(:end_date, 'YYYY-MM-DD')
        """

        # Execute the SQL query with parameters
        cursor.execute(sql, {'start_date': start_date, 'end_date': end_date})
        
        # Fetch all results
        results = cursor.fetchall()

        

    return render_template('filtered_tourist.html', tourists = results)  # Assuming you have a form template
       
    
@app.route('/admin_destinations', methods = ['GET', 'POST'])
def admin_destinations():
    cursor.execute("SELECT * FROM Destinations")
    print("Select Destinations are Selected ")
    destinations_data = cursor.fetchall()
    name = session.get('name')
    return render_template('admin_dest.html', destinations=destinations_data, enumerate=enumerate)

@app.route('/update_destinations', methods = ['GET', 'POST'])   
def update_destinations():

    if request.method == 'POST':
      if request.method == 'POST':
        destination_id = request.form['destinationID']
        destination_name = request.form['destinationName']
        city = request.form['city']
        country = request.form['country']
        description = request.form['description']
        cost_per_day = request.form['costPerDay']
        
        # Assuming you have a function to execute SQL queries using a cursor
        update_destination_query = """
        UPDATE Destinations
        SET name = :destination_name,
            description = :description,
            city = :city,
            country = :country,
            cost_per_day = :cost_per_day
        WHERE destination_id = :destination_id
        """
        
        cursor.execute(update_destination_query, {
            'destination_name': destination_name,
            'description': description,
            'city': city,
            'country': country,
            'cost_per_day': cost_per_day,
            'destination_id': destination_id
        })
        
        # Commit the transaction if needed
        # conn.commit()
        
    return render_template('update_dest.html')
    



@app.route('/destinations', methods = ['GET', 'POST'])
def destinations():
    cursor.execute("SELECT * FROM Destinations")
    print("Select Destinations are Selected ")
    destinations_data = cursor.fetchall()
    name = session.get('name')
    return render_template('destination.html', destinations=destinations_data, user_name = name, enumerate=enumerate)



@app.route('/user_page', methods=['POST', 'GET'])
def user_data():
    if request.method == 'POST':
        selected_row = int(request.form['selected_row'])
        destination_name = request.form[f'destination_name_{selected_row}']
        destination_id = request.form[f'destination_id_{selected_row}']
        days = request.form[f'days_{selected_row}']
        people = request.form[f'people_{selected_row}']
        cost_per_day = request.form[f'cost_per_day_{selected_row}']

        # Process the received data here (e.g., perform calculations, save to database, etc.)

        return render_template('user.html', destination_id=destination_id, days=days, people=people, cost_per_day=cost_per_day, destination_name = destination_name)


@app.route('/bill', methods = ['POST', 'GET'])
def bill():
    if request.method == 'POST':
        dest_name = request.form['destination_name']
        cost_per_day = request.form['cost_per_day']
        people = request.form['people']
        dest_id = request.form['destination_id']
        cursor.execute("SELECT tourist_seq.NEXTVAL FROM dual")
        tourist_id = cursor.fetchone()[0]
        cursor.execute("SELECT bookings_seq.NEXTVAL FROM dual")
        bookings_id = cursor.fetchone()[0]
        total_cost = request.form['total_cost']
        current_date = date.today()
        in_date = current_date.strftime("%d-%b-%y").upper()
        days_to_add = int(request.form['days'])
        future_date = current_date + timedelta(days=days_to_add)
        out_date = future_date.strftime("%d-%b-%y").upper()
        tourist_name = request.form['name']
        tourist_email  = request.form['email']
        tourist_ph = request.form['phone']
        tourist_nationality = request.form['nationality']
        tourist_address = request.form['address']
        #booking_id, tourist_id, destination_id, check_in_date, check_out_date, total_cost
        insert_tourist(tourist_id, tourist_name, tourist_email,tourist_ph , tourist_nationality, tourist_address)
        insert_booking(cursor, connection, bookings_id, tourist_id, dest_id, in_date, out_date, total_cost, people, days_to_add)


        
    return render_template('bill.html', 
                               tourist_id = tourist_id,
                               destination_name=dest_name,
                               destination_id=dest_id,
                               cost_per_day=cost_per_day,
                               days= days_to_add,
                               people=people,
                               total_cost=total_cost,
                               name=tourist_name,
                               email=tourist_email,
                               phone=tourist_ph,
                               nationality=tourist_nationality,
                               address=tourist_address,
                               bookings_id = bookings_id)

@app.route('/my_orders', methods = ['GET', 'POST'])
def my_orders():
    return render_template('track_order.html')



if __name__ == '__main__':
    app.run(debug=True)