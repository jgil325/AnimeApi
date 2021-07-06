# imports
import requests
# import sqlalchemy, requests, os, matplotlib
# from sqlalchemy import create_engine 
# import pandas as pd
# import matplotlib.pyplot as plt

# Input function 
def user_input():
    return input("Enter a genre: ")

  
def page_input():
    return input("How many animes would you like displayed? ")
  
# Here we define our query as a multi-line string
query = '''
query ($id: Int, $page: Int, $perPage: Int, $genre: String, $popularity: Int) {
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
                native
            }
            popularity
        }
    }
}
'''

# Define our query variables and values that will be used in the query request
variables = {
    'genre': user_input(),
    'page': 1,
    'perPage': page_input()
}

url = 'https://graphql.anilist.co'

def handle_response():
    # Make the HTTP Api request
    response = requests.post(url, json={'query': query, 'variables': variables})
    # testing filtering
    response = response.json()
    response = response['data']
    response = response['Page']
    response = response['media']
    return response

print(handle_response())

# https://anilist.gitbook.io/anilist-apiv2-docs/overview/graphql/pagination

# https://anilist.github.io/ApiV2-GraphQL-Docs/