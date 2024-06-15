# Library_Project
dataset from kaggle 
https://www.kaggle.com/datasets/datasf/sf-library-usage-data/data

**Context** :

San Francisco's Integrated Library System (ILS) is composed of bibliographic records including inventoried items, patron records, and circulation data. The data is used in the daily operation of the library, including circulation, online public catalog, cataloging, acquisitions, collection development, processing, and serials control. This dataset represents the usage of inventoried items by patrons (~420K records).

**Content** :

The dataset includes approximately 420,000 records, with each record representing an anonymized library patron. Individual columns include statistics on the type code and age of the patron, the year the patron registered (only since 2003), and how heavily the patron has been utilizing the library system (in terms of number of checkouts) since first registering.

**Acknowledgements** :

The data is provided by [SF Public Library](https://sfpl.org/) via the [San Francisco Open Data Portal](https://data.sfgov.org/Culture-and-Recreation/Library-Usage/qzz6-2jup/about_data), under the PDDL 1.0 ODC Public Domain Dedication and Licence ([PDDL](https://opendatacommons.org/licenses/pddl/1-0/)).

#### Feature Description

* **Patron Type Code** : 
    * Data Type : Numeric
    * Definition : Type of patron record (adult, teen, child, senior, etc.) Some blank.	
* **Patron Type Definition** : 
    * Data Type :Text	
    * Definition : Description of patron (adult, teen, child, senior, etc.)	
* **Total Checkouts**	(TARGET): 
    * Data Type : Numeric	
    * Definition : Total number of items the patron has checked out from the library since the record was created.	
* **Total Renewals**  :	
    * Data Type :Numeric	
    * Definition : Total number of times the patron has renewed checked-out items.	
* **Age Range** :	
    * Data Type : Text	
    * Definition : Age ranges: 0 to 9 years, 10 to 19 years, 20 to 24 years, 25 to 34 years, 35 to 44 years, 45 to 54 years, 55 to 59 years, 60 to 64 years 65 to 74 years, 75 years and over. Some blank. 	
* **Home Library Code** :	
    * Data Type : Text	
    * Definition : Default value indicates the branch library where the patron was originally registered. Patrons can change this value if they change their preferred branch. 	
* **Home Library Definition** :	
    * Data Type : Text	
    * Definition : Description of the branch library where the patron was originally registered. 	
* **Circulation Active Year** :	
    * Data Type : Text	
    * Definition : Year the patron last checked out library materials, or last logged into the library’s subscription databases from a computer outside the library.	
* **Notice Preference Code** :	
    * Data Type :Text	
    * Definition : This field is used to indicate the patron’s preferred method of receiving library notices (email, print, phone). Some blank.	
* **Notice Preference Definition** :	
    * Data Type :Text	
    * Definition : Description of  the patron’s preferred method of receiving library notices. 	
* **Provided Email Address** :	
    * Data Type :Boolean (True/False)	
    * Definition : Indicates whether the patron provided an email address	
* **Year Patron Registered** :	
    * Data Type :Text	
    * Definition : Year patron registered with library system. No dates prior to 2003  due to system migration.	
* **Outside of County** :	
    * Data Type :Boolean (True/False)	
    * Definition : If a patron's home address is not in San Francisco, then flagged as true, otherwise false.	
* **Supervisor District** :	
    * Data Type :Numeric	
    * Definition : Based on patron address: San Francisco Supervisor District.	
    * Note : This is an automated field, please note that if "Outside of County" is true, then there will be no supervisor district. Also, if the input address was not well-formed, the supervisor district will be blank.
  
Main Goal is to identify patterns in data to best enhance Library Total Checkouts

* **Requirements** :	
pandas ,numpy ,seaborn  ,plotly ,datasist ,matplotlib.pyplot ,streamlit , sklearn ,category_encoders
