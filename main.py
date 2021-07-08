import requests
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
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


# Creates bar graph based on the data retreived
def create_bargraph(data, genre):
    # Lists for Anime titles and Popularity count
    dic = {}
    # Loops to adds Anime titles and popularity amount to the dictionary, dic
    for i in data:
        string = str(i['title'])
        dic[f'{string[12:-2]}'] = i['popularity']
    # Sort dic by value
    data_list = sorted(dic.items(), key=lambda x: x[1])
    # Convert list to dic
    sortdic = dict(data_list)
    # Convert keys and values as a list
    dataFirstCol = list(sortdic.keys())
    dataSecondCol = list(sortdic.values())
    # Adds color to graph bars
    New_Colors = ['green', 'blue', 'purple', 'brown', 'teal']
    # Adds spaces between the bars
    bar_width = 0.4
    # Figure Size
    fig, ax = plt.subplots()
    plt.subplots_adjust(left=.22, bottom=.124, right=.89,
                        top=.843, wspace=.198, hspace=.202)
    # Horizontal Bar Plot
    ax.barh(dataFirstCol, dataSecondCol, bar_width, color=New_Colors)
    # Remove axes splines
    for s in ['top', 'bottom', 'left', 'right']:
        ax.spines[s].set_visible(False)
    # Remove x, y Ticks
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')
    # Add x, y gridlines
    ax.grid(b=True, color='grey',
            linestyle='-.', linewidth=0.5,
            alpha=0.2)
    # Add annotation to bars
    for i in ax.patches:
        plt.text(i.get_width()+0.2, i.get_y()+0.5,
                 str(round((i.get_width()), 2)),
                 fontsize=10, fontweight='bold',
                 color='grey')
    # Add Plot Title
    ax.set_title(f'Top {len(dataFirstCol)}' +
                 f' {(genre[0:1].upper() + genre[1:len(genre)])} Animes',
                 loc='left', fontsize=14)
    # Add Plot x-axis title
    plt.xlabel('Popularity Amount', fontsize=14)
    # Add Plot y-axis title
    plt.ylabel('Anime Titles', fontsize=14)
    # Show Plot
    plt.ion()
    user_input = ""
    while(user_input != "exit"):
      plt.show()
      user_input = input("Enter [exit] to terminate program: ")
    



# Runs the program
def main():
    variables = make_variables()
    genre = variables['genre']
    query = make_query()
    data = handle_response(query, variables)
    check_existing()
    df = create_dataframe(data)
    data_to_sql(df)
    os.system("mysqldump -u root -pcodio genreList > genreList.sql")
    create_bargraph(data, genre)
    #     print(data)


if __name__ == "__main__":
    main()

# DOCUMENTATION

# https://anilist.gitbook.io/anilist-apiv2-docs/overview/graphql/pagination

# https://anilist.github.io/ApiV2-GraphQL-Docs/
