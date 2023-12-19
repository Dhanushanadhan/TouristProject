

create_sequence_query = """
            CREATE SEQUENCE destination_seq
            START WITH 1000
            INCREMENT BY 1
            MAXVALUE 9999
            CYCLE
        """

create_sequence_query = """
            CREATE SEQUENCE tourist_seq
            START WITH 1000
            INCREMENT BY 1
            MAXVALUE 9999
            CYCLE
        """

create_sequence_query = """
            CREATE SEQUENCE bookings_seq
            START WITH 1000
            INCREMENT BY 1
            MAXVALUE 9999
            CYCLE
        """

insert_query_users = "INSERT INTO users (name, email, password) VALUES (:1, :2, :3)"

select_query_users = "SELECT * FROM users WHERE email = :1 AND password = :2"

select_query_admin = "SELECT * FROM admins WHERE email = :1"

insert_query_admin = "INSERT INTO admins (name, email, password) VALUES (:1, :2, :3)"


select_query_admin1 = "SELECT * FROM admins WHERE email = :1 AND password = :2"

insert_query_destinations = """ INSERT INTO Destinations (destination_id, name, description, city, country, cost_per_day)
                                VALUES (:1, :2, :3, :4, :5, :6)
                                """

insert_query_tourists = """
            INSERT INTO Tourists (tourist_id, name, email, phone_number, nationality, address)
            VALUES (:1, :2, :3, :4, :5, :6)
        """

insert_query_bookings = """
            INSERT INTO Bookings (booking_id, tourist_id, destination_id, check_in_date, check_out_date, total_cost)
            VALUES (:1, :2, :3, :4, :5, :6)
        """


select_sequence_destinatoin = "SELECT DESTINATION_SEQ.NEXTVAL FROM dual"

select_destinations  = "SELECT * FROM Destinations"


delete_destinations = "DELETE FROM Destinations WHERE destination_id = :id"

fetch_query1 = """
        SELECT SUM(total_cost) FROM Bookings
        WHERE check_in_date >= TO_DATE(:start_date, 'YYYY-MM-DD') 
        AND check_in_date <= TO_DATE(:end_date, 'YYYY-MM-DD')
        """


fetch_query2 = """
        SELECT t.name, t.email, t.phone_number, t.nationality, t.address, b.check_in_date, b.check_out_date, b.total_cost,
        d.name
        FROM Tourists t
        INNER JOIN Bookings b ON t.tourist_id = b.tourist_id
        INNER JOIN Destinations d ON d.destination_id = b.destination_id
        WHERE TRUNC(b.check_in_date) >= TO_DATE(:start_date, 'YYYY-MM-DD')
            AND TRUNC(b.check_in_date) <= TO_DATE(:end_date, 'YYYY-MM-DD')
        """

update_dest = """
        UPDATE Destinations
        SET name = :destination_name,
            description = :description,
            city = :city,
            country = :country,
            cost_per_day = :cost_per_day
        WHERE destination_id = :destination_id
        """


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


