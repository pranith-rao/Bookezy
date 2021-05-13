from flask import *
from flask.wrappers import Request
from flask_sqlalchemy import SQLAlchemy
import os,random,re
from passlib.hash import sha256_crypt
from flask_mail import Mail,Message


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(16)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///rail_db.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "bookezy13@gmail.com"
app.config['MAIL_PASSWORD'] = "pradeep13"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True


db = SQLAlchemy(app)
mail = Mail(app)

class Users(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),nullable=False,unique=True)
    email = db.Column(db.String(100),nullable=False,unique=True)
    phone = db.Column(db.String(11), nullable=False, unique=True)
    address = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255),nullable=True)



    def __repr__(self):
        return '<User %r>' % self.name

class Station(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    station_name = db.Column(db.String(100),nullable=False,unique=True)
    station_location = db.Column(db.String(100),nullable=False)
    station_pincode = db.Column(db.String(15),nullable=False)
    name = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(100), nullable=False,unique=True)
    phone = db.Column(db.String(11), nullable=False,unique=True)
    password = db.Column(db.String(255),nullable=False)

    def __repr__(self):
        return '<Station {}>' % self.name


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(100), nullable=False,unique=True)
    password = db.Column(db.String(255),nullable=False)

    def __repr__(self):
        return '<Admin %r>' % self.name

class Train(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    train_name = db.Column(db.String(100),nullable=False,unique=True)
    seats = db.Column(db.Integer,nullable=False)
    arrival_time = db.Column(db.String(30),nullable=False)
    departure_time = db.Column(db.String(30), nullable=False)
    from_location = db.Column(db.String(200),nullable=False)
    through_route = db.Column(db.String(100), nullable=False)
    to_location = db.Column(db.String(11), nullable=False)

    def __repr__(self):
        return '<Train %r>' % self.train_name



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
    if 'mainadmin' in session:
        data = Station.query.all()
        return render_template('station_list.html',data=data)
    else:
        return redirect(url_for('adminlog'))

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

@app.route("/mainadmin_log",methods=['POST'])
def mainadmin_log():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email == 'mainadmin@gmail.com' and password == '1234567890':
            session['mainadmin'] = True
            flash('Login Successfull','success')
            return redirect(url_for('admdash'))
        else:
            flash('Invalid Credentials','error')
            return redirect(url_for('adminlog'))

@app.route("/reg_station",methods=['POST'])
def reg_station():
    if request.method == 'POST':
        if 'mainadmin' in session:
            name_station = request.form['station_name']
            station_location = request.form['station_location']
            station_code = request.form['station_code']
            admin_name = request.form['admin_name']
            email = request.form['email']
            phno = request.form['phno']
            station_check = Station.query.filter_by(station_name = name_station).first()
            if not station_check:
                email_check = Station.query.filter_by(email = email).first()
                if not email_check:
                    phno_check = Station.query.filter_by(phone = phno).first()
                    if not phno_check:
                        hash_pass = sha256_crypt.hash(phno)
                        station = Station(station_name = name_station, station_location = station_location, station_pincode = station_code, name = admin_name, email = email, phone = phno, password = hash_pass)
                        db.session.add(station)
                        db.session.commit()
                        msg = Message("Registration Confirmation",sender="bookezy13@gmail.com",recipients=[email])
                        msg.body = "Your station was registered successfully"
                        mail.send(msg)
                        flash('Station registered successfully','success')
                        return redirect(url_for('admdash'))
                    else:
                        flash('Admin phone number already used','error')
                        return redirect(url_for('stationreg'))
                else:
                    flash('Admin Mail ID already used','error')
                    return redirect(url_for('stationreg'))
            else:
                flash('Station name already registered','error')
                return redirect(url_for('stationreg'))
        else:
            flash("Please login as the main admin to do so","error")
            return redirect(url_for('adminlog'))

@app.route("/logout")
def logout():
    session.clear()
    flash('Logged out successfully',"success")
    return redirect(url_for("home"))

@app.route("/log_admin",methods=['POST'])
def log_admin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        response = Station.query.filter_by(email=email).first()
        if not response:
            flash("Email ID not registered",'error')
            return redirect(url_for("stationlog"))
        else:
            checkpass = sha256_crypt.verify(password,response.password)
            if email == response.email and checkpass == True:
                session['admin'] = True
                flash('You were successfully logged in',"success")
                return redirect(url_for("stationdash"))
            else:
                flash('Invalid Credentials',"error")
                return redirect(url_for("stationlog"))

@app.route("/admin_send_otp",methods=['POST'])
def admin_send_otp():
    if request.method == 'POST':
        email = request.form['email']
        email_check = Station.query.filter_by(email=email).first()
        if email_check:
            session['station'] = True
            session['email'] = email_check.email
            otp = random.randint(000000,999999)
            session['otp'] = otp
            msg = Message('OTP for Password change',sender="bookezy13@gmail.com",recipients=[email])
            msg.body = "Dear User, your verification code is: " + str(otp)
            mail.send(msg)
            flash("OTP sent","success")
            return redirect(url_for("station_otp"))
        else:
            flash("Email ID not registered. Please contact Main Admin","error")
            return redirect(url_for('stationlog'))

@app.route('/admin_verify',methods=['POST'])
def admin_verify():
    if request.method == "POST":
        if 'station' in session:
            admin_otp = request.form['admin_otp']
            if session['otp'] == int(admin_otp):
                return redirect(url_for("station_forpass_form"))
            else:
                flash("Wrong OTP. Please try again","error")
                return redirect(url_for("station_otp"))
        else:
            flash("Session Expired","error")
            return redirect(url_for('stationlog'))

@app.route('/change_admin_pass',methods=['POST'])
def change_admin_pass():
    if request.method == "POST":
        if 'station' in session:
            pass1 = request.form['pass1']
            flag = 0
            while True:  
                if (len(pass1)<8):
                    flag = -1
                    break
                elif not re.search("[a-z]", pass1):
                    flag = -1
                    break
                elif not re.search("[A-Z]", pass1):
                    flag = -1
                    break
                elif not re.search("[0-9]", pass1):
                    flag = -1
                    break
                elif not re.search("[_@$]", pass1):
                    flag = -1
                    break
                elif re.search("\\s", pass1):
                    flag = -1
                    break
                else:
                    flag = 0
                    break
            if flag ==-1:
                flash("Not a Valid Password","error")
                return redirect(url_for("station_forpass_form"))
            pass2 = request.form['pass2']
            if pass1 == pass2:
                hash_pass = sha256_crypt.hash(pass1)
                data = Station.query.filter_by(email=session['email']).first()
                data.password = hash_pass
                db.session.commit()
                session.pop('station',None)
                session.pop('email',None)
                flash("Password changed successfully","success")
                return redirect(url_for("stationlog"))
            else:
                flash("Passwords dont match",'error')
                return redirect(url_for('station_forpass_form'))
        else:
            flash("Session Expired","error")
            return redirect(url_for('stationlog'))
            
@app.route('/change_station_pass',methods=['POST'])
def change_station_pass():
    if request.method == 'POST':
        if 'admin' in session:
            name = request.form['name']
            pass1 = request.form['pass1']
            flag = 0
            while True:  
                if (len(pass1)<8):
                    flag = -1
                    break
                elif not re.search("[a-z]", pass1):
                    flag = -1
                    break
                elif not re.search("[A-Z]", pass1):
                    flag = -1
                    break
                elif not re.search("[0-9]", pass1):
                    flag = -1
                    break
                elif not re.search("[_@$]", pass1):
                    flag = -1
                    break
                elif re.search("\\s", pass1):
                    flag = -1
                    break
                else:
                    flag = 0
                    break
            if flag ==-1:
                flash("Not a Valid Password","error")
                return redirect(url_for("changepass_station"))
            pass2 = request.form['pass2']
            if pass1 == pass2:
                name_check = Station.query.filter_by(station_name=name).first()
                if name_check:
                    hash_pass = sha256_crypt.hash(pass1)
                    name_check.password = hash_pass
                    db.session.commit()
                    flash("Password changed successfully","success")
                    return redirect(url_for("stationdash"))
                else:
                    flash("Check your station name and try again","error")
                    return redirect(url_for("changepass_station"))
            else:
                flash("Passwords dont match",'error')
                return redirect(url_for('changepass_station'))
        else:
            flash("Session Expired","error")
            return redirect(url_for('stationlog'))

if __name__ == '__main__':
    app.run(debug=True,port=9876)