import psycopg2

# declare the connection string specifying
# the host name database name use name 
# and password
#conn_string = "host='localhost' dbname='postgres' user='postgres' password='myPassword'"




class Db:

    # Constructor
    def __init__(self, conn_string):
        self.conn_string = conn_string

    def connect(self):
        self.conn = psycopg2.connect(self.conn_string)
        return
    
    def disconnect(self):
        if self.conn != None:
            self.conn.close()
        return
    
    def execute(self, query):
        if self.conn is None:
            raise Exception("connect first")


        self.conn.autocommit = True

        cursor = self.conn.cursor() 
        cursor.execute(query)
        self.conn.commit() 

        return

    def query(self, query):
        if self.conn is None:
            raise Exception("connect first")


        self.conn.autocommit = True
        cursor = self.conn.cursor() 

        cursor.execute(query) 
        results = cursor.fetchall() 
        

        self.conn.commit() 

        return results
      
