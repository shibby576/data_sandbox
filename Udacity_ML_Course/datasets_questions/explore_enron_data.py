
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
import numpy as np

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
enron_array = np.array(enron_data)

#number of data points
print (len(enron_data))

#number of features per person
print (len(enron_data.values()[1]))

#count then number of "persons of interest" in the data set
counter =0
for i in enron_data:
    if enron_data[i]['poi']==1:
        counter +=1










print("Total number of POIs: ", str(counter))



