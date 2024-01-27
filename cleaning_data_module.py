import explore_data_module as edm
import datetime as dt

def remove_outlier_for_price(dataset, general_dict):
    dataset = dataset[dataset['price'].between(general_dict['minimum_price'], general_dict['maximum_price'])]
    return dataset


def cleaning_numeric_columns(dataset, general_dict):
    dataset['price']        = dataset['price'].astype(int)
    dataset['kilometer']    = dataset['kilometer'].astype(int)

    edm.explore_numeric_columns(dataset['price'])
    edm.explore_numeric_columns(dataset['kilometer'])

    # Removing Outliers
    dataset = remove_outlier_for_price(dataset, general_dict)

    return dataset


def cleaning_columns(dataset):
    new_columns = []

    # Re-naming columns
    dataset = dataset.rename({'yearOfRegistration': 'registration_year',
                              'monthOfRegistration': 'registration_month',
                              'notRepairedDamage': 'unrepaired_damage',
                              'dateCreated': 'ad_created'}, axis=1)

    for column in dataset.columns:
        column = column.lower()
        new_columns.append(column)

    dataset.columns = new_columns
    print('New column names:')
    print(dataset.columns)
    return dataset

def cleaning_dataset(dataset, general_dict):
    dataset = cleaning_columns(dataset)
    dataset = cleaning_numeric_columns(dataset, general_dict)
    edm.exploring_datetime_columns(dataset)

    return dataset

def removing_outlier_for_registration_year(dataset, general_dict):
    y = dt.datetime.now().year
    dataset = dataset[dataset['registration_year'].between(general_dict['min_reg_year'], y, inclusive='both')]
    edm.explore_registraion_year(dataset)
    return dataset