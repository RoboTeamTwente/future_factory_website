# Contact
The website makes use of contact forms. With the help of these forms people can send directly a message to either the
entire Future Factory, or just individual teams.

When a message gets send from the home page, it is sent to all the teams, whereas when a message is send through a team 
page it will only end up at that specific team.

In order to clean all the data and make it safe for processing we use the `ContactForm` object, using a Django 
[Form](https://docs.djangoproject.com/en/4.1/topics/forms/).

The `SendMessage` view, located in `main_site/views.py` takes care of actually sending the email to the correct
destination. At first the form is populated with the data and it is checked. If safe, an email is created and send.
A message indicating that the mail was successfully send will be shown to the user.

In case the form contains any error, the user will be made aware of these errors. Asking them to fix it.