
import time
import pytest
import logging as logger

from ssqatest.src.pages.HomePage import HomePage
from ssqatest.src.pages.Header import Header
from ssqatest.src.pages.CartPage import CartPage


@pytest.mark.usefixtures("init_driver")
class TestCartPageColumnheader:

    """
    A class for testing the column header of the cart page.
    """

    @pytest.fixture(scope='class')
    def setup(self, request):
        request.cls.homepage = HomePage(self.driver)
        request.cls.header = Header(self.driver)
        request.cls.cart = CartPage(self.driver)

        yield

    @pytest.mark.estcf17
    def test_cart_page_column_header(self, setup):
        """
        Test case for verifying the column headers on the cart page.
        Args: setup: A setup object
        """

        logger.info("Running Test: test_cart_page_column_header")
        expected_column_headers = ['Remove item', 'Thumbnail image', 'Product', 'Price', 'Quantity', 'Subtotal']

        self.homepage.go_to_home_page()
        logger.info("Navigated to home page.")
        self.homepage.click_first_add_to_cart_button()
        logger.info("Added first item to cart.")
        self.header.wait_until_cart_item_count(1)
        logger.info("Cart item count is now 1.")
        self.cart.go_to_cart_page()
        logger.info("Navigated to cart page.")

        headers = self.cart.get_cart_column_headers()
        actual_column_headers = [header.text for header in headers]

        logger.info(f"Expected Headers: {expected_column_headers}")
        logger.info(f"Actual Headers: {actual_column_headers}")

        assert expected_column_headers == actual_column_headers, (
            f"Column headers do not match! Expected: {expected_column_headers}, Got: {actual_column_headers}"
        )

        logger.info("Test passed: Column headers are as expected.")