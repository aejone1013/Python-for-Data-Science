# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterstring.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jaoh <jaoh@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/10/11 15:22:31 by jaoh              #+#    #+#              #
#    Updated: 2026/10/11 15:41:33 by jaoh             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

from ft_filter import ft_filter


def main():
    """Print words from a string argument longer than an integer argument."""
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        assert sys.argv[2].lstrip("-").isdigit(), "the arguments are bad"
        text = sys.argv[1]
        length = int(sys.argv[2])
        words = [word for word in text.split()]
        print(ft_filter(lambda word: len(word) > length, words))
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
