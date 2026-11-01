# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_filter.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jaoh <jaoh@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/10/11 15:22:35 by jaoh              #+#    #+#              #
#    Updated: 2026/10/11 15:41:30 by jaoh             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if function is None:
        return [item for item in iterable if item]
    return [item for item in iterable if function(item)]
