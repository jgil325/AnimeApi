# imports
import requests

# Input function 
def user_input():
    pass


# Here we define our query as a multi-line string
query = '''
query ($id: Int, $page: Int, $perPage: Int, $genre: String) {
    Page (page: $page, perPage: $perPage) {
        pageInfo {
            total
            currentPage
            lastPage
            hasNextPage
            perPage
        }
        media (id: $id, genre: $genre) {
            id
            title {
                romaji
                native
            }
        }
    }
}
'''

# Define our query variables and values that will be used in the query request
variables = {
    'genre': 'Fantasy',
    'page': 1,
    'perPage': 5
}

url = 'https://graphql.anilist.co'

# Make the HTTP Api request
response = requests.post(url, json={'query': query, 'variables': variables})
print(response.json())

# https://anilist.gitbook.io/anilist-apiv2-docs/overview/graphql/pagination

# https://anilist.github.io/ApiV2-GraphQL-Docs/