from django import template

register = template.Library()


def get_companion(user, chat):
    for u in chat.members.all():
        if u != user:
            return u
    return None