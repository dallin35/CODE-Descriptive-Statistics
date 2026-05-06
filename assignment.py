import pandas as pd
import matplotlib.pyplot as plt

filename = "big-mac-full-index.csv"
df = pd.read_csv(filename)

def get_describe_country(country_code):
    query = f"iso_a3 == '{country_code.upper()}'"
    country_df = df.query(query).copy()
    return country_df['dollar_price'].describe()


def get_country_groupby_year(country_code):
    query = f"iso_a3 == '{country_code.upper()}'"
    country_df = df.query(query).copy()
    country_df['year'] = pd.to_datetime(country_df['date']).dt.year
    return country_df.groupby('year')['dollar_price'].describe()

if __name__ == "__main__":
    print("\nAnnual Report for USA")
    print(get_country_group_by_year('USA'))
   
    usa_stats = get_describe_country('USA')
    print("Statistics for USA")
    print(usa_stats)
   
    countries = ['MEX', 'ARG', 'USA', 'POL', 'CHN']
    five_countries_df = df[df['iso_a3'].isin(countries)].copy()
    print(f"Rows found: {len(five_countries_df)}") 
    
    five_countries_df.boxplot(column='dollar_price', by='iso_a3')
    plt.show()
