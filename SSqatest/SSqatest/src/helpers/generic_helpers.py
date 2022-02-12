

import random
import string

def generate_random_email_and_password(domain_name=None,email_prefix=None):

    if not domain_name:
        domain_name='supersqa.com'

    if not email_prefix:
        email_prefix ='testuser'

    random_email_char_len= 10
    rand_email_chars=''.join(random.choices(string.ascii_lowercase,k=random_email_char_len))

    random_email=email_prefix + rand_email_chars + '@' + domain_name

    random_pass_char_len=20
    random_password =''.join(random.choices(string.ascii_letters,k=random_pass_char_len))

    random_email_and_pass={'email':random_email,'password':random_password}

    return random_email_and_pass


