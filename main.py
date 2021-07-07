import requests
# import matplotlib
# import matplotlib.pyplot as plt
import pandas as pd
from sqlalchemy import create_engine
import os


# Retreives the genre based on the user's input
def genre_input():
    return input("Enter a genre: ")


# Retreives the number of anime shows based on the user's input
def page_input():
    return input("How many animes would you like displayed? ")


# Defines the query as a multi-line string to be used with GraphQL
def make_query():
    query = '''
    query ($id: Int, $page: Int, $perPage: Int,
    $genre: String, $popularity: Int) {
        Page (page: $page, perPage: $perPage) {
            pageInfo {
                total
                currentPage
                lastPage
                hasNextPage
                perPage
            }
            media (id: $id, genre: $genre, popularity: $popularity) {
                id
                title {
                    romaji
                }
                popularity
            }
        }
    }
    '''
    return query


# Defines our query variables and values that will be used in the query request
def make_variables():
    variables = {
        'genre': genre_input(),
        'page': 1,
        'perPage': page_input()
    }
    return variables


# Takes the response from the query and filters the data to make it usable
def handle_response(query, variables):
    url = 'https://graphql.anilist.co'
    # Make the HTTP Api request
    response = requests.post(
        url, json={'query': query, 'variables': variables})
    # testing filtering
    response = response.json()
    response = response['data']
    response = response['Page']
    response = response['media']
    return response


# Organizes the data into two columns, name and popularity
def make_colummns(df, data):
    dataSecondCol = []
    for i in data:
        dataSecondCol.append(i['popularity'])
    df.insert(1, "Popularity", dataSecondCol, True)
    return df


def create_dataframe(data):
    # test dataframe creation
    col_names = ['Anime Name']
    dataFirstCol = []
    for i in data:
        string = str(i['title'])
        dataFirstCol.append(string[12:-2])
    df = pd.DataFrame(dataFirstCol, columns=col_names)
    df = make_colummns(df, data)
    return df


def check_existing():
    # create the database
    os.system('mysql -u root -pcodio -e "CREATE DATABASE IF NOT EXISTS ' +
              'genreList' + '; "')
    # load
    os.system("mysql -u root -pcodio genreList < genreList.sql")
    df = pd.read_sql_table('genreList', con=create_engine('mysql:' +
                                                          '//root:co' +
                                                          'dio@loc' +
                                                          'alhost/' +
                                                          'genreList'))


def data_to_sql(df):
    # test uploading the dataframe to SQL
    engine = create_engine('mysql://root:codio@localhost/genreList')
    df.to_sql('genreList', con=engine, if_exists='replace', index=False)


# Runs the program
def main():
    variables = make_variables()
    query = make_query()
    data = handle_response(query, variables)
    print(data)
    check_existing()
    df = create_dataframe(data)
    data_to_sql(df)
    os.system("mysqldump -u root -pcodio genreList > genreList.sql")


if __name__ == "__main__":
    main()

# DOCUMENTATION

# https://anilist.gitbook.io/anilist-apiv2-docs/overview/graphql/pagination

# https://anilist.github.io/ApiV2-GraphQL-Docs/
