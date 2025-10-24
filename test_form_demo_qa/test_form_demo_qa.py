from selene import browser, be, have, command
import os


def test_filling_out_and_submitting_the_form(open_browser):
    browser.open("/automation-practice-form")

    browser.element('input[id=firstName]').type('Ivan') # для id селектор ищется так
    browser.element('[id=lastName]').type('Ivanov') # а можно сократить
    browser.element('#userEmail').type('ivanivanov@mail.ru') # еще больше сократить
    browser.element('[for=gender-radio-1]').click()
    browser.element('#userNumber').type('9997777172')

    browser.element('#dateOfBirthInput').click()
    browser.element("select[class=react-datepicker__month-select]").click().element("option[value='6']").click()
    browser.element("select[class=react-datepicker__year-select]").click().element("option[value='1991']").click()
    browser.element("[aria-label='Choose Friday, July 26th, 1991']").click()

    browser.element('#subjectsInput').type('Test')
    browser.element('#submit').perform(command.js.scroll_into_view)
    browser.element('[for=hobbies-checkbox-1]').click()

    browser.element('#uploadPicture').send_keys(os.path.abspath('../picture.png'))
    browser.element('#currentAddress').type('Москва, ул Ленина, 1-5-61')

    browser.element('#state').click().element('#react-select-3-option-1').click()
    browser.element('#city').click().element('#react-select-4-option-1').click()

    browser.element('#submit').click()

    browser.element('.modal-content').should(be.existing)
    browser.all('.table-dark tbody tr').should(have.size(10))
    # browser.element('.modal-content').element('table').all('tr').all('td').even.should(
    #     have.exact_texts(
    #         'Masha Maria',
    #         'mama@mail.ru',
    #         'Female',
    #         '7987654543',
    #         '12 July,2022',
    #         'Hindi',
    #         'Sports',
    #         'picture.jpg',
    #         'Address',
    #         'NCR Delhi',
    #     )
    # )











