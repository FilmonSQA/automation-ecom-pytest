

import pytest
from demostore_automation.src.pages.HomePage import HomePage
from demostore_automation.src.pages.Header import Header
from demostore_automation.src.pages.CartPage import CartPage


@pytest.mark.usefixtures("init_driver")
class TestCartPageInvalidCouponSmoke:

    @pytest.mark.estcf2
    @pytest.mark.abc123
    def test_verify_invalid_coupon(self):

        # go to home add add item to cart
        home_page = HomePage(self._driver)

        # go to home page
        home_page.go_to_home_page()
        home_page.click_first_add_to_cart_button()


        # make sure the cart is updated before going to cart
        header = Header(self.driver)
        header.wait_until_cart_item_count(1)


        # go to car
        header.click_on_cart_on_right_header()


        # verify there are items in the cart
        cart_page = CartPage(self.driver)
        product_names = cart_page.get_all_product_names_in_cart()
        assert len(product_names) ==1, f"Expected 1 product in caart but found {len(product_names)}"


        # apply invalid coupon
        cart_page.apply_coupon("q438473ejdskjf")
        displayed_msg = cart_page.get_error_message()

        expected_msg = 'Coupon "q438473ejdskjf" does not exist!'
        if displayed_msg != expected_msg:
            raise Exception(f"Test=invalid coupon. Displayed error message does not match expected.")
        else:
            print("PASS")
        # verify the invalid coupon