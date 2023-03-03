from django import forms


class ContactForm(forms.Form):
    """
    The form that is being filled out when sending an email to our servers.
    """
    sender_mail = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    sender_mail.widget.attrs.update({'class': 'form-control form-control-lg',
                                     'aria-describedby': 'emailHelp',
                                     'placeholder': 'Enter email'})
    message.widget.attrs.update({'class': 'form-control form-control-lg',
                                 'placeholder': 'Message'})