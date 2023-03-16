class LoginPage:
    log_in = "//a[@class='nav-link text-dark']"
    email_field = "//input[@name='Email']"
    password_field = "//input[@name='Password']"
    log_in_button = "//input[@value='Sign In']"
    user_profile_name = "//a[@href='/Account/Profile']"

    def start_page(self):
        self.get("https://shop.synctoskill.com/")