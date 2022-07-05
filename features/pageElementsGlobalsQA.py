
class PageElementsGlobalsQA:
    url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"

    #click_bank_manager
    bank_manager_btn = "//button[normalize-space()='Bank Manager Login']"
    add_customer_btn = "//button[normalize-space()='Add Customer']"

    #add_customer
    cust_input_name = "//input[@placeholder='First Name']"
    cust_input_lname = "//input[@placeholder='Last Name']"
    cust_input_postal = "//input[@placeholder='Post Code']"
    submit_customer = "//button[@type='submit']"


    #search_customer
    customers = "//button[@ng-click='showCust()']"
    search_field = "//input[@placeholder='Search Customer']"

    #delete customer
    delete_btn = "//button[@ng-click='deleteCust(cust)']"






