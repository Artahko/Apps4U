from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.exceptions import ImmediateHttpResponse
from django.shortcuts import render

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):

    def populate_user(self, request, sociallogin, data):
        user = super().populate_user(request, sociallogin, data)

        # Logic for checking if user is an UCU student
        email = sociallogin.user.email

        # CHANGE TO pn@ucu.edu.ua WHEN PRODUCT IS READY
        if not email.endswith('@ucu.edu.ua'):
            raise ImmediateHttpResponse(render(request, 'users/restricted_access.html'))

        # This Saves Google user's data automatically
        user.first_name = data.get("given_name", "")
        user.last_name = data.get("family_name", "")
        user.email = data.get("email", "")

        return user
