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
    # A dictionary the alien name and act function
    alien_type = {'star': act_star, 'squid': act_squid, 'sponge': act_sponge}
    alien, sentence = input('Pick an alien: '), input('What does it says? ')
    # If the alien in the dictionary call the function with the input sentence
    try:
        print(alien_type.get(alien.lower())(sentence))
    except:
        print(act_else(sentence))


if __name__ == '__main__':
    main()