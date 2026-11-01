# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whatis.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jaoh <jaoh@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/10/11 15:22:26 by jaoh              #+#    #+#              #
#    Updated: 2026/10/13 16:52:34 by jaoh             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


def main():
    """Tell whether the integer given as argument is odd or even."""
    try:
        args = sys.argv[1:]
        assert len(args) < 2, "more than one argument is provided"
        if not args:
            return
        try:
            number = int(args[0])
        except ValueError:
            raise AssertionError("argument is not an integer")
        print("I'm Even." if number % 2 == 0 else "I'm Odd.")
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
