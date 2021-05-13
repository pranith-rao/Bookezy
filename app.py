from flask import Flask,redirect,render_template,url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///rail_db.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class users(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),nullable=False,unique=True)
    email = db.Column(db.String(100),nullable=False,unique=True)
    phone = db.Column(db.String(11), nullable=False, unique=True)
    address = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255),nullable=True)



    def __repr__(self):
        return '<User %r>' % self.name

class station(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    station_name = db.Column(db.String(100),nullable=False,unique=True)
    station_location = db.Column(db.String(100),nullable=False)
    station_pincode = db.Column(db.String(15),nullable=False)
    name = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(100), nullable=False,unique=True)
    phone = db.Column(db.String(11), nullable=False,unique=True)
    password = db.Column(db.String(255),nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name


class admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(100), nullable=False,unique=True)
    password = db.Column(db.String(255),nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name

class train(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    train_name = db.Column(db.String(100),nullable=False,unique=True)
    seats = db.Column(db.Integer,nullable=False)
    arrival_time = db.Column(db.String(30),nullable=False)
    departure_time = db.Column(db.String(30), nullable=False)
    from_location = db.Column(db.String(200),nullable=False)
    through_route = db.Column(db.String(100), nullable=False)
    to_location = db.Column(db.String(11), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.train_name



#db.create_all()
@app.route("/admreg")
def admreg():
    return render_template('adminreg.html')

@app.route("/admdash")
def admdash():
    return render_template('Admin_dash.html')

@app.route("/stationreg")
def stationreg():
    return render_template('station_reg.html')

@app.route("/stationdash")
def stationdash():
    return render_template('station_dash.html')

@app.route("/stationlist")
def stationlist():
    return render_template('station_list.html')

@app.route("/trainreg")
def trainreg():
    return render_template('Train_reg.html')


@app.route("/trainlist")
def trainlist():
    return render_template('train_list.html')

@app.route("/booklist")
def booklist():
    return render_template('Booked_list.html')


@app.route("/changepass_station")
def changepass_station():
    return render_template('change_pass_station.html')

@app.route("/userreg")
def userreg():
    return render_template('userreg.html')

@app.route("/userdash")
def userdash():
    return render_template('user_dash.html')

@app.route("/available_train")
def available_train():
    return render_template('availtrain_list.html')

@app.route("/Book_train")
def Book_train():
    return render_template('Book_train.html')

@app.route("/History")
def History():
    return render_template('user_history.html')

@app.route("/")
def home():
    return render_template('Home.html')

@app.route("/adminlog")
def adminlog():
    return render_template('adminlog.html')

@app.route("/userlog")
def userlog():
    return render_template('user_log.html')

@app.route("/stationlog")
def stationlog():
    return render_template('Station_log.html')

@app.route("/admin_forpass")
def admin_forpass():
    return render_template('Admin_forpass.html')

@app.route("/station_forpass")
def station_forpass():
    return render_template('station_forpass.html')

@app.route("/user_forpass")
def user_forpass():
    return render_template('user_forpass.html')

@app.route("/admin_otp")
def admin_otp():
    return render_template('admin_otp.html')

@app.route("/station_otp")
def station_otp():
    return render_template('station_otp.html')

@app.route("/user_otp")
def user_otp():
    return render_template('user_otp.html')

@app.route("/admin_forpass_form")
def admin_forpass_form():
    return render_template('Admin_forpass_form.html')

@app.route("/station_forpass_form")
def station_forpass_form():
    return render_template('station_forpass_form.html')

@app.route("/user_forpass_form")
def user_forpass_form():
    return render_template('user_forpass_form.html')




if __name__ == '__main__':
    app.run(debug=True,port=9876)