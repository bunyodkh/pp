# self.fields['full_name'].validators.extend([
#                 MinLengthValidator(2, _('Full name must be at least 2 characters long.')),
#                 MaxLengthValidator(100, _('Full name must be at most 100 characters long.')),
#                 RegexValidator(regex=r'^[^\W\d_]+(?:\s[^\W\d_]+)*$', message=_('Username can only contain letters and spaces.')),
                
#         ])
#         self.fields['full_name'].widget.attrs.pop('required', None)

#         self.fields['organization'].validators.extend([
#             MinLengthValidator(2, _('Organization name must be at least 2 characters long.')),
#             MaxLengthValidator(100, _('Organization name must be at most 100 characters long.')),
#             RegexValidator(regex=r'^[^\W\d_]+(?:\s[^\W\d_]+)*$', message=_('Organization name can only contain letters and spaces.')),
#         ])
#         self.fields['organization'].widget.attrs.pop('required', None)

#         self.fields['position'].validators.extend([
#             MinLengthValidator(2, _('Position must be at least 2 characters long.')),
#             MaxLengthValidator(100, _('Position must be at most 100 characters long.')),
#             RegexValidator(regex=r'^[^\W\d_]+(?:\s[^\W\d_]+)*$', message=_('Position can only contain letters and spaces.')),
#         ])
#         self.fields['position'].widget.attrs.pop('required', None)

#         self.fields['tg'].validators.extend([
#             MinLengthValidator(2, _('Telegram username must be at least 2 characters long.')),
#             MaxLengthValidator(100, _('Telegram username must be at most 100 characters long.')),
#             RegexValidator(regex=r'^[^\W\d_]+(?:\s[^\W\d_]+)*$', message=_('Telegram username can only contain letters and spaces.')),
#         ])
#         self.fields['tg'].widget.attrs.pop('required', None)

#         self.fields['phone'].validators.extend([
#             MinLengthValidator(2, _('Phone number must be at least 2 characters long.')),
#             MaxLengthValidator(15, _('Phone number must be at most 15 characters long.')),
#             RegexValidator(regex=r'^\+?[0-9\s\-()]+$', message=_('Enter a valid phone number.')),
#         ])
#         self.fields['phone'].widget.attrs.pop('required', None)

#         self.fields['linkedin_profile'].validators.extend([
#             MinLengthValidator(2, _('LinkedIn profile URL must be at least 2 characters long.')),
#             MaxLengthValidator(100, _('LinkedIn profile URL must be at most 100 characters long.')),
#             RegexValidator(regex=r'^[^\W\d_]+(?:\s[^\W\d_]+)*$', message=_('LinkedIn profile URL can only contain letters and spaces.')),
#         ])  
#         self.fields['linkedin_profile'].widget.attrs.pop('required', None)

#         self.fields['bio'].validators.extend([
#             MinLengthValidator(2, _('Bio must be at least 2 characters long.')),
#             MaxLengthValidator(500, _('Bio must be at most 500 characters long.')),
#         ])
#         self.fields['bio'].widget.attrs.pop('required', None)