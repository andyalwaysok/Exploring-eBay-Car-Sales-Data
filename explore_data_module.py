import pandas as pd

def explore_dataset(dataset):
    print('Shape of this DataFrame is: ')
    print(dataset.shape)
    print('\n')
    print('Quick information of this DataFrame:')
    print('\n')
    print(dataset.info())
    print('\n')
    print('Describing this DataFrame:')
    print(dataset.describe(include=['O']))
    print('First few lines of this DataFrame:')
    print(dataset.head())
    print('Columns of this DataFrame:')
    print(dataset.columns)

def explore_numeric_columns(series):
    uniq_val    = series.unique().shape
    count_val   = series.value_counts().sort_index(ascending=False)
    maximum_5   = series.sort_values(ascending=False).head()
    minium_5    = series.sort_values(ascending=True).head()

    print('\n')
    print('This is the number of unique values:')
    print(uniq_val)
    print('\n')
    print('First 10 of counting values and sorting by index:')
    print(count_val)
    print('\n')
    print('This is the highest 5 sorted values:')
    print(maximum_5)
    print('\n')
    print('This is the lowest 5 sorted values:')
    print(minium_5)
    print('\n')

def exploring_datetime_columns(dataset):
    dataset['datecrawled'] = dataset['datecrawled'].str.split().str[0]
    dataset['ad_created'] = dataset['ad_created'].str.split().str[0]
    dataset['lastseen'] = dataset['lastseen'].str.split().str[0]


    # Normalizing datetime based columns
    datecrawled = (dataset['datecrawled'].value_counts(normalize=True, dropna=False).sort_index()) * 100
    adcreated = (dataset['ad_created'].value_counts(normalize=True, dropna=False).sort_index()) * 100
    lastween = (dataset['lastseen'].value_counts(normalize=True, dropna=False).sort_index()) * 100

    return dataset

def explore_registraion_year(dataset):
    print('Statistical information of registration year')
    print(dataset['registration_year'].describe())
    print('\n')
    print('10 Registration year from top')
    print(dataset['registration_year'].value_counts(ascending=False).sort_index(ascending=False).head(10))
    print('\n')
    print('10 Registration year from bottom')
    print(dataset['registration_year'].value_counts(ascending=True).sort_index().head(10))
    print('\n')
    return dataset

def explore_car_brand_and_mileage(dataset):
    normalizing_brand = dataset['brand'].value_counts(normalize=True).head(10)
    print(normalizing_brand)
    top10_brand = normalizing_brand * 100
    print(top10_brand)
    car_brand = top10_brand.index
    print(car_brand)

    brand_mean_data = {}
    for brand in car_brand:
        aggregate = dataset.loc[dataset['brand'] == brand, 'price']
        mean_val = aggregate.mean()
        brand_mean_data[brand] = round(mean_val, 2)

    kilometer_mean_data = {}
    for brand in car_brand:
        aggregate = dataset.loc[dataset['brand'] == brand, 'kilometer']
        mean_val = aggregate.mean()
        kilometer_mean_data[brand] = round(mean_val, 2)


    dict_to_series_price    = pd.Series(brand_mean_data).sort_values(ascending=False)
    dict_to_series_kilo     = pd.Series(kilometer_mean_data).sort_values(ascending=False)
    series_to_df            = pd.DataFrame(dict_to_series_price, columns=['Average Price of Each Car Brand'])


    series_to_df['Average Kilometer of Each Car Brand'] = dict_to_series_kilo
    print('\n')
    print(series_to_df)

    return dataset