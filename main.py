import pyodbc
import os
from flask import Flask, render_template, request, redirect, jsonify
from werkzeug.utils import secure_filename
import json
import datetime
import dateutil.parser

uploadFolder = './static/weddingImages'


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=BADIH-RYZEN\SQLEXPRESS;'
                      'Database=430PROJECT;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

currentUsername = ""

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = uploadFolder
@app.route("/")
def main():
    if __name__ == "__main__":
        return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("index.html", infoWrong = False)

@app.route('/signin', methods=['POST'])
def signin():
    username        = request.form['username2']
    passwordUser = request.form['password']
    SQL = "SELECT * FROM users WHERE username = '{}' and UserPassword = '{}'".format(username, passwordUser)
    result = conn.execute(SQL).fetchall()
    print(result)
    if (result):
        currentUsername = result[0][0]
        if(result[0][5]):
            return redirect('/adminPage')
        else:
            return redirect('/mainpage')
    else:
        return redirect('/login?wrongInfo=true')

@app.route('/signup', methods=['POST'])
def signup():
    username     = request.form['username']
    email        = request.form['email']
    firstName        = request.form['firstName']
    lastName        = request.form['lastName']
    passwordUser = request.form['password']
    SQL = "INSERT INTO users VALUES ('{}', '{}', '{}', '{}', '{}', 0)".format(username,email, firstName,lastName, passwordUser)
    try:
        conn.execute(SQL)
        conn.commit()
        currentUsername = username
        return redirect('/mainpage')
    except Exception as e:
        print(e)
        return redirect('/login?errorSignUp=true')

@app.route('/adminPage', methods=['GET'])
def adminPage():
    return render_template("adminPage.html")

@app.route('/adminWeddings', methods=['GET'])
def adminWeddings():
    weddingsList = []
    try:
        weddings = conn.execute("SELECT * FROM weddings").fetchall()
        print(weddings)
        for wedding in weddings:
            row = {
                "weddingID": str(wedding[0]),
                "brideName": str(wedding[1]),
                "groomName": str(wedding[2]),
                "weddingDate": str(wedding[3]),
                "venue": str(wedding[4]),
                "imageURL": str(wedding[5])
            }
            weddingsList.append(row)
        return render_template("adminWeddings.html", weddings=weddingsList)
    except Exception as e:
        print(e)

@app.route('/adminNoWeddings', methods=['GET'])
def noWedsAdmin():
    return render_template("adminNoWeds.html")

@app.route('/adminLetters', methods=['GET'])
def adminLetters():
    lettersList = []
    try:
        letters = conn.execute("SELECT * FROM congratulations").fetchall()
        print(letters)
        for letter in letters:
            row = {
                "weddingID": letter[0],
                "sender": letter[1],
                "congratsMessage": letter[2],
                "letterID": letter[3]
            }
            lettersList.append(row)
        return render_template("adminLetters.html", letters = lettersList)
    except Exception as e:
        print(e)
        return redirect('/emptyLetters')
    return redirect('/emptyLetters')

@app.route('/editLetter', methods=['GET', 'POST'])
def editLetter():
    letterID = request.args.get('letterIdToEdit')
    if request.method == 'GET':
        try:
            letter = conn.execute("SELECT * FROM congratulations WHERE messageID={}".format(letterID)).fetchall()[0]
            row = [{
                "weddingID": letter[0],
                "sender": letter[1],
                "message": letter[2],
                "messageID": letter[3]
            }]
        except Exception as e:
            print(e)
            return redirect('/emptyLetters')
        return render_template("editLetter.html", letter = row)

    else:
        message = request.form['message']
        messageID = request.form['messageID']
        try:
            conn.execute("""UPDATE congratulations
                            SET congratsMessage = '{}'
                            WHERE messageID={}
                            """.format(message,messageID))
            conn.commit()
            return redirect('/adminLetters')
        except Exception as e:
            return redirect('/adminLetters')

@app.route('/createLetter', methods=['GET', 'POST'])
def createLetter():
    if request.method == 'GET':
        weddingIDs = conn.execute("SELECT weddingID FROM weddings").fetchall()
        usernames = conn.execute("SELECT username FROM users").fetchall()
        for username in usernames:
            if username[0] == "admin":
                usernames.remove(username)
        return render_template("createLetter.html", weddingIDs=weddingIDs , usernames=usernames)
    else:
        username = request.form['username']
        weddingID = request.form['weddingID']
        messageContent = request.form['message']
        try:
            conn.execute("""
                            INSERT INTO congratulations
                            VALUES ({}, '{}', '{}')
                            """.format(weddingID, username, messageContent))
            conn.commit()
            return redirect('/adminLetters')
        except Exception as e:
            print(e)
            return redirect('/adminLetters')

@app.route('/emptyLetters', methods=['GET'])
def emptyLetters():
    return render_template("lettersEmpty.html")


@app.route('/deleteLetter', methods=['POST'])
def deleteLetter():
    letterToDelete = request.args.get('letterIdToEdit')
    print(letterToDelete)
    try:
        conn.execute("DELETE FROM congratulations WHERE messageID = {}".format(letterToDelete))
        conn.commit()
        return redirect('/adminLetters')
    except Exception as e:
        print(e)
    return redirect('/adminLetters')



@app.route('/adminContributions', methods=['GET'])
def adminContributions():
    contributionsList = []
    try:
        contributions = conn.execute("SELECT * FROM moneyTransfer").fetchall()
        for contribution in contributions:
            row = {
                "weddingID": contribution[0],
                "sender": contribution[1],
                "moneyAmount": contribution[2],
                "transactionID": contribution[3]
            }
            contributionsList.append(row)
        return render_template("adminContributions.html", contributions = contributionsList)
    except Exception as e:
        print(e)
        return redirect('/emptyContributions')
    return redirect('/emptyContributions')
    
@app.route('/editContribution', methods=['GET', 'POST'])
def editContribution():
    transactionID = request.args.get('contributionIdToEdit')
    print
    if request.method == 'GET':
        try:
            contribution = conn.execute("SELECT * FROM moneyTransfer WHERE transactionID={}".format(transactionID)).fetchall()[0]
            row = [{
                "weddingID": contribution[0],
                "sender": contribution[1],
                "moneyAmount": contribution[2],
                "transactionID": contribution[3]
            }]
            return render_template("editContributions.html", contribution = row)
        except Exception as e:
            print(e)
            return redirect('/emptyContributions')

    else:
        amount = request.form['amount']
        txID = request.form['txID']
        try:
            conn.execute("""UPDATE moneyTransfer
                            SET moneyAmount = {}
                            WHERE transactionID={}
                            """.format(amount,txID))
            conn.commit()
            return redirect('/adminContributions')
        except Exception as e:
            return redirect('/adminContributions')


@app.route('/createContribution', methods=['GET', 'POST'])
def createContribution():
    if request.method == 'GET':
        weddingIDs = conn.execute("SELECT weddingID FROM weddings").fetchall()
        usernames = conn.execute("SELECT username FROM users").fetchall()
        for username in usernames:
            if username[0] == "admin":
                usernames.remove(username)
        return render_template("createContribution.html", weddingIDs=weddingIDs , usernames=usernames)
    else:
        username = request.form['username']
        weddingID = request.form['weddingID']
        amount = request.form['amount']
        try:
            conn.execute("""
                            INSERT INTO moneyTransfer
                            VALUES ({}, '{}', {})
                            """.format(weddingID, username, amount))
            conn.commit()
            return redirect('/adminContributions')
        except Exception as e:
            print(e)
            return redirect('/adminContributions')

@app.route('/deleteContribution', methods=['POST'])
def deleteContribution():
    txID = request.form['txID']
    print(txID)
    try:
        conn.execute("DELETE FROM moneyTransfer WHERE transactionID = {}".format(txID))
        conn.commit()
        return redirect('/adminContributions')
    except Exception as e:
        print(e)
    return redirect('/adminContributions')

@app.route('/emptyContributions', methods=['GET'])
def emptyContributions():
    return render_template("emptyContributions.html")



@app.route('/adminUsers', methods=['GET'])
def adminUsers():
    try:
        usersList = []
        users = conn.execute("SELECT * FROM users").fetchall()
        for user in users:
            row = { 
                "username": user[0],
                "email": user[1],
                "FirstName": user[2],
                "LastName": user[3],
                "UserPassword": user[4], 
            }
            usersList.append(row)
    except Exception as e:
        print(e)
    return render_template("adminUsers.html", users=usersList)

@app.route('/deleteUser', methods=['POST'])
def deleteUser():
    usernameToDelete = request.args.get('usernameToEdit')
    print(usernameToDelete)
    try:
        conn.execute("DELETE FROM users WHERE username = '{}'".format(usernameToDelete))
        conn.commit()
        return redirect('/adminUsers')
    except Exception as e:
        print(e)
        return redirect('/adminUsers')

@app.route('/createUser', methods=['POST', 'GET'])
def addUser():
    if request.method == 'POST':
        usernameToEdit = request.form['username']
        email = request.form['email']
        FirstName = request.form['FirstName']
        LastName = request.form['LastName']
        UserPassword = request.form['UserPassword']
        try:
            conn.execute("INSERT INTO users VALUES ('{}', '{}', '{}', '{}', '{}', 0)".format(usernameToEdit,email,FirstName,LastName,UserPassword))
            conn.commit()
            return redirect('/adminUsers')
        except Exception as e:
            print(e)
            return redirect('/adminUsers')

    else:
        return render_template("createUser.html")
        

@app.route('/editUser', methods=['POST', 'GET'])
def editUser():
    usernameToEdit = request.args.get('usernameToEdit')
    if (request.method == 'GET'):
        try:
            user = conn.execute("SELECT * FROM users WHERE username='{}'".format(usernameToEdit)).fetchall()[0]
            row = [{ 
                "username": user[0],
                "email": user[1],
                "FirstName": user[2],
                "LastName": user[3],
                "UserPassword": user[4], 
            }]
            return render_template('editUser.html', userInfo = row)
        except Exception as e:
            print(e)
            return redirect('/adminUsers')

    if (request.method == 'POST'):
        usernameToEdit = request.form['username']
        email = request.form['email']
        FirstName = request.form['FirstName']
        LastName = request.form['LastName']
        UserPassword = request.form['UserPassword']
        try:
            conn.execute("""UPDATE users
                            SET username = '{}',
                            email ='{}',
                            FirstName ='{}',
                            LastName ='{}',
                            UserPassword = '{}'
                            WHERE username='{}'
                            """.format(usernameToEdit,email,FirstName,LastName,UserPassword, usernameToEdit))
            conn.commit()
            return redirect('/adminPage')
        except Exception as e:
            return redirect('/adminPage')

@app.route('/homepage', methods=['GET'])
def homepage():
    #weddings = conn.execute("SELECT weddingID FROM userAttending WHERE username = '{}'".format(currentUsername)).fetchall()
    username = request.args.get('username')
    adminMode = conn.execute("SELECT isAdmin FROM users WHERE username='{}'".format(username)).fetchall()[0][0]
    if (adminMode):
        try:
            weddingsIDs = conn.execute("SELECT weddingID FROM weddings").fetchall()
        except Exception as e:
            pass
    else:
        try:
            weddingsIDs = conn.execute("SELECT weddingID FROM userAttending WHERE username = '{}'".format(username)).fetchall()
        except Exception as e:
            pass
    weddingsList = []
    def getJSON(weddingID, brideName, groomName, weddingDate, venue, imageURL):
        return jsonify(weddingID= weddingID,
                       brideName = brideName,
                       groomName = groomName,
                       weddingDate = weddingDate,
                       venue = venue,
                       imageURL = imageURL)
    for weddingID in weddingsIDs:
        result = conn.execute("SELECT * FROM weddings WHERE weddingID = {}".format(int(weddingID[0]))).fetchall()[0]
        row = {
            "weddingID": str(result[0]),
            "brideName": str(result[1]),
            "groomName": str(result[2]),
            "weddingDate": str(result[3]),
            "venue": str(result[4]),
            "imageURL": str(result[5])
        }
        weddingsList.append(row)
    print(weddingsList)
    
    if (adminMode):
        return render_template("homepage.html", weddings = weddingsList)
    else:       
        return render_template("homepage.html", weddings = weddingsList)

@app.route('/mainpage', methods=['GET'])
def mainpage():
    return render_template("mainpage.html")

@app.route('/noWedding', methods=['GET'])
def noWedding():
    return render_template("noWedding.html")

@app.route('/myWedding', methods=['GET'])
def myWedding():
    username = request.args.get('username')
    weddingID = request.args.get('weddingID')
    if(not weddingID):
        try:
            weddingID = conn.execute("SELECT weddingID FROM hasWeddings WHERE username='{}'".format(username)).fetchall()[0][0]
        except Exception as e:
            print(e)
            return redirect('/noWedding')
    result = conn.execute("SELECT * FROM weddings WHERE weddingID = {}".format(weddingID)).fetchall()[0]
    attendeesUsernames = conn.execute("SELECT username FROM userAttending WHERE weddingID = {}".format(weddingID)).fetchall()
    attendeesNames = []
    guestEmails = []
    for attendeesUsername in attendeesUsernames:
        result2 = conn.execute("SELECT FirstName,LastName FROM users WHERE username = '{}'".format(attendeesUsername[0])).fetchall()[0]
        guestEmail = conn.execute("SELECT email FROM users WHERE username = '{}'".format(attendeesUsername[0])).fetchall()[0][0]
        guestEmails.append(guestEmail)
        name = result2[0] + " " + result2[1]
        attendeesNames.append(name)
    
    #Get contribution
    #Money
    moneyContributionsList = []
    try:
        moneyContributions = conn.execute("SELECT username,moneyAmount,transactionID FROM moneyTransfer WHERE weddingID={}".format(weddingID)).fetchall()
        for moneyContribution in moneyContributions:
            FirstLastName = conn.execute("SELECT FirstName,LastName from users WHERE username = '{}'".format(moneyContribution[0])).fetchall()[0]
            fullName = FirstLastName[0] + " " + FirstLastName[1]
            #moneyContributionsList.append({fullName: moneyContribution[1]})
            moneyContributionsList.append({
                "name": fullName,
                "amount": moneyContribution[1],
                "txID": moneyContribution[2]
            })
    except Exception as e:
        print(e)
        print("No Money contributions")

    #Congrats
    congratsList = []
    try:
        congrats = conn.execute("SELECT username,congratsMessage,messageID FROM congratulations WHERE weddingID={}".format(weddingID)).fetchall()
        for congrat in congrats:
            FirstLastName = conn.execute("SELECT FirstName,LastName from users WHERE username = '{}'".format(congrat[0])).fetchall()[0]
            fullName = FirstLastName[0] + " " + FirstLastName[1]
            #congratsList.append({fullName: congrat[1]})
            congratsList.append({
                "name": fullName,
                "message": congrat[1],
                "mesID": congrat[2]
            })
    except Exception as e:
        print(e)
        print("No Congratulation Letters")

    print(moneyContributionsList)
    print(congratsList)
    return render_template("myWedding.html",
                            weddingDets = result,
                            attendees = attendeesNames,
                            guestEmails = guestEmails,
                            congratsMessages = congratsList,
                            moneyContributions = moneyContributionsList)

@app.route('/alreadyHasWedding', methods=['GET'])
def alreadyHasWedding():
    return render_template("alreadyHasWedding.html")

@app.route('/createWedding', methods=['GET', 'POST'])
def createWedding():

    if request.method == 'GET':
        username = request.args.get('username')
        print(username)
        try:
            weddingID = conn.execute("SELECT weddingID from hasWeddings WHERE username = '{}'".format(username)).fetchall()[0][0]
            return redirect('/alreadyHasWedding')
        except Exception as e:
            print(e)
            return render_template("createWedding.html")

    elif request.method == 'POST':
        username = request.args.get('username')
        usernameSave = request.args.get('username')
        if (username == "admin"):
            username = request.form['username'] 
        brideName = request.form['bname']
        groomName = request.form['gname']
        dateDay   = request.form['date']
        dateTime  = request.form['time']
        venue     = request.form['location']
        guests    = request.form.getlist('guest[]')
        fulldate = dateDay + " " + dateTime
        picture   = request.form['picture']
        print(brideName)
        print(groomName)
        print(fulldate)
        print(venue)
        #print(guests)
        #Creating the wedding
        weddingID = -1
        try:
            conn.execute("INSERT INTO weddings VALUES (?, ?, ?, ?, ?)", brideName, groomName, fulldate, venue, picture)
            conn.commit()
            weddingID = conn.execute("SELECT MAX(weddingID) FROM weddings").fetchall()[0][0]
            #pictureName = secure_filename(picture.filename)
            #pictureName = str(weddingID) + "-" + pictureName
            #picture.save(os.path.join(app.config['UPLOAD_FOLDER'], pictureName))
        except Exception as e:
            print(e)
            if(usernameSave == "admin"):
                return redirect('/adminWeddings')
            return redirect('/mainpage')
            
        #Add the guests
        for guest in guests:
            try:
                usernameGuest = conn.execute("SELECT username FROM users WHERE email=?", guest).fetchall()[0][0]
                if username == usernameGuest:
                    continue
                conn.execute("INSERT INTO userAttending VALUES (?, ?)", usernameGuest, weddingID)
                conn.commit()
            except Exception as e:
                print(e)


        #Associating wedding with username
        try:
            #username = conn.execute("SELECT username FROM users WHERE email=?", email).fetchall()[0][0]
            conn.execute("INSERT INTO hasWeddings VALUES (?, ?)", weddingID, username)
            conn.commit()
            if(usernameSave == "admin"):
                return redirect('/adminWeddings')
            return redirect('/mainpage')
        except Exception as e:
            print(e)
            if(usernameSave == "admin"):
                return redirect('/adminWeddings')
            return redirect('/mainpage')
        if(usernameSave == "admin"):
            return redirect('/adminWeddings')
        return redirect('/mainpage')

@app.route('/updateWedding', methods=['POST'])
def updateWedding():
    #Get update info
    username =  request.args.get('username')
    weddingID = request.args.get('weddingID')
    print(weddingID)
    brideName = request.form['bname']
    groomName = request.form['gname']
    fulldate   = dateutil.parser.parse(request.form['date'])
    print (fulldate)
    venue     = request.form['location']
    imageURL = request.form['imageURL']
    guests    = request.form.getlist('guest[]')
    
    try:
        conn.execute("""UPDATE weddings
                        SET brideName = '{}',
                        groomName = '{}',
                        weddingDate = '{}',
                        venue = '{}',
                        imageURL = '{}'              
                        WHERE weddingID={}""".format(brideName,groomName,fulldate,venue, imageURL, weddingID))
        conn.commit()
    except Exception as e:
        print(e)

    #Update invitees
    try:
        conn.execute("""DELETE FROM userAttending
                        WHERE weddingID={}
                        """.format(weddingID))
        conn.commit()
    except Exception as e:
        print(e)
    #Add the guests
    for guest in guests:
        try:
            usernameGuest = conn.execute("SELECT username FROM users WHERE email=?", guest).fetchall()[0][0]
            if username == usernameGuest:
                continue
            conn.execute("INSERT INTO userAttending VALUES (?, ?)", usernameGuest, weddingID)
            conn.commit()
        except Exception as e:
            print(e)


    return redirect('/myWedding?username={}&weddingID={}'.format(username,weddingID))


@app.route('/weddingDetail', methods = ['GET'])
def weddingDetail():
    username = request.args.get('username')
    weddingID = request.args.get('weddingID')
    result = conn.execute("SELECT * FROM weddings WHERE weddingID = {}".format(weddingID)).fetchall()[0]
    attendeesUsernames = conn.execute("SELECT username FROM userAttending WHERE weddingID = {}".format(weddingID)).fetchall()
    attendeesNames = []
    for attendeesUsername in attendeesUsernames:
        result2 = conn.execute("SELECT FirstName,LastName FROM users WHERE username = '{}'".format(attendeesUsername[0])).fetchall()[0]
        name = result2[0] + " " + result2[1]
        attendeesNames.append(name)
    print(attendeesNames)
    return render_template('weddingDetail.html', weddingDets = result, attendees = attendeesNames)


@app.route('/sendCongrats', methods=['POST'])
def sendCongrats():
    username = request.args.get('username')
    weddingID = request.args.get('weddingID')
    congratsMessage = request.form['congratsMessage']
    if (not congratsMessage):
        return redirect('/weddingDetail?username={}&weddingID={}'.format(username, weddingID))
    try:
        conn.execute("""INSERT INTO congratulations
                        (weddingID, username, congratsMessage)
                        VALUES ({}, '{}', '{}');
                        """.format(weddingID,username, congratsMessage, congratsMessage))
        conn.commit()
    except Exception as e:
        print(e)
        conn.execute("""UPDATE congratulations
                        SET congratsMessage='{}'
                        WHERE weddingID={} AND username='{}';
                        """.format(congratsMessage, weddingID, username))
        conn.commit()
    return redirect('/weddingDetail?username={}&weddingID={}'.format(username, weddingID))


@app.route('/sendMoney', methods=['POST'])
def sendMoney():
    username = request.args.get('username')
    weddingID = request.args.get('weddingID')
    moneyAmount = int(request.form['amount'])
    if (moneyAmount <= 0):
        return redirect('/weddingDetail?username={}&weddingID={}&negativeAmount=true'.format(username, weddingID))
    if (not moneyAmount):
        return redirect('/weddingDetail?username={}&weddingID={}'.format(username, weddingID))
    try:
        conn.execute("""INSERT INTO moneyTransfer
                        (weddingID, username, moneyAmount)
                        VALUES ({}, '{}', {})
                        """.format(weddingID,username, moneyAmount))
        conn.commit()
    except Exception as e:
        print(e)
        conn.execute("""UPDATE moneyTransfer
                        SET moneyAmount={}
                        WHERE weddingID={} AND username='{}';
                        """.format(moneyAmount, weddingID, username))
        conn.commit()
    return redirect('/weddingDetail?username={}&weddingID={}'.format(username, weddingID))

@app.route('/deleteWedding', methods=['POST'])
def deleteWedding():
    weddingID = request.args.get('weddingID')
    username = request.args.get('username')
    try:
        conn.execute("DELETE FROM weddings WHERE weddingID = {}".format(weddingID))
        conn.commit()
        if(username == "admin"):
            return redirect('/adminWeddings')
        return redirect('/mainpage')
    except Exception as e:
        print(e)
        return redirect('/weddingDetail?username={}&weddingID={}'.format(username, weddingID))



@app.route('/adminHasWeddings', methods=['GET'])
def adminHasWeddings():
    ownershipList = []
    ownerships = conn.execute("SELECT * FROM hasWeddings").fetchall()
    for ownership in ownerships:
        row = {
            "weddingID": ownership[0],
            "username": ownership[1],
            "ownershipID": ownership[2]
        }
        ownershipList.append(row)
    usersWithNoWeds = conn.execute("""SELECT DISTINCT U.username
                                      FROM users U, hasWeddings H
                                      WHERE NOT EXISTS (SELECT *
                                                        FROM hasWeddings H1
                                                        WHERE U.username = H1.username)
                                      """).fetchall()
    for usersWithNoWed in usersWithNoWeds:
        if usersWithNoWed[0] == "admin":
            usersWithNoWeds.remove(usersWithNoWed)
    return render_template("adminHasWeddings.html", ownerships=ownershipList, freeUsers = usersWithNoWeds)

@app.route('/editOwnerShip', methods=['POST'])
def editOwnerShip():
    ownershipID = request.args.get('ownershipID')
    username = request.form['username']
    try:
        conn.execute("""UPDATE hasWeddings
                        SET username='{}'
                        WHERE ownershipID={}        
                        """.format(username, ownershipID))
        conn.commit()
    except Exception as e:
        print(e)
    return redirect('/adminHasWeddings')


@app.errorhandler(404)
def not_found(e):
    return render_template("noPageFound.html")
            