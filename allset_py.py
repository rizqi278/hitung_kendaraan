import cv2
import numpy as np
import Vehicle
import time
import re
import mysql.connector

from flask import Flask, render_template, request, redirect, url_for, session, Response


app = Flask(__name__)
app.secret_key = "super secret key"

# Enter your database connection details below

# http://localhost:5000/pythonlogin/ - this will be the login page, we need to use both GET and POST requests
@app.route('/login', methods=['GET', 'POST'])
def login():
    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="log"
        )
    mycursor = mydb.cursor()
# Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        mycursor.execute('SELECT * FROM akun WHERE username = %s AND password = %s', (username, password))
        # Fetch one record and return result
        akun = mycursor.fetchone()
                # If account exists in accounts table in out database
        if akun:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = akun[0]
            session['username'] = akun[1]
            # Redirect to home page
            return redirect(url_for('home'))
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    return render_template('index.html', msg=msg)
@app.route('/register', methods=['GET', 'POST'])
def register():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="log"
    )
    mycursor = mydb.cursor()
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
                # Check if account exists using MySQL
        mycursor.execute('SELECT * FROM akun WHERE username = %s',(username,))
        akun = mycursor.fetchone()
        # If account exists show error and validation checks
        if akun:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            mycursor.execute('INSERT INTO akun VALUES (NULL, %s, %s, %s)', (username, password, email))
            mydb.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)

# http://localhost:5000/pythinlogin/home - this will be the home page, only accessible for loggedin users
@app.route('/home')
def home():
    # Check if user is loggedin
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('index1.html', username=session['username'])
# User is not loggedin redirect to login page
    return redirect('/login')
@app.route('/logout')
def logout():
	session.pop('username', None)
	return redirect('/login')


@app.route('/laporan')
def index2():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="log"
    )
    #setting chart
    mycursor1 = mydb.cursor() #SUM(JML) AS total
    sql1 = "SELECT SUM(JML) AS total FROM data_kend WHERE BLN=01"
    mycursor1.execute(sql1)
    myresult1 = mycursor1.fetchall()

    mycursor2 = mydb.cursor()
    sql2 = "SELECT SUM(JML) AS total FROM data_kend WHERE BLN=02"
    mycursor2.execute(sql2)
    myresult2 = mycursor2.fetchall()

    mycursor3 = mydb.cursor()
    sql3 = "SELECT SUM(JML) AS total FROM data_kend WHERE BLN=03"
    mycursor3.execute(sql3)
    myresult3 = mycursor3.fetchall()

    mycursor4 = mydb.cursor()
    sql4 = "SELECT SUM(JML) AS total FROM data_kend WHERE BLN=04"
    mycursor4.execute(sql4)
    myresult4 = mycursor4.fetchall()

    mycursor5 = mydb.cursor()
    sql5 = "SELECT SUM(JML) AS total FROM data_kend WHERE BLN=05"
    mycursor5.execute(sql5)
    myresult5 = mycursor5.fetchall()

    mycursor6 = mydb.cursor()
    sql6 = "SELECT SUM(JML) AS total FROM data_kend WHERE BLN=06"
    mycursor6.execute(sql6)
    myresult6 = mycursor6.fetchall()

    mycursor7 = mydb.cursor()
    sql7 = "SELECT SUM(JML) AS total FROM data_kend WHERE BLN=07"
    mycursor7.execute(sql7)
    myresult7 = mycursor7.fetchall()

    mycursor8 = mydb.cursor()
    sql8 = "SELECT SUM(JML) AS total FROM data_kend WHERE BLN=08"
    mycursor8.execute(sql8)
    myresult8 = mycursor8.fetchall()

    mycursor9 = mydb.cursor()
    sql9 = "SELECT SUM(JML) AS total FROM data_kend WHERE BLN=09"
    mycursor9.execute(sql9)
    myresult9 = mycursor9.fetchall()

    mycursor10 = mydb.cursor()
    sql10 = "SELECT SUM(JML) AS total FROM data_kend WHERE BLN=10"
    mycursor10.execute(sql10)
    myresult10 = mycursor10.fetchall()

    mycursor11 = mydb.cursor()
    sql11 = "SELECT SUM(JML) AS total FROM data_kend WHERE BLN=11"
    mycursor11.execute(sql11)
    myresult11 = mycursor11.fetchall()

    mycursor12 = mydb.cursor()
    sql12 = "SELECT SUM(JML) AS total FROM data_kend WHERE BLN=12"
    mycursor12.execute(sql12)
    myresult12 = mycursor12.fetchall()
    if 'loggedin' in session:
        return render_template("laporan.html", username=session['username'], myresult1=myresult1, myresult2=myresult2, myresult3=myresult3, myresult4=myresult4, myresult5=myresult5, myresult6=myresult6, myresult7=myresult7, myresult8=myresult8, myresult9=myresult9, myresult10=myresult10, myresult11=myresult11, myresult12=myresult12 )
    return redirect('/login')

def gen():
    # konektor database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="log"
    )
    mycursor = mydb.cursor()

    # cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    # cv2.resizeWindow('image', 64,64)
    cnt_up = 0
    cnt_down = 0
    UpMTR = 0
    UpLV = 0
    UpHV = 0
    DownLV = 0
    DownHV = 0
    cnt_upid = 0
    countnoumber = 0
    idl = 0
    id = 0
    # rtsp://www.lalinsemarang.info:1935/live/kaligarang.stream
    # set input video
    cap = cv2.VideoCapture("rtsp://www.lalinsemarang.info:1935/live/kaligarang.stream")

    # Capture the properties of VideoCapture to console (mengambil properties video eg. width, height dll)
    for i in range(10):
        # print properties video
        print(i, cap.get(i))

    # mengambil width dan heigth video dari properties (value w posisi ke 3, h posisi ke 4)
    w = cap.get(3)
    print('Width', w)
    h = cap.get(4)
    print('Height', h)
    # luas frame area h*w
    frameArea = 500 * 900
    areaTH = frameArea / 1000
    print('Area Threshold', areaTH)

    # Input/Output Lines
    # yang itung kendaraan turun (biru)
    line_up = 180
    up_limit = 100
    # yang itung kendaraan naik (merah), untuk setting garis
    line_down = 500
    down_limit = int(3 * (h / 5))

    print("Red line y:", str(line_down))
    print("Blue line y:", str(line_up))
    line_down_color = (255, 0, 0)
    line_up_color = (0, 0, 255)
    # set height garis
    pt1 = [0, line_down]
    pt3 = [0, line_up]
    pt5 = [0, up_limit]
    pt7 = [0, down_limit]
    # set lebar garis sesuai width video
    pt2 = [w, line_down]
    pt4 = [w, line_up]
    pt6 = [w, up_limit]
    pt8 = [w, down_limit]
    pts_L1 = np.array([pt1, pt2], np.int32)
    pts_L1 = pts_L1.reshape((-1, 1, 2))
    pts_L2 = np.array([pt3, pt4], np.int32)
    pts_L2 = pts_L2.reshape((-1, 1, 2))
    pts_L3 = np.array([pt5, pt6], np.int32)
    pts_L3 = pts_L3.reshape((-1, 1, 2))
    pts_L4 = np.array([pt7, pt8], np.int32)
    pts_L4 = pts_L4.reshape((-1, 1, 2))

    # Create the background subtractor
    fgbg = cv2.createBackgroundSubtractorMOG2()

    kernelOp = np.ones((3, 3), np.uint8)
    kernelOp2 = np.ones((5, 5), np.uint8)
    kernelCl = np.ones((11, 11), np.uint8)

    # Variables
    font = cv2.FONT_HERSHEY_SIMPLEX
    vehicles = []
    max_p_age = 5
    pid = 1

    while (cap.isOpened()):
        # read a frame
        ret, frame = cap.read()

        for i in vehicles:
            i.age_one()  # age every person on frame

        #################
        # PREPROCESSING #
        #################
        fgmask = fgbg.apply(frame)
        fgmask2 = fgbg.apply(frame)

        # Binary to remove shadow
        try:
            # cv2.imshow('Frame', frame)
            # cv2.imshow('Backgroud Subtraction', fgmask)
            ret, imBin = cv2.threshold(fgmask, 200, 255, cv2.THRESH_BINARY)
            ret2, imBin2 = cv2.threshold(fgmask2, 200, 255, cv2.THRESH_BINARY)
            # Closing (dilate->erode) to join white region
            mask = cv2.morphologyEx(imBin, cv2.MORPH_CLOSE, kernelOp2)
            mask2 = cv2.morphologyEx(imBin2, cv2.MORPH_CLOSE, kernelOp2)
            # Opening (erode->dilate) to remove noise
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernelOp2)
            mask2 = cv2.morphologyEx(mask2, cv2.MORPH_OPEN, kernelOp2)
            cv2.imshow('Image Threshold', cv2.resize(fgmask, (400, 300)))
            cv2.imshow('Image Threshold2', cv2.resize(fgmask2, (400, 300)))
            cv2.imshow('Masked Image', cv2.resize(mask, (400, 300)))
            cv2.imshow('Masked Image2', cv2.resize(mask2, (400, 300)))
        except:
            # If there is no more frames to show...
            print('EOF')
            print('UP:', cnt_up)
            print('DOWN:', cnt_down)
            break

        ##################
        ## FIND CONTOUR ##
        ##################
        contours0, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        for cnt in contours0:
            # membuat kontur/garis mengikuti objek bergerak
            # cv2.drawContours(frame, cnt, -1, (0,255,0), 3, 8)
            area = cv2.contourArea(cnt)
            # print area," ",areaTH
            if area > areaTH and area < 50000:
                # mengatur ukuran kendaraan yang dideteksi
                # if area > areaTH:
                # print 'Area:::', area
                ################
                #   TRACKING   #
                ################
                M = cv2.moments(cnt)
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])
                x, y, w, h = cv2.boundingRect(cnt)

                # the object is near the one which already detect before
                new = True
                for i in vehicles:
                    if abs(x - i.getX()) <= w and abs(y - i.getY()) <= h:
                        new = False
                        i.updateCoords(cx, cy)  # Update the coordinates in the object and reset age
                        # jika objek melewati garis biru duluan berarti going up, dicek di Vehicle.py
                        if i.going_UP(line_down, line_up) == True:
                            roi = frame[y:y + h, x:x + w]
                            rectangle = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                            height = h
                            width = w
                            luas = height * width
                            # atur parameter luas rectangle berdasarkan video
                            if luas > 40000:
                                UpLV += 1
                            elif luas > 60000:
                                UpHV += 1

                            cv2.imshow('Region of Interest', roi)
                            # cv2.imshow('Rectangle', rectangle)
                            # print "Area equal to ::::", area
                            cnt_up += 1
                            idk = int(time.strftime("%y%m%d%H%M%S")) * 100
                            if idk == idl:
                                cnt_upid += 1
                            else:
                                cnt_upid = 1

                            idl = idk
                            countnoumber = int(time.strftime("%H%M%S")) * 100 + cnt_upid
                            print('id =', str(countnoumber), str(cnt_up), 'vehicles', 'crossed going up at',
                                  time.strftime("%c"))
                            # input database
                            sql = "INSERT INTO data_kend (ID, JML, TGL, BLN) VALUES (%s, %s, %s, %s)"
                            val = (countnoumber, cnt_up, time.strftime("%y/%m/%d"), time.strftime("%m"))
                            mycursor.execute(sql, val)
                            mydb.commit()
                            print(mycursor.rowcount, "record inserted.")

                            # cv2.imshow('Region of Interest', roi)
                            # cv2.imshow('Rectangle', rectangle)
                            # print "Area equal to ::::", area
                            cnt_down += 1
                            # print ("ID:", i.getId(), 'crossed going down at', time.strftime("%c"))
                        break
                    if i.getState() == '1':
                        if i.getDir() == 'down' and i.getY() > down_limit:
                            i.setDone()
                        elif i.getDir() == 'up' and i.getY() < up_limit:
                            i.setDone()
                    if i.timedOut():
                        # Remove from the list person
                        index = vehicles.index(i)
                        vehicles.pop(index)
                        del i
                if new == True:
                    p = Vehicle.MyVehicle(pid, cx, cy, max_p_age)
                    vehicles.append(p)
                    pid += 1

                ##################
                ##   DRAWING    ##
                ##################
                cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)
                img = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                # height = y+h
                # print 'height::::', height

                # print ('Rectangle size', img)
                # cv2.drawContours(frame, cnt, -1, (0, 255, 0), 3)
                # cv2.imshow('Image', cv2.resize(img, (400, 300)))

        for i in vehicles:
            cv2.putText(frame, str(i.getId()), (i.getX(), i.getY()), font, 1, i.getRGB(), 1, cv2.LINE_AA)

        ###############
        ##   IMAGE   ##
        ###############
        str_up = 'UP: ' + str(cnt_up)
        # frame = cv2.polylines(frame, [pts_L1], False, line_down_color, thickness=2)
        frame = cv2.polylines(frame, [pts_L2], False, line_up_color, thickness=2)
        frame = cv2.polylines(frame, [pts_L3], False, (255, 0, 255), thickness=1)  # garis atas
        # frame = cv2.polylines(frame, [pts_L4], False, (255,255,255), thickness=1) #garis bawah
        cv2.putText(frame, str_up, (20, 80), font, 3, (0, 0, 255), 2, cv2.LINE_AA)

        #cv2.imshow('Frame', cv2.resize(frame, (700, 600)))
        frame = cv2.imencode('.jpg', frame)[1].tobytes()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        #cv2.imshow('Frame', cv2.resize(frame, (1280, 720)))
        # cv2.imshow('Backgroud Subtraction', fgmask)

        # Abort and exit with 'Q' or ESC
        k = cv2.waitKey(1)
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run()
