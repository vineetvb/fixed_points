from num2word_constants import kTens, kSpecial_20


def get_tens_value(n):
    n_2digit = n % 100
    tens_val = n_2digit // 10
    return tens_val


def get_hundreds_value(n):
    n_3digit = n % 1000
    hundreds_val = n_3digit // 100
    return hundreds_val


def get_thousands_value(n):
    n_4digit = n % 10000
    thousands_val = n_4digit // 1000
    return thousands_val


def get_num_thousands(n):
    return (n - (n % 100)) // 1000


def num2word(n):
    def compose_2digit(tens_val, units_val):
        if tens_val > 1:
            if units_val > 0:
                word = " ".join([kTens[tens_val], kSpecial_20[units_val]])
            else:
                word = kTens[tens_val]
        else:
            word = kSpecial_20[tens_val * 10 + units_val]
        return word

    def compose_word(words):
        final_word = []
        if "thousand" in words:
            thousands = num2word(words["thousand"])
            final_word.append("{} thousand".format(thousands))

        if "hundred" in words:
            hundreds = words["hundred"]
            final_word.append("{} hundred".format(hundreds))

        if "ten" in words:
            tens = words["ten"]
            final_word.append(tens)

        return_word = final_word[-1]

        if len(final_word) > 1:
            if final_word[-1] != "zero":
                return_word = final_word[-2] + " and " + final_word[-1]
            else:
                return_word = final_word[-2]

        if len(final_word) == 3:
            if final_word[-1] != "zero":
                return_word = final_word[0] + " " + final_word[-2] + " and " + final_word[-1]
            else:
                return_word = final_word[0] + " and " + final_word[-2]

        return return_word

    units_val = n % 10
    tens_val = get_tens_value(n)
    hundreds_val = get_hundreds_value(n)
    num_thousands = get_num_thousands(n)

    digit_word = {"ten": compose_2digit(tens_val, units_val)}

    if hundreds_val > 0:
        digit_word["hundred"] = kSpecial_20[hundreds_val]

    if num_thousands > 0:
        digit_word["thousand"] = num_thousands

    return compose_word(digit_word)
