from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

cnx = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Arturs12",
    database="mydb"
)

cursor = cnx.cursor()

@app.route('/')
def sakums():
    return render_template("sakums.html")

@app.route('/jauns_lietotajs')
def jauns_lietotajs():
    return render_template("jauns_lietotajs.html")

@app.route('/jauns_sporta_veids')
def jauns_sporta_veids():
    return render_template("jauns_sporta_veids.html")

@app.route('/jauns_trenins')
def jauns_trenins():
    return render_template("jauns_trenins.html")

@app.route('/lietotaja_apstrade', methods=["GET", "POST"])
def lietotaja_apstrade():
    if request.method == "POST":
        vards = request.form["vards"]
        uzvards = request.form["uzvards"]

        cnx = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Arturs12",
            database="mydb"
        )
        cursor = cnx.cursor()


        query = "INSERT INTO lietotaju (vards, uzvards, sporta_veidi_id, trenins_id) VALUES (%s, %s, 1, 1)"
        cursor.execute(query, (vards, uzvards))
        cnx.commit()
        cursor.close()
        cnx.close()

        return redirect("/")

@app.route('/veida_apstrade', methods=["GET", "POST"])
def veida_apstrade():
    if request.method == "POST":
        nosaukums = request.form["nosaukums"]

        cnx = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Arturs12",
            database="mydb"
        )
        cursor = cnx.cursor()

        query = "INSERT INTO sporta_veidi (veids) VALUES (%s)"
        cursor.execute(query, (nosaukums,))
        cnx.commit()

        cursor.close()
        cnx.close()

        return redirect("/")

@app.route('/trenina_apstrade', methods=["GET", "POST"])
def trenina_apstrade():
    if request.method == "POST":
        intensitate = request.form["intensitate"]
        laiks = request.form["laiks"]
        cnx = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Arturs12",
            database="mydb"
        )
        cursor = cnx.cursor()

        query = "INSERT INTO trenins (intensitate, laiks) VALUES (%s, %s)"
        cursor.execute(query, (intensitate, laiks))
        cnx.commit()
        cursor.close()
        cnx.close()

        return redirect("/")

if __name__ == "__main__":
  app.run(host = '0.0.0.0',port = 8080)

cursor.close()
cnx.close()