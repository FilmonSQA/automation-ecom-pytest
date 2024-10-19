
import pytest

from demostore_automation.src.pages.HomePage import HomePage
from demostore_automation.src.pages.Header import Header

@pytest.mark.usefixtures("init_driver")
class TestRowColumn:
    """
    Test class to verify there are 5 columns and 4 rows on the home page
    """

    @pytest.fixture(scope='class')
    def setup(self, request):
        request.cls.homepage = HomePage(self.driver)
        request.cls.header = Header(self.driver)
        self.homepage.go_to_home_page()
        yield

    @pytest.mark.estcf18
    def test_five_columns_and_four_rows(self):
        """
        Test to verify that there are five columns and four rows on the home page.
        """

        # Get all the product elements on the homepage
        all_product_elements = self.homepage.get_all_products_elements()

        #Expected number of columns and rows
        expected_columns = 5
        expected_rows = 4
        expected_total_products = expected_columns * expected_rows

        # Verify the total number of products equals 20 (5 columns * 4 rows)
        num_of_products = len(all_product_elements)
        assert num_of_products == expected_total_products, \
            f"Expected {expected_total_products} products, but found {num_of_products}."
        
        print(f"Test passed with {expected_rows} rows and {expected_columns} columns.")