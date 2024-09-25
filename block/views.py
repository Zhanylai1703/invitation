from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Invitation, Wish


def invitation_view(request, token):
    invitation = get_object_or_404(Invitation, token=token)

    full_invitation = invitation.first_invitation
    if invitation.second_invitation:
        full_invitation += f" & {invitation.second_invitation}"

    if request.method == 'POST':
        response = request.POST.get('response')
        name = request.POST.get('name')  # Получаем имя пользователя
        wish_text = request.POST.get('wish')  # Получаем текст пожелания

        # Обновляем статус приглашения
        if response == 'accept':
            invitation.status = 'accepted'
        elif response == 'decline':
            invitation.status = 'declined'

        # Сохраняем пожелание в модели Wish, если введены имя и текст пожелания
        if name and wish_text:
            Wish.objects.create(name=name, wish=wish_text)

        invitation.save()
        return JsonResponse({"message": "Спасибо за ваш ответ!"})

    return render(
        request,
        'page_source.html',
        {'invitation': invitation, 'full_invitation': full_invitation, 'token': token}
    )


def random_wishes_view(request):
    wishes = Wish.objects.all()  # Берем все записи из модели Wish
    context = {'wishes': wishes}
    return render(request, 'random_wishes.html', context)
