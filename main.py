# imports
import requests

# Input function 
def user_input():
    pass


# Here we define our query as a multi-line string
query = '''
query ($id: Int, $page: Int, $perPage: Int, $search: String) {
    Page (page: $page, perPage: $perPage) {
        pageInfo {
            total
            currentPage
            lastPage
            hasNextPage
            perPage
        }
        media (id: $id, search: $search) {
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
    'search': 'Fate/Zero'
}

url = 'https://graphql.anilist.co'

# Make the HTTP Api request
response = requests.post(url, json={'query': query, 'variables': variables})
print(response.json())

# https://anilist.gitbook.io/anilist-apiv2-docs/overview/graphql/pagination