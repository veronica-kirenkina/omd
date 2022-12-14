from random import choice


incident = ['пожар', 'потоп', 'охотник']
duck_with_umbrella = {
        'пожар': 'промокла бы, когда пожар тушили',
        'потоп': 'не смогла бы уплыть из этого несчастного бара',
        'охотник': 'охотник бы заметил и застрелил. '
        'А так он подумал, что это просто зонтик по улице летает'
    }
duck_without_umbrella = {
        'пожар': 'его тушили и струей воды утку-маляра окатили. '
        'Бедная утка вся промокла, вся продрогла',
        'потоп': 'бы не пришлось грести своими двумя',
        'охотник': 'пришлось убегать со всех ног. '
        'Могла бы за зонтиком спрятаться, он бы и не заметил'
    }


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    whats_happend = choice(incident)
    print(f'Утка-маляр взяла зонтик, и пошла в бар. А там {whats_happend}!\n'
          f'Хорошо, что зонтик взяла, а то {duck_with_umbrella[whats_happend]}.')


def step2_no_umbrella():
    whats_happend = choice(incident)
    print(f'Утка-маляр не взяла зонтик, и пошла в бар. А там {whats_happend}!\n'
          f'Как жаль, что зонтик не взяла, а то {duck_without_umbrella[whats_happend]}.')


if __name__ == '__main__':
    step1()
