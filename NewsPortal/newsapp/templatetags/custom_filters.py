from django import template

register = template.Library()

STOP_LIST = ['растан', 'эрдоган', 'муссолини', 'джорданом', 'вином', 'фань', 'уорстлер',
             'пола',]

@register.filter()
def censor(text):
    censored_list = []
    for i in text.split():
        if i.isdigit() is not True:
            if i.lower() in STOP_LIST:
                i = i[0] + '*'*(len(i) - 1)
                censored_list.append(i)
            else:
                censored_list.append(i)
        else:
     #       raise ValueError   если надо вынуждено вызвать исключение
            i = '<Ошибка>'
            censored_list.append(i)
    return ' '.join(censored_list)