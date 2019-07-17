"""

Author      : Digambar Gadekar
Created At  : 16 July 2019
Description : This is sample flask application to select the team member from team
Dependancies: Data file "data/cricketTeamMemberList2nd.json" which contain company details.

"""

from flask import Flask, request, jsonify
import json
import os
import collections
import operator
import codecs

app = Flask(__name__)
app.config["DEBUG"] = True

data_source = os.path.join(os.path.dirname(
   os.path.realpath(__file__)), "database/cricketTeamMemberList.json")


'''
    Author : Digambar Gadekar  // Last modifide : 16 - 07 - 2019
    Discription : This Function is for read all the input data 
'''
def read_json_data(data_source):
   fp = open(data_source, encoding="utf8")
   data = json.load(codecs.open(data_source, 'r', 'utf-8-sig'))
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
    Discription : This API is to get all the team member of all country
'''
@app.route('/api/v1/resourcess/team/all', methods=['GET'])
# http://localhost:8888/api/v1/resourcess/team/all

def makeLogoByNameAll():   
    teamMemberDetails = read_json_data(data_source)
    if len(teamMemberDetails) > 0:
        result = {
            "status": "200",
            "data": teamMemberDetails
        }
    else:
        result = {
            "status": "Not available",
            "data": "No data found!"
        } 
    return jsonify(result)
 

################################### Country basis API Section ##################################### 
# http://localhost:8888/api/v1/resources/teamName?id=India
@app.route('/api/v1/resources/teamName', methods=['GET'])
def makeLogoByName():
    try:
        if 'id' in request.args:
            id = str(request.args['id'])
            teamMemberDetails = read_json_data(data_source)
            selectedTeamMemberList = []
            for company in range(len(teamMemberDetails)):
                Team = teamMemberDetails[company]['Team']
                if Team == id:
                    playerName = teamMemberDetails[company]['Name']
                    print(playerName)
                    selectedTeamMemberList.append(teamMemberDetails[company])

            result = {
                "status": "200",
                "data": selectedTeamMemberList
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