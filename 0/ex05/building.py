# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    building.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jaoh <jaoh@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/10/11 15:22:28 by jaoh              #+#    #+#              #
#    Updated: 2026/10/11 15:41:35 by jaoh             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string


def main():
    """Count upper, lower, punctuation, space and digit characters."""
    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
        if len(sys.argv) == 2:
            text = sys.argv[1]
        else:
            print("What is the text to count?")
            text = sys.stdin.read()

        upper = lower = punct = space = digit = 0
        for char in text:
            if char.isupper():
                upper += 1
            elif char.islower():
                lower += 1
            elif char in string.punctuation:
                punct += 1
            elif char.isspace():
                space += 1
            elif char.isdigit():
                digit += 1

        print(f"The text contains {len(text)} characters:")
        print(f"{upper} upper letters")
        print(f"{lower} lower letters")
        print(f"{punct} punctuation marks")
        print(f"{space} spaces")
        print(f"{digit} digits")
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
