#import PyMongo as PyMongo
from flask import Flask, render_template, request
from flask_pymongo import PyMongo
import numpy as np
import pickle
import joblib
import sklearn



import json


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/road_collusion"
app.config["MONGO_DBNAME"] = "road_collusion"
mongo = PyMongo(app)

db_collection = mongo.db.collusion


################# Global Variables ################

week = [1,2,3,4,5,6,7]
month = [1,2,3,4,5,6,7,8,9,10,11,12]
year = [1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
month_data=[]




########## Month data counting and put it in an array  #########

month_label = list(db_collection.distinct("C_MNTH"))

for items in month:
    count_month = db_collection.find({"C_MNTH": items}).count()
    month_data = np.append(month_data, count_month)

@app.route('/')
def home():
   # data_array = [20, 1, 3 , 13, 1, 6, 0, 16, 90, 22]
    #print(data_array)

    #final_model = joblib.load(open("/Users/tasrifahmed/PyProjects/collusion_Project/random_forest_model.sav", "rb"))
    #final_model = pickle.load(open("random_forest_model.sav", "rb"))
    #Prediction = final_model.predict(np.array([data_array]))
    #print(Prediction)#




    count_all = db_collection.count()
    max_in_month = np.max(month_data)
    ave_in_month = int(np.average(month_data))

    ##### RoadWay Collusion ######

    def road_conf_year(year, road_config):
        config_query = db_collection.find({"C_YEAR":{"$eq":year}, "C_RCFG":{"$eq":road_config}}).count()
        return config_query

    year_2011_1 = road_conf_year(2011, 1)
    year_2011_2 = road_conf_year(2011, 2)
    year_2011_3 =road_conf_year(2011, 3)

    year_2012_1 = road_conf_year(2012, 1)
    year_2012_2 = road_conf_year(2012, 2)
    year_2012_3 = road_conf_year(2012, 3)

    year_2013_1 = road_conf_year(2013, 1)
    year_2013_2 = road_conf_year(2013, 2)
    year_2013_3 = road_conf_year(2013, 3)

    year_2014_1 = road_conf_year(2014, 1)
    year_2014_2 = road_conf_year(2014, 2)
    year_2014_3 = road_conf_year(2014, 3)

    year_2015_1 = road_conf_year(2015, 1)
    year_2015_2 = road_conf_year(2015, 2)
    year_2015_3 = road_conf_year(2015, 3)

    year_2016_1 = road_conf_year(2016, 1)
    year_2016_2 = road_conf_year(2016, 2)
    year_2016_3 = road_conf_year(2016, 3)

    year_2017_1 = road_conf_year(2017, 1)
    year_2017_2 = road_conf_year(2017, 2)
    year_2017_3 = road_conf_year(2017, 3)


########## Count Year Collusion ############

    count_2015 = db_collection.find({"C_YEAR": 2015}).count()
    count_2016 = db_collection.find({"C_YEAR": 2016}).count()
    count_2017 = db_collection.find({"C_YEAR": 2017}).count()



############## Colusion due to weather###############

    rain_count = db_collection.find({"C_WTHR": 3}).count()
    clear_count = db_collection.find({"C_WTHR": 1}).count()
    snow_count = db_collection.find({"C_WTHR": 4}).count()


################ Max count Time ##############


    hour_count = db_collection.find({"C_HOUR": {"$gt": 15, "$lt":22}}).count()



    return render_template('index.html', count_all = count_all, month_max = max_in_month , average = ave_in_month,
                year_2011_2 = year_2011_2, year_2011_3= year_2011_3,year_2011_1=year_2011_1, year_2012_1=year_2012_1,
                year_2012_2 = year_2012_2, year_2012_3 = year_2012_3, year_2013_1 =year_2013_1, year_2013_2 = year_2013_2,
                year_2013_3 = year_2013_3, year_2014_1=year_2014_1,year_2014_2=year_2014_2,year_2014_3=year_2014_3,year_2015_1=year_2015_1,
                year_2015_2 = year_2015_2, year_2015_3=year_2015_3, year_2016_1=year_2016_1, year_2016_2=year_2016_2,
                year_2016_3=year_2016_3, year_2017_1=year_2017_1, year_2017_2 =year_2017_2, year_2017_3=year_2017_3,
                count_2015 = count_2015, count_2016=count_2016, count_2017=count_2017, rain_count=rain_count, clear_count=clear_count,
                snow_count = snow_count, hour_count=hour_count










                           )


@app.route('/charts', methods=["GET"])
def charts():

#Line chart making data

    year_data = []
    year_label = list(db_collection.distinct("C_YEAR"))
    for items in year:
        count_year = db_collection.find({"C_YEAR": items}).count()
        year_data = np.append(year_data,count_year)

    count_1999 = db_collection.find({"C_YEAR": 1999}).count()
    count_2014 = db_collection.find({"C_YEAR": 2014}).count()
    count_all = db_collection.count()


#Count Mail and female number from database
    count_male= db_collection.find({"P_SEX": "M"}).count()
    count_female = db_collection.find({"P_SEX": "F"}).count()

    age_list = list(db_collection.distinct("P_AGE"))


####### bar chart data ######
    count_jan = db_collection.find({"C_MNTH": 1}).count()
    count_oct = db_collection.find({"C_MNTH": 10}).count()

    #month_data = np.array([count_jan, count_feb, count_mar, count_apr,count_may, count_jun, count_jul, count_aug,
                          # count_sep, count_oct, count_nov, count_dec])



################# Age distribution on donut chart #################

    young_age = db_collection.find({"P_AGE": {"$gt": 15, "$lt":28}}).count()
    middle_age = db_collection.find({"P_AGE": {"$gt": 29, "$lt":45}}).count()
    old_age = db_collection.find({"P_AGE": {"$gt": 46, "$lt":100}}).count()


################ Daywise Collusion ##################



    collusion_monday_clear = db_collection.find({"C_WDAY":1, "C_WTHR":1}).count()
    collusion_tuesday_clear = db_collection.find({"C_WDAY":2, "C_WTHR":1}).count()
    collusion_wedensday_clear = db_collection.find({"C_WDAY":3, "C_WTHR":1}).count()
    collusion_thursday_clear = db_collection.find({"C_WDAY":4, "C_WTHR":1}).count()
    collusion_friday_clear = db_collection.find({"C_WDAY":5, "C_WTHR":1}).count()
    collusion_saturday_clear = db_collection.find({"C_WDAY":6, "C_WTHR":1}).count()
    collusion_sunday_clear = db_collection.find({"C_WDAY":7, "C_WTHR":1}).count()
    data_sunny= np.array([collusion_monday_clear, collusion_tuesday_clear, collusion_wedensday_clear, collusion_thursday_clear,
                          collusion_friday_clear, collusion_saturday_clear, collusion_sunday_clear ])
    total_data_clear = np.sum(data_sunny)

    collusion_monday_snow = db_collection.find({"C_WDAY":1, "C_WTHR":4}).count()
    collusion_tuesday_snow = db_collection.find({"C_WDAY":2, "C_WTHR":4}).count()
    collusion_wedensday_snow = db_collection.find({"C_WDAY":3, "C_WTHR":4}).count()
    collusion_thursday_snow = db_collection.find({"C_WDAY":4, "C_WTHR":4}).count()
    collusion_friday_snow = db_collection.find({"C_WDAY":5, "C_WTHR":4}).count()
    collusion_saturday_snow =db_collection.find({"C_WDAY":6, "C_WTHR":4}).count()
    collusion_sunday_snow = db_collection.find({"C_WDAY":7, "C_WTHR":4}).count()
    data_snow = np.array([collusion_monday_snow, collusion_tuesday_snow, collusion_wedensday_snow,collusion_thursday_snow,
                          collusion_friday_snow, collusion_saturday_snow, collusion_sunday_snow  ])

    total_data_snow = np.sum(data_snow)




    collusion_monday_rain = db_collection.find({"C_WDAY":1, "C_WTHR":3}).count()
    collusion_tuesday_rain = db_collection.find({"C_WDAY":2, "C_WTHR":3}).count()
    collusion_wedensday_rain = db_collection.find({"C_WDAY":3, "C_WTHR":3}).count()
    collusion_thursday_rain = db_collection.find({"C_WDAY":4, "C_WTHR":3}).count()
    collusion_friday_rain = db_collection.find({"C_WDAY":5, "C_WTHR":3}).count()
    collusion_saturday_rain =db_collection.find({"C_WDAY":6, "C_WTHR":3}).count()
    collusion_sunday_rain = db_collection.find({"C_WDAY":7, "C_WTHR":3}).count()
    data_rain = np.array([collusion_monday_rain, collusion_tuesday_rain, collusion_wedensday_rain,collusion_thursday_rain,
                          collusion_friday_rain, collusion_saturday_rain, collusion_sunday_rain  ])

    total_data_rain = np.sum(data_rain)
    ################### Day wise collusion Polar Chart ###################

    day_wise =[]

    for day in week:
        collusio_day_wise = db_collection.find({"C_WDAY":day}).count()
        day_wise = np.append(day_wise, collusio_day_wise)
    print(day_wise)



    return render_template('charts.html', year_labels = year_label, count_1999= count_1999, count_2014=count_2014,count_all=count_all,
                        year_data =year_data,  count_m = count_male, count_f = count_female,  age = age_list,
                           month_data =month_data, month_label= month_label, count_jan = count_jan, count_oct = count_oct,
                        young_age=young_age, middle_age=middle_age,old_age=old_age, data_sunny=data_sunny, data_snow=data_snow, data_rain=data_rain,
                        total_data_snow=total_data_snow, total_data_clear=total_data_clear, total_data_rain=total_data_rain,
                        day_wise=day_wise


                           )


@app.route('/tables', methods=["GET"])
def tables():
    all_data = list(db_collection.find({}))
    return render_template('tables.html', show_data = all_data )


@app.route('/forms')
def forms():


    return render_template('form.html')

@app.route('/submitted', methods=['POST'])
def submit():
    global year, month

    def year_input_change(year1):
        converter = {

            0:"1999",
            1:"2000",
            2:"2001",
            3:"2002",
            4:"2003",
            5:"2004",
            6:"2005",
            7:"2006",
            8:"2007",
            9:"2008",
            10:"2009",
            11:"2010",
            12:"2011",
            13:"2012",
            14:"2013",
            15:"2014",
            16:"2015",
            17:"2016",
            18:"2018",
            19:"2019",
            20:"2020",
            21:"2021"
        }
        return converter.get(year1, "nothing")


    year_initial = int(request.form.get("year"))
    print(year_initial)
    year_final =  year_input_change(year_initial)
    print(year_final)
    print(year_final)
    month = int(request.form.get("month"))
    day = int(request.form.get("day"))
    hour = int(request.form.get("hour"))
    v_number = int(request.form.get("v_number"))
    road = int(request.form.get("road"))
    weather = int(request.form.get("weather"))
    traffic = int(request.form.get("traffic"))
    v_year = int(request.form.get("v_year"))
    age = int(request.form.get("age"))
    #db_collection.insert_one({'C_YEAR': year_final, 'C_MNTH': month , 'C_WDAY': day, 'C_HOUR': hour , 'C_VEHS': v_number , 'C_CONF': road,
                              #'C_WTHR': weather, 'C_TRAF':traffic , 'V_YEAR':v_year , 'P_AGE':age })

    data_array =  np.array([year_initial,month,day,hour,v_number,road,weather,traffic,v_year,age])
    print(data_array)
    #[9, 10, 2, 55, 2, 15, 0, 16, 94, 28]

    final_model = pickle.load(open("random_forest_model.sav", "rb"))
    Prediction_initial = final_model.predict(np.array([data_array]))
    print(Prediction_initial)
    final_prediction = int(Prediction_initial[0])
    print(final_prediction)

    db_collection.insert_one(
        {'C_YEAR': year_final, 'C_MNTH': month, 'C_WDAY': day, 'C_HOUR': hour, 'C_VEHS': v_number, 'C_CONF': road,
         'C_WTHR': weather, 'C_TRAF': traffic, 'V_YEAR': v_year, 'P_AGE': age, 'C_RCFG':final_prediction})

    def convert_prediction(prediction):
        conveter = {

            0:"Non-Intersection",
            1:"At an intersection of at least two public roadways",
            2:"Intersection with parking lot entrance/exit, private driveway or laneway",
            3:"Railroad level crossing",
            4:"Bridge, overpass, viaduct",
            5:"Tunnel or underpass",
            6:"Passing or climbing lane",
            7:"Ramp",
            8:"Traffic circle",
            9:"Express lane of a freeway system",
            10:"Collector lane of a freeway system",
            11:"Transfer lane of a freeway system"



        }
        return conveter.get(prediction, "Sorry!!! Wrong Prediction")
    Pretty_prediction = convert_prediction(final_prediction)

    print(Pretty_prediction)

    return render_template('submitted.html' , show_data = Pretty_prediction )





app.run(debug=True)
