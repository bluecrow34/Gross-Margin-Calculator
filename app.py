
from flask import Flask, redirect, request, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from calculations import calRevenue, calTotalPay, calTotalCost, calTotalComp, calTotalGM, calGM, highlight_values, calTotalBurden, calBurden, calSick, calWorkComp, calPerm


app= Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'itsasecret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SQLALCHEMY_ECHO'] = True 
toolbar = DebugToolbarExtension(app)

app.app_context().push()

#connect_db(app)
#db.create_all


@app.route('/')
def home():
    """Home Page"""
    return render_template('base.html')
    
@app.route('/converted', methods=["POST", "GET"])
def convert():
        bill_rate = int(request.form.get('bill'))     
        pay_rate = int(request.form.get('pay'))
        hrPerWk = int(request.form.get('Hours_Per_Week'))
        assignmentWks = int(request.form.get('weeks_assignment'))
        selectedState = request.form.get('states')
#        permFee = int(request.form.get('permFee'))
#        salary = int(request.form.get('salary'))

        try:

            weekBill = round(calRevenue(bill_rate,hrPerWk), 2)
            weekPay = round(calTotalPay(pay_rate,hrPerWk),2)
            burdenRate = round(calBurden(weekPay, selectedState),2)
    #       workCompRate = round(calWorkComp(weekPay, selectedState),2)
            sickTimeRate = round(calSick(weekPay, selectedState),2)
            totalBurden = round(calTotalBurden(burdenRate, sickTimeRate),2)
            totalComp = round(calTotalComp(weekPay,totalBurden),2)
            totalCost = round(calTotalCost(totalComp, assignmentWks),2)
            totalRevenue = round(calRevenue(weekBill,assignmentWks),2)
            totalGM = round(calTotalGM(totalRevenue,totalCost),2)
            grossMargin = round(calGM(totalGM,totalRevenue), 2)
#            totalRevenue = round(calPerm(permFee, salary),2)
        except ValueError:
            flash("Invalid input. Please enter numeric values.")
            return render_template('converted.html', error="Invalid number entered")
    

        return render_template('converted.html', weekBill=weekBill, 
                            weekPay=weekPay, totalCost=totalCost, 
                            totalComp=totalComp, totalRevenue=totalRevenue,
                            totalGM=totalGM, grossMargin=grossMargin,
                            totalBurden=totalBurden, selectedState=selectedState, 
                            sickTimeRate=sickTimeRate, burdenRate=burdenRate )

@app.route("/404")
def four_0four(e):

    return render_template('404.html'), 404
 



if __name__=="__main__":
    app.run(debug=True)