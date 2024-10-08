import os.path

from selene import browser, have

# test_data
name = "Konstantun"
lastname = "Zolotovskiy"
email = "qa@qa.qa"
gender = "Male"
number = "9876543210"
day, month, year = 1, "February", 1989
subject = "Computer Science"
hobby = "Reading"
file = os.path.abspath("../test.png")
address = "Some fake address"
state = "NCR"
city = "Noida"


def test_fill_form(browser_driver):
    browser.open("/automation-practice-form")
    browser.driver.execute_script("$('#fixedban').remove()")
    browser.driver.execute_script("$('footer').remove()")

    browser.element("#firstName").type(name)
    browser.element("#lastName").type(lastname)
    browser.element("#userEmail").type(email)
    browser.all('[name="gender"]').element_by(have.attribute('value', gender)).element('../label').click()
    browser.element("#userNumber").type(number)
    browser.element("#dateOfBirthInput").click()
    browser.element("//select[@class = 'react-datepicker__year-select']").click()
    browser.element(f"//option[text() = '{year}']").click()
    browser.element("//select[@class = 'react-datepicker__month-select']").click()
    browser.element(f"//option[text() = '{month}']").click()
    browser.element(f"//div[contains(@class, 'react-datepicker__day') and text() = '{day}']").click()
    browser.element("#subjectsInput").type(subject)
    browser.element(".subjects-auto-complete__option").click()
    browser.element(f'//label[text()="{hobby}"]').click()
    browser.element("#uploadPicture").type(file)
    browser.element("#currentAddress").type(address)
    browser.element("#state").click()
    browser.element(f"//div[contains(@id, 'react-select-3-option') and contains(text(), '{state}')]").click()
    browser.element("#city").click()
    browser.element(f"//div[contains(@id, 'react-select-4-option') and contains(text(), '{city}')]").click()

    browser.element("#submit").click()

    browser.element(f"//table//td[text() = 'Student Name']/following-sibling::td").should(have.text(f"{name} {lastname}"))
    browser.element(f"//table//td[text() = 'Student Email']/following-sibling::td").should(have.text(email))
    browser.element(f"//table//td[text() = 'Gender']/following-sibling::td").should(have.text(gender))
    browser.element(f"//table//td[text() = 'Mobile']/following-sibling::td").should(have.text(number))
    browser.element(f"//table//td[text() = 'Date of Birth']/following-sibling::td").should(have.text(f"{day} {month},{year}"))
    browser.element(f"//table//td[text() = 'Subjects']/following-sibling::td").should(have.text(subject))
    browser.element(f"//table//td[text() = 'Hobbies']/following-sibling::td").should(have.text(hobby))
    browser.element(f"//table//td[text() = 'Picture']/following-sibling::td").should(have.text(file.split(os.path.sep)[-1]))
    browser.element(f"//table//td[text() = 'Address']/following-sibling::td").should(have.text(address))
    browser.element(f"//table//td[text() = 'State and City']/following-sibling::td").should(have.text(f"{state} {city}"))
