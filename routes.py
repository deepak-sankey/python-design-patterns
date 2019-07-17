"""
Author      : Deepak Terse
Created At  : 15 July 2019
Description : All routes are specified here
"""

from flask import render_template
from flask import request, jsonify

from app import app

# Views:
@app.route('/')
def index():
    return "Server Working"

@app.route('/addPlayer', methods=['POST'])
def addPlayer():
    responseData = {}
    print(responseData)
    
    return jsonify(responseData), 200

@app.route('/updatePlayer', methods=['POST'])
def updatePlayer():
    responseData = {}
    print(responseData)
    
    return jsonify(responseData), 200

@app.route('/deletePlayer', methods=['POST'])
def deletePlayer():
    responseData = {}
    print(responseData)
    
    return jsonify(responseData), 200

@app.route('/viewPlayers', methods=['POST'])
def viewPlayers():
    responseData = {}
    print(responseData)
    
    return jsonify(responseData), 200

@app.route('/sampleApiCall', methods=['POST'])
def sampleApiCall():
    responseData = {}
    print(responseData)
    
    return jsonify(responseData), 200


"""

Author      : Digambar Gadekar
Created At  : 27 June 2019
Description : This is sample flask application to make logo by company name
Dependancies: Data file "data/companyList.json" which contain company details.

"""

from flask import Flask, request, jsonify
import json
import os
import collections
import operator

app = Flask(__name__)
app.config["DEBUG"] = True

data_source = os.path.join(os.path.dirname(
   os.path.realpath(__file__)), "data/CompaniesNameList.json")


'''
    Author : Digambar Gadekar  // Last modifide : 27 - 06 - 2019
    Discription : This Function is for read all the input data 
'''
def read_json_data(data_source):
   # fp = open(data_source, 'r')
   fp = open(data_source, encoding="utf8")

   data = json.loads(fp.read())
   return data

################################### API For All Company name #####################################
'''
    Author : Digambar Gadekar  // Last modifide : 30 - 06 - 2019
    Discription : This section is for errror handaling
'''
@app.errorhandler(404)
def page_not_found(e):
   return jsonify({"status": "404", "data": "Page Not Found!"})


'''
    Author : Digambar Gadekar  // Last modifide : 30 - 06 - 2019
    Discription : This Route is for All the company name
'''
@app.route('/api/v1/resourcess/companies/all', methods=['GET'])

#Discription : This function is for choose char  by Company name to make Company logo.
def makeLogoByNameAll():   
    try:
        companyDetails = read_json_data(data_source)
        #This loop occure till range of input data (No of company)
        for company in range(len(companyDetails)):
            #Validate Company Name is present in Dictionory : If Yes Loop continue  , Else Key error
            if ('Company Name' in companyDetails[int(company)]):
                companyName = companyDetails[company]['Company Name']
                if len(companyName) > 0:
                    occurenceList = []
                    occurenceList = charOccurence(str(companyName))
                    logoName = chooseCharForLogo(occurenceList)
                    #If logoName is not 404 , Put in database
                    if logoName != 404:
                        companyDetails[company].update(logoName = logoName)
                    else:
                        companyDetails[company].update(logoName = "")
                    result = {
                        "status": "200",
                        "data": companyDetails
                    }
                else:
                    result = {
                        "status": "404",
                        "data": "No Company data found!"
                    } 
        return jsonify(result)
    except:
        result = {
           "status": "404",
           "data": "No Company data found!"
       }
    return jsonify(result)


'''
    Author : Digambar Gadekar  // Last modifide : 30 - 06 - 2019
    Discription : This Function is for chose the char by condition and make the 3 char string for "Company Logo"
        Condition 1 : Most occurence char of string
        Condition 2 : Alphabetical order if same occurence
'''
def chooseCharForLogo(occurenceList):
    logoName = ""
    try:
        occurenceList = sorted(occurenceList, key=lambda x: (-occurenceList[x], x))
        sortedoccurenceList = occurenceList[0:3]
        logoName = listToString(sortedoccurenceList)
        return logoName
    except:
        return 404


'''
    Author : Digambar Gadekar  // Last modifide : 30 - 06 - 2019
    Discription : #This function is for convert the List in to string 
'''
def listToString(list):  
    res = ""
    if(len(list) != 0):
        s = [str(i) for i in list] 
        # Join list items using join() 
        res = "".join(s)
    return(res) 


'''
    Author : Digambar Gadekar  // Last modifide : 30 - 06 - 2019
    Discription : #This function is for check the char occurence
'''
def charOccurence(str):
   occurence = {}
   for c in str:
       if c != " ":
           occurence[c] = str.count(c)
   return occurence



################################### ID basis API Section ##################################### 
@app.route('/api/v1/resources/CompaniesList', methods=['GET'])
def makeLogoByName():
    """
        Check if an ID was provided as part of the URL.
        If ID is provided, assign it to a variable.
        If no ID is provided, display an error in the browser.
    """
    try:
        if 'id' in request.args:
            id = str(request.args['id'])
            companyDetails = read_json_data(data_source)
            for company in range(len(companyDetails)):
                companyId = companyDetails[company]['CompanyId']
                if companyId == id:
                    print(companyDetails[company])
                    companyName = companyDetails[company]['Company Name']
                    if len(companyName) > 0:
                        occurenceList = []
                        occurenceList = charOccurence(str(companyName))
                        logoName = chooseCharForLogo(occurenceList)
                        print(logoName)
                        if logoName != 404:
                            companyDetails[company].update(logoName = logoName)
                        else:
                            companyDetails[company].update(logoName = "")
                        result = {
                            "status": "200",
                            "data": companyDetails[company]
                        }
        else:
            return jsonify({"status": "200", "data": "Please specify Company ID!"})
    except:
        result = {
                    "status": "404",
                    "data": "No Company data found!"
                }
    return jsonify(result)


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=8888)