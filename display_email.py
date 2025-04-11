import pytest

def display_email_address(email):
    if "@" not in email:
        return "Invalid email address!"
    if "." not in email:
        return "Invalid email address!"
    print(f'Your email is : {email}')



def test_display_email_address():
    assert display_email_address('Hj4hD@example.com') == None
    assert display_email_address('s6M1axample.com') == 'Invalid email address!'
    with pytest.raises(TypeError):
        display_email_address(123)

if __name__ == "__main__":
    test_display_email_address()




