from flask import Flask, render_template, request

import os
import sqlite3
import pandas as pd


app = Flask(__name__)


'''
DB 함수
'''
def get_db(db_name):
    return sqlite3.connect(db_name)
def sql_command(conn, command):
    try:

        conn.execute(command)
        conn.commit()
        command = command.lower()

        if "select" in command:

            command_split = command.split(" ")
            select_command = "SELECT * FROM " + command_split[command_split.index("from")+1]
            df = pd.read_sql(select_command, conn, index_col=None)
            html = df.to_html()

            conn.close()

            return html

        conn.close()

        return True



    except:

        conn.close()

    return False






@app.route("/index")
def index():
    return render_template("p2.html")

@app.route("/sql", methods=['POST'] )
def imgPreprocssing():
    if request.method == "POST":

        con= get_db(request.form.get("db_name"))
        sql= get_db(request.form.get("sql"))
        result = sql_command(con, sql)

        returnText = "비정상"

        if result == False:
            returnText = "비정상"
        elif result == True:
            returnText = "정상 작동"
        else:
            returnText = result


        return render_template('p1.html', result=returnText)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 3000))