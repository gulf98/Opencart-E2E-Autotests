from mimesis import Person as PersonalDataGenerator

from infrastructure.types import Person

personal_data_generator = PersonalDataGenerator()


class PersonGenerator:
    @staticmethod
    def create_person(
            firstname=None,
            lastname=None,
            email=None,
            telephone=None,
            password=None,
            password_confirm=None
    ):
        _firstname = firstname if firstname is not None else personal_data_generator.first_name()
        _lastname = lastname if lastname is not None else personal_data_generator.last_name()
        _email = email if email is not None else personal_data_generator.email()
        _telephone = telephone if telephone is not None else personal_data_generator.telephone()
        _password = password if password is not None else personal_data_generator.password()
        _password_confirm = password_confirm if password_confirm is not None else _password
        return Person(
            _firstname,
            _lastname,
            _email,
            _telephone,
            _password,
            _password_confirm
        )

    @staticmethod
    def create_correct_random_person():
        return PersonGenerator.create_person()

    @staticmethod
    def create_person_with_empty_firstname():
        return PersonGenerator.create_person(firstname="")

    @staticmethod
    def create_person_with_empty_lastname():
        return PersonGenerator.create_person(lastname="")

    @staticmethod
    def create_person_with_empty_email():
        return PersonGenerator.create_person(email="")

    @staticmethod
    def create_person_with_empty_telephone():
        return PersonGenerator.create_person(telephone="")

    @staticmethod
    def create_person_with_empty_password():
        return PersonGenerator.create_person(password="", password_confirm="password2")

    @staticmethod
    def create_person_with_empty_password_confirm():
        return PersonGenerator.create_person(password_confirm="")

    @staticmethod
    def create_person_with_different_passwords():
        return PersonGenerator.create_person(password="password1", password_confirm="password2")
