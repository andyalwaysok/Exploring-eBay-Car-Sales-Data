import pandas as pd
import mysql.connector

import explore_data_module as edm
import cleaning_data_module as cdm

general_dict = {'minimum_price': 5000,
                'maximum_price': 7000000,
                'min_reg_year': 1910}

directory = 'C:\\Personal Projects\\Dataquest\\Python Project\\Exploring eBay Car Sales Data\\'

autos = pd.read_csv(directory + 'autos.csv', encoding = 'ISO-8859-1')

edm.explore_dataset(autos)

autos = cdm.cleaning_dataset(autos, general_dict)

edm.explore_registraion_year(autos)

autos = cdm.removing_outlier_for_registration_year(autos, general_dict)

edm.explore_car_brand_and_mileage(autos)