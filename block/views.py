from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Invitation


def invitation_view(request, token):
    invitation = get_object_or_404(Invitation, token=token)

    full_invitation = invitation.first_invitation
    if invitation.second_invitation:
        full_invitation += f" & {invitation.second_invitation}"

    if request.method == 'POST':
        response = request.POST.get('response')
        wish = request.POST.get('wish')

        if response == 'accept':
            invitation.status = 'accepted'
        elif response == 'decline':
            invitation.status = 'declined'

        if wish:
            invitation.wish = wish

        invitation.save()
        return JsonResponse({"message": "Спасибо за ваш ответ!"})

    return render(
        request,
        'page_source.html',
        {'invitation': invitation, 'full_invitation': full_invitation, 'token': token}
    )
