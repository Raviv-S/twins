def act_star(sentence):
    if len(sentence.split()) == 3:
        return 'Fight!'
    else:
        return 'Bargain'


def act_squid(sentence):
    if 'squid' in sentence.lower().split():
        return 'Fight!'
    elif 'squid'[::-1] in sentence.lower().split():
        return 'Bargain'
    else:
        return 'Run!'


def act_sponge(sentence):
    unique_words = set(sentence.lower().split())
    if len(unique_words) < len(sentence.split()):
        return 'Fight!'
    else:
        return 'Run!'


def act_else(sentence):
    if 'peace' in sentence.lower().split():
        return 'Bargain'
    else:
        return 'Run!'


def main():
    print(act_star('hows it going? brah'))
    print(act_squid('diuqs squid'))
    print(act_sponge('bla foo blip Bla'))
    print(act_else('peace a'))


if __name__ == '__main__':
    main()