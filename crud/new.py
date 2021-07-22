from flask import Flask,render_template,url_for,redirect,request
from flask.helpers import flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "flash message"
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='Gauranitai27#'
app.config['MYSQL_DB']='CrudApplication'

mysql=MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM students ")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', students = data )

def hello():
    return render_template("index.html")
@app.route('/insert',methods=['GET','POST'])
def insert():
    if request.method== "POST":
        flash('data inserted successfully')
        
        name=request.form['name']
        email=request.form['email']
        phone=request.form['phone']
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO students (name,email,phone) VALUES(%s,%s,%s)",(name,email,phone))
        mysql.connection.commit()
        cur.close
        return redirect(url_for('index'))
    return render_template('index.html')
@app.route('/update',methods=['GET','POST'])
def update():
    if request.method== "POST":
           
                id_data=request.form['id']
                name=request.form['name']
                email=request.form['email']
                phone=request.form['phone']
                cur=mysql.connection.cursor()
                cur.execute("UPDATE students SET name=%s,email=%s,phone=%s WHERE id = %s ",(name,email,phone,id_data))
                flash('data updated successfully')
                mysql.connection.commit()
                cur.close
                return redirect(url_for('index'))
@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM students WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('index'))                 
    
if __name__ == "__main__":
    app.run(debug=True)



