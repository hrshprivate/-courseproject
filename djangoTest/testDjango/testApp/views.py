
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect
from django.utils.encoding import smart_str, uri_to_iri
from django.utils.text import slugify

from .models import Task, Example, UserProfile, Room, Message
from .forms import TaskForm, ExampleForm, UserProfileForm, PasswordChangingForm, MessageForm, RoomForm, UserEditForm
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.views.generic.base import View
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = 'login'


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'testApp/index.html',
                      {'title': 'main page of site'})
    else:
        tasks = Task.objects.order_by('-id')
        examples = Example.objects.all()
        userok = request.user
        test = Example.objects.filter(Name=userok.first_name + " " + userok.last_name)
        if not UserProfile.objects.filter(user=request.user):
            example = UserProfile.objects.create(user=request.user)
        else:
            example = UserProfile.objects.get(user=request.user)
        return render(request, 'testApp/index.html', {'title': 'main page of site', 'tasks': tasks, 'examples': examples, 'example': example, 'test': test})


def about(request):
    return render(request, 'testApp/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        user = request.user
        if user.first_name and user.last_name:
            if not Example.objects.filter(Name=user.first_name + " " + user.last_name):
                    examples = Example.objects.create(Name=user.first_name + " " + user.last_name)
            else:
                    examples = Example.objects.get(Name=user.first_name + " " + user.last_name)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.name = "Ваша работа пока без оценки!"
            instance.example = examples
            instance.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
    form = TaskForm()
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'testApp/create.html', context)


def update(request, id):
    tasks = Task.objects.get(id=id)
    form = TaskForm(request.POST or None, instance=tasks)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'testApp/update.html', {'form': form, 'tasks': tasks})


class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = 'login'

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "testApp/register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "testApp/login.html"

    # В случае успеха перенаправим на главную.
    success_url = "/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect("/")


def mono(request, item_id):
    tasks = UserProfile.objects.get(id=item_id)
    return render(request, 'testApp/detail.html', {'tasks': tasks})


def delete_task(request, task_id):
    pro = Task.objects.get(id=task_id)
    userok = Example.objects.filter(Name=request.user.first_name + " " + request.user.last_name)
    test = Task.objects.filter(example__in=userok)
    if pro:
        if test.count() == 1:
            userok.delete()
            return redirect('home')
        else:
            pro.delete()
            return redirect('home')


def profile(request):
    qun = UserProfile.objects.all()
    tasks = UserProfile.objects.get(user=request.user)
    state = request.POST.get('Date')
    user_form = UserEditForm(request.POST, instance=request.user)
    form = UserProfileForm(request.POST or None, request.FILES or None, instance=tasks)
    if form.is_valid() and user_form.is_valid():
        user = form.save(commit=False)
        user.birth_date = state
        user.data = user.birth_date
        instance = user_form.save()
        instance.save()
        user.save()
        return redirect('profile')
    return render(request, 'testApp/profile.html', {'form': form, 'tasks': tasks, 'qun': qun, 'state': state, 'user_form': user_form})


def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'testApp/room.html', {
        'username': username,
        'room': room,
        'room_details': room_details,
    })


def chattwo(request):
    rooms = Room.objects.filter(author=request.user)
    another = Room.objects.filter(author=None)
    users = User.objects.all()
    return render(request, 'testApp/chat.html', {'rooms': rooms, 'users': users, 'another': another})


def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']
    author = request.POST.getlist('author')
    if Room.objects.filter(name=room).exists():
        if Room.objects.filter(person=request.user).exists():
            if not author or author:
                new_room = Room.objects.get(name=room, person=request.user)
                new_room.author.add(*author)
                new_room.save()
                return redirect('/' + room + '/?username=' + username)
        else:
            return redirect('chattwo')
    else:
        if not author:
                if request.user.is_superuser:
                    new_room = Room.objects.create(name=room, person=request.user)
                    new_room.author.add(*author)
                    new_room.save()
                    return redirect('/'+room+'/?username='+username)
                else:
                    return redirect('chattwo')
        if author:
            new_room = Room.objects.create(name=room, person=request.user)
            new_room.author.add(*author)
            django = Room.objects.all()
            userok = request.user
            for retweet in django:
                if retweet == userok:
                    new_room.save()
                else:
                    new_room.author.add(userok)
                    new_room.save()
            return redirect('/'+room+'/?username='+username, {'userok': userok})


def getcheckview(request):
    room = request.GET['room_name']
    username = request.GET['username']
    if Room.objects.filter(name=room).exists():
        return redirect('/' + room + '/?username=' + username)
    else:
        return redirect('chattwo')


def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']
    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')


def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})


def DeleteChatUser(request, chat_id):
        pro = Room.objects.get(id=chat_id)
        userok = request.user
        test = pro.author.filter(author__isnull=False)
        if pro:
            if test.count() == 1:
                pro.delete()
                return redirect('chattwo')
            else:
                pro.author.remove(userok)
                return redirect('chattwo')