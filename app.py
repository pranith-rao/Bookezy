from flask import *
from flask.wrappers import Request
from flask_sqlalchemy import SQLAlchemy
import os,random,re
from passlib.hash import sha256_crypt
from flask_mail import Mail,Message
import random
import datetime

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
        return '<Station %r>' % self.name


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

class Seats(db.Model):
    train_id = db.Column(db.Integer,primary_key=True)
    seats_count = db.Column(db.Integer,nullable=False)

    def __repr__(self):
        return '<Seats %r>' % self.train_id

class Book(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    ticket_no = db.Column(db.String(100),nullable=False)
    name = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    seat_no = db.Column(db.String(100), nullable=False)
    train_id = db.Column(db.Integer,nullable=False)
    date = db.Column(db.String(50), nullable=False)
    child = db.Column(db.Integer, nullable=False)
    old = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Boolean,nullable=False)


    def __repr__(self):
        return '<Book %r>' % self.id

#db.create_all()
#db.drop_all()
@app.route("/admreg")
def admreg():
    return render_template('adminreg.html')

@app.route("/admdash")
def admdash():
    if 'mainadmin' in session:
        trains = Train.query.count()
        stations = Station.query.count()
        admins = Station.query.count()
        return render_template('Admin_dash.html',data=[trains,stations,admins])
    else:
        return redirect(url_for('adminlog'))

@app.route("/stationreg")
def stationreg():
    return render_template('station_reg.html')

@app.route("/stationdash")
def stationdash():
    if 'admin' in session:
        trains = Train.query.count()
        stations = Station.query.count()
        users = Users.query.count()
        return render_template('station_dash.html',data=[trains,stations,users])
    else:
        return redirect(url_for("stationlog"))

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
    if 'admin' in session:
        data = Train.query.all()
        return render_template('train_list.html',data=data)
    else:
        return redirect(url_for('stationlog'))


@app.route("/booklist")
def booklist():
    if 'admin' in session:
        reservations = Book.query.filter_by(status=0).all()
        return render_template('Booked_list.html',data=reservations)
    else:
        return redirect(url_for("stationlog"))


@app.route("/changepass_station")
def changepass_station():
    return render_template('change_pass_station.html')

@app.route("/userreg")
def userreg():
    return render_template('userreg.html')

@app.route("/userdash")
def userdash():
    if 'user' in session:
        trains = Train.query.count()
        station = Station.query.count()
        return render_template('user_dash.html',data=[trains,station])
    else:
        flash("please log in", "error")
        return redirect(url_for("userlog"))

@app.route("/available_train")
def available_train():
    if 'user' in session:
        avail = Train.query.all()
        return render_template('availtrain_list.html',data=avail)
    else:
        flash("please log in", "error")
        return redirect(url_for("userlog"))

@app.route("/Book_train")
def Book_train():
    if 'user' in session:
        station_locations = Train.query.all()
        trains_avialable = Seats.query.all()
        return render_template('Book_train.html',location=station_locations,train=trains_avialable)
    else:
        flash("please log in", "error")
        return redirect(url_for("userlog"))

@app.route("/History")
def History():
    if 'user' in session:
        history = Book.query.filter_by(email=session['user_email']).all()
        return render_template('user_history.html',data=history)
    else:
        flash("please log in", "error")
        return redirect(url_for("userlog"))

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

@app.route("/user_reserve")
def user_reserve():
    if 'user' in session:
        station_locations = Train.query.all()
        trains_avialable = Seats.query.all()
        return render_template('user_reserve.html',location=station_locations,train=trains_avialable)
    else:
        flash("please log in", "error")
        return redirect(url_for("userlog"))

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

@app.route('/train_submit',methods=['POST'])
def train_submit():
    if request.method == 'POST':
        if 'admin' in session:
            train_id = request.form['train_id']
            train_name = request.form['train_name']
            seats = request.form['seats']
            a_time = request.form['a_time']
            d_time = request.form['d_time']
            from_loc = request.form['from_loc']
            through = request.form['through']
            to_loc = request.form['to_loc']
            id_check = Train.query.filter_by(id=train_id).first()
            if not id_check:
                name_check = Train.query.filter_by(train_name=train_name).first()
                if not name_check:
                    train = Train(id=train_id,train_name=train_name,seats=seats,arrival_time=a_time,departure_time=d_time,from_location=from_loc,through_route=through,to_location=to_loc)
                    seats = Seats(train_id=train_id,seats_count=seats)
                    db.session.add(train)
                    db.session.add(seats)
                    db.session.commit()
                    flash("Train added successfully","success")
                    return redirect(url_for('stationdash'))
                else:
                    flash("Train name already used","error")
                    return redirect(url_for('trainreg'))
            else:
                flash("Train ID already used","error")
                return redirect(url_for('trainreg'))
        else:
            flash("Session Expired","error")
            return redirect(url_for('stationlog'))

@app.route("/book_ticket",methods=['POST'])
def book_ticket():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        location = request.form['location']
        tot_seats = request.form['seat']
        date = request.form['travel']
        child = request.form['child']
        senior = request.form['senior']
        train_id = request.form['train']
        if name and email:
            seats = Seats.query.filter_by(train_id=train_id).first()
            if seats.seats_count == 0:
                flash("No Seats available", "error")
                return redirect(url_for("Book_train"))
            elif int(tot_seats) > seats.seats_count:
                flash(f"Only {seats.seats_count} Seats Available","error")
                return redirect(url_for("Book_train"))
            else:
                updated_seats = seats.seats_count - int(tot_seats)
                seats.seats_count = int(updated_seats)
                db.session.commit()
                users = Book(name=name,email=email,location=location,seat_no=tot_seats,ticket_no=random.randint(999,999999),train_id=int(train_id),date=date,child=int(child),old=int(senior),status=1)
                db.session.add(users)
                db.session.commit()
                flash("Ticket Successfully Booked","success")
                return redirect(url_for("userdash"))
        else:
            flash("Name and Email Required","error")
            return redirect(url_for("Book_train"))


@app.route("/reset")
def reset():

    seats = Seats.query.all()
    return render_template("reset.html",train=seats)

@app.route("/reset_seats",methods=['POST'])
def reset_seats():
    if request.method == 'POST':
        train_id = request.form['train']
        reset = Seats.query.filter_by(train_id=train_id).first()
        reset.seats_count = 20
        db.session.commit()
        flash("Reset Successfull","success")
        return redirect(url_for("admdash"))

@app.route("/user_register",methods=["POST"])
def user_register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        password = request.form['password']
        email_check = Users.query.filter_by(email=email).first()
        if not email_check:
            phone_check = Users.query.filter_by(phone=phone).first()
            if not phone_check:
                flag = 0
                while True:  
                    if (len(password)<8):
                        flag = -1
                        break
                    elif not re.search("[a-z]", password):
                        flag = -1
                        break
                    elif not re.search("[A-Z]", password):
                        flag = -1
                        break
                    elif not re.search("[0-9]", password):
                        flag = -1
                        break
                    elif not re.search("[_@$]", password):
                        flag = -1
                        break
                    elif re.search("\\s", password):
                        flag = -1
                        break
                    else:
                        flag = 0
                        break
                if flag ==-1:
                    flash("Not a Valid Password","error")
                    return redirect(url_for("userreg"))
                hash_pass = sha256_crypt.hash(password)
                user = Users(name=name,email=email,phone=phone,address=address,password=hash_pass)
                db.session.add(user)
                db.session.commit()
                msg = Message("Registration Confirmation",sender="bookezy13@gmail.com",recipients=[email])
                msg.body = "Thank you for registering on our website.Hope you have a good experience"
                mail.send(msg)
                flash('Registeration successfully','success')
                return redirect(url_for('userlog'))
            else:
                flash("Phone Number already registered","error")
                return redirect(url_for('userreg'))
        else:
            flash("Email ID already registered","error")
            return redirect(url_for('userreg'))

@app.route("/user_login",methods=['POST'])
def user_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        response = Users.query.filter_by(email=email).first()
        if not response:
            flash("Email ID not registered",'error')
            return redirect(url_for("userlog"))
        else:
            checkpass = sha256_crypt.verify(password,response.password)
            if email == response.email and checkpass == True:
                session['user'] = True
                session['user_name'] = response.name
                session['user_email'] = response.email
                session['user_phone'] = response.phone
                flash('You were successfully logged in',"success")
                return redirect(url_for("userdash"))
            else:
                flash('Invalid Credentials',"error")
                return redirect(url_for("userlog"))

@app.route("/enquiry",methods=['POST'])
def enquiry():
    if 'user' in session:
        if request.method == 'POST':
            enquiry = request.form['enquiry']
            check_ticket_valid = Book.query.filter_by(ticket_no=enquiry).first()
            if not check_ticket_valid:
                flash("Invalid Ticket number","error")
                return redirect(url_for("userdash"))
            elif check_ticket_valid.status == 0:
                flash("Reservation is in process", "error")
                return redirect(url_for("userdash"))
            else:
                flash("Booking is Done","success")
                return redirect(url_for("userdash"))
        else:
            flash("some error occurred","error")
            return redirect(url_for("/"))

    else:
        flash("please log in","error")
        return redirect(url_for("userlog"))

@app.route("/reserve_ticket",methods=['POST'])
def reserve_ticket():
    if 'user' in session:
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            location = request.form['location']
            tot_seats = request.form['seat']
            date = request.form['travel']
            child = request.form['child']
            senior = request.form['senior']
            train_id = request.form['train']
            if name and email:
                users = Book(name=name,email=email,location=location,seat_no=tot_seats,ticket_no=random.randint(999,999999),train_id=int(train_id),date=date,child=int(child),old=int(senior),status=0)
                db.session.add(users)
                db.session.commit()
                flash("Request sent for reservation","success")
                return redirect(url_for("userdash"))
            else:
                flash("Name and Email Required","error")
                return redirect(url_for("Book_train"))
        else:
            flash("some error occurred","error")
            return redirect(url_for("/"))
    else:
        flash("please log in","error")
        return redirect(url_for("userlog"))

@app.route("/reserve_success/<int:id>")
def reserve_success(id):
    if 'admin' in session:
        update_status = Book.query.filter_by(id=id).first()
        train_id = update_status.train_id
        tot_seats = update_status.seat_no
        seats = Seats.query.filter_by(train_id=train_id).first()
        if seats.seats_count == 0:
            flash("No Seats available", "error")
            return redirect(url_for("booklist"))
        elif int(tot_seats) > seats.seats_count:
            flash(f"Only {seats.seats_count} Seats Available", "error")
            return redirect(url_for("booklist"))
        else:
            updated_seats = seats.seats_count - int(tot_seats)
            seats.seats_count = int(updated_seats)
            db.session.commit()
            update_status.status = 1
            db.session.commit()
            flash("Ticket Booked", "success")
            return redirect(url_for("booklist"))
    else:
        flash("unauthorized access","error")
        return redirect(url_for("stationlog"))

@app.route("/reserve_error/<int:id>")
def reserve_error(id):
    if 'admin' in session:
        del_ticket = Book.query.filter_by(id=id).first()
        db.session.delete(del_ticket)
        db.session.commit()
        flash("Reservation Cancelled","error")
        return redirect(url_for("booklist"))
    else:
        flash("unauthorized access", "error")
        return redirect(url_for("stationlog"))

@app.route("/cancel/<int:id>")
def cancel(id):
    check_date = Book.query.filter_by(id=id).first()
    user_date = check_date.date

    current = datetime.date.today()

    final_date = datetime_str-current
    print(final_date)



if __name__ == '__main__':
    app.run(debug=True,port=9876)