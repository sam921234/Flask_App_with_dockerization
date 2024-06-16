import pickle
from flask import Flask,request

#creating an instance of Flask class by passing name of the file
app = Flask(__name__)

## loading the pickle file and storing model inside a variable

model_pickle = open("./artefacts/car_pred.pkl","rb")
clf = pickle.load(model_pickle)

#defining endpoint functions
## mapping of end point function to an url happens via a decorator 
#### @name_of_file.route('/endpoint function name',method=['GET',"POST"])
#### method is depending on requirement
@app.route("/ping",methods = ["GET"])
def ping():
    return {'message':"Hi there, I'm Jeet !"}

## defining endpoint function that makes the prediction
@app.route("/predict", methods=['POST'])
def prediction():
     """ Returns loan application status using ML model """ 
     loan_req = request.get_json() 
     print(loan_req) 
     
     if loan_req['Gender'] == "Male": 
        Gender = 0 
     else: 
         Gender = 1 
     
     if loan_req['Married'] == "Unmarried": 
        Married = 0 
     else: 
        Married = 1 
     
     if loan_req['Credit_History'] == "Unclear Debts": 
        Credit_History = 0 
     else: 
        Credit_History = 1 
     
     ApplicantIncome = loan_req['ApplicantIncome'] 
     
     LoanAmount = loan_req['LoanAmount'] 
     result = clf.predict([[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]]) 
     
     if result == 0: 
        pred = "Rejected" 
     else:
        pred = "Approved" 
     return {"loan_approval_status": pred}