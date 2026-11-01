# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    core.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jaoh <jaoh@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/10/11 15:22:54 by jaoh              #+#    #+#              #
#    Updated: 2026/10/11 15:22:55 by jaoh             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def count_in_list(lst: list, item: any) -> int:
    """Count the number of occurrences of item within lst."""
    return lst.count(item)
