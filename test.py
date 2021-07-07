import unittest
from main import (
  genre_input,
  page_input,
  make_query,
  make_variables,
  handle_response,
  make_colummns,
  create_dataframe,
  check_existing,
  data_to_sql,
  main
)


class test(unittest.TestCase):
    def test_genre_input(self):
        self.assertIsNotNone(genre_input)
        
    def test_page_input(self):
        self.assertIsNotNone(page_input)
        
    def test_make_query(self):
        self.assertIsNotNone(make_query)
        
    def test_make_variables(self):
        self.assertIsNotNone(make_variables)
        
    def test_handle_response(self):
        self.assertIsNotNone(handle_response)
        
    def test_make_columns(self):
        self.assertIsNotNone(make_colummns)
        
    def test_create_dataframe(self):
        self.assertIsNotNone(create_dataframe)
        
    def test_check_existing(self):
        self.assertIsNotNone(check_existing)
        
    def test_data_to_sql(self):
        self.assertIsNotNone(data_to_sql)
        
    def test_main(self):
        self.assertIsNotNone(main)
        
        
# if __name__ == "__main__":
#     unittest.main()
    