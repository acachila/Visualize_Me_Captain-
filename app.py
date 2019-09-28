from flask import Flask, jsonify, render_template
import psycopg2
import psycopg2.extras

# Flask Setup
app = Flask(__name__)
name = 'postgres' #default username, use yours if different
password = 'Bootcamp!1' #insert yours
db = 'project' #insert database name you used

connection =  psycopg2.connect(user = name,
                 password = password, 
                 host = '127.0.0.1',
                port = '5432',
                database = db)
                               
cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

@app.route("/")

def index():
    
    return render_template("index.html")
    

@app.route("/<country>")

def country(country):
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute(f'Select * from merged where country = \'{country}\';')

    country_dat = cursor.fetchall()
    cursor.close()
    country = dict(country_dat[0])
    return jsonify(country)
                            
@app.route("/topco2")
def topco2():
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute('Select country, total_c02 from merged;')

    co2 = cursor.fetchall()

    cursor.close()
    top_co2 = dict(co2)
    return jsonify(top_co2)

@app.route("/topgdp")
def topgdp():
    cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute('Select country, total_gdp from merged;')

    gdp = cursor.fetchall()

    cursor.close()
    top_gdp = dict(gdp)
    return jsonify(top_gdp)


if __name__ == '__main__':
    app.run(debug=True)