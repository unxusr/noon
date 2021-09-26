from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from pages import *
from time import sleep
from faker import Faker
from helpers.read_users import read_users
from helpers.read_products import read_products
from assertpy import assert_that

fake = Faker()

email = fake.email()
password = fake.password()
product = read_products()
fname = fake.first_name()
lname = fake.last_name()

print(product)

@given(u'i open noon.com')
def step_impl(context):
    # Assert that the site is open 
    assert context.browser.title ==  home_page.title 
    
@given(u'i create new user')
def step_impl(context):
    context.browser.find_element(By.XPATH, home_page.sign_in_button).click()
    context.browser.find_element(By.XPATH, home_page.sign_up_button).click()
    context.browser.find_element(By.ID, home_page.email_id).send_keys(email)
    context.browser.find_element(By.ID, home_page.password_id).send_keys(password)
    context.browser.find_element(By.ID, home_page.first_name).send_keys(fname)
    context.browser.find_element(By.ID, home_page.last_name).send_keys(lname)
    context.browser.find_element(By.XPATH, home_page.submit_sign_up).click()
    #sleep(4)


@then(u'i logged in successfully')
def step_impl(context):
    assert "Ahlan" in context.browser.find_element(By.XPATH, home_page.verify_sign_in).text

@then(u'i can search for item')
def step_impl(context):
    search = context.browser.find_element(By.XPATH, home_page.search_bar)
    search.send_keys(product)
    search.send_keys(Keys.ENTER)
    product_on_result = context.browser.find_element(
            By.XPATH, search_result_page.first_item_after_search).text
    product_on_result = product_on_result.lower()
    assert_that(product_on_result).contains(product.lower())

@then(u'i can sort the result from high to low price')
def step_impl(context):
    price_before_sort = context.browser.find_element(By.XPATH, search_result_page.first_item_price_before_sort).text
    context.browser.find_element(By.XPATH, search_result_page.sortBy_dropmenu).click()
    context.browser.find_element(By.XPATH, search_result_page.price_to_low).click()
    sleep(1)
    price_after_sort = context.browser.find_element(By.XPATH, search_result_page.first_item_price_after_sort).text
    sleep(4)
    assert float(price_after_sort) > float(price_before_sort)
    print(price_before_sort)
    print(price_after_sort)

@then(u'i can select an item to review its specs')
def step_impl(context):
    sleep(2)
    context.browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.ARROW_DOWN)
    context.browser.find_element(By.XPATH, search_result_page.first_item_price_after_sort).click()

@then(u'i can add an item to wish list by liking it')
def step_impl(context):
    context.browser.find_element(By.TAG_NAME, 'body').click()
    context.browser.find_element(By.XPATH, product_page.like_icon).click()
    context.browser.find_element(By.TAG_NAME, 'body').click()
    sleep(1)
    assert context.browser.find_element(By.XPATH, product_page.wish_list_counter).text == "1"

@then(u'i moved to the wish list')
def step_impl(context):
    context.browser.find_element(By.XPATH, product_page.wish_list_button).click()

@then(u'i can move the item to the cart')
def step_impl(context):
    context.browser.find_element(By.XPATH, cart_wish_list.move_to_cart_button).click()
    context.browser.find_element(By.TAG_NAME, 'body').send_keys(Keys.ARROW_UP)

@then(u'i click on checkout button')
def step_impl(context):
    context.browser.find_element(By.XPATH, cart.checkout_button).click()
    #sleep(3)

@then(u'i confirm my location')
def step_impl(context):
    actionChains = ActionChains(context.browser)
    actionChains.double_click(context.browser.find_element(By.ID, checkout.map_element)).perform()
    context.browser.find_element(By.TAG_NAME, 'body').click()
    sleep(2)
    context.browser.find_element(By.XPATH, checkout.confirm_location).click()

@then(u'i insert address details')
def step_impl(context):
    context.browser.find_element(By.XPATH, checkout.first_name).send_keys(fname)
    context.browser.find_element(By.XPATH, checkout.last_name).send_keys(lname)
    context.browser.find_element(By.XPATH, checkout.phone).send_keys('12345678')
    context.browser.find_element(By.XPATH, checkout.address).send_keys('Flat 10 Building 9 Name someone')


@then(u'i save the address')
def step_impl(context):
    context.browser.find_element(By.XPATH, checkout.save_address).click()
    sleep(3)

