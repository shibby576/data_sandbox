
#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#number of data points
total_data_points = len(enron_data)
print (total_data_points)

#number of features per person
print (len(enron_data.values()[1]))

#count then number of "persons of interest" in the data set
counter =0
for i in enron_data:
    if enron_data[i]['poi']==1:
        counter +=1

print "Number of POIs in data set: ", str(counter)

#get the total number of POIs from poi names file
poi_names = open("/Users/jonathan/Documents/GitHub/data_sandbox/Udacity_ML_Course/final_project/poi_names.txt", "r")
counter_1 = 0
for i in poi_names:
    counter_1 +=1
print "Total POIs: ", str(counter_1)

#get an individuals stock value

print("James Prentice total stock value " + str(enron_data["PRENTICE JAMES"]["total_stock_value"]))
#print(enron_data.values())

#number of messages fromWesley Colwell
print "Messages from Wesley Colwell TO POIs " + str(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])

#print(enron_data)
#value of stock options exercised by Jeffrey K Skilling
print "Value of stock options exercised by Jeffrey K Skilling " + str(enron_data['SKILLING JEFFREY K']['exercised_stock_options'])

#total paymets for top enron employees
print "Total payments Jeffrey K Skilling " + str(enron_data['SKILLING JEFFREY K']['total_payments'])
print "Total payments LAY KENNETH L " + str(enron_data['LAY KENNETH L']['total_payments'])
print "Total payments FASTOW ANDREW S " + str(enron_data['FASTOW ANDREW S']['total_payments'])

#number of people with a salary
counter =0
for i in enron_data:
    if enron_data[i]['salary']!= 'NaN':
        counter +=1

print "Number of missing salaries: ", str(counter)

#number of people with an email address
counter =0
for i in enron_data:
    if enron_data[i]['email_address']!= 'NaN':
        counter +=1

print "Number of missing email addresses: ", str(counter)

#how many people have NaN for total payments?
nan_counter =0.0
for i in enron_data:
    if enron_data[i]['total_payments']== 'NaN':
        nan_counter +=1

print "Number of missing total payments: ", str(nan_counter)

#percent of people with missing total payments
perct = nan_counter/total_data_points
print('% of missing total payments ' + str(perct))