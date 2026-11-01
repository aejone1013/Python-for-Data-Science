# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    find_ft_type.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jaoh <jaoh@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/10/11 15:00:44 by jaoh              #+#    #+#              #
#    Updated: 2026/10/11 15:41:43 by jaoh             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def all_thing_is_obj(object: any) -> int:
    """Print the type of the given object and return 42."""
    t = type(object)
    if t is list:
        print(f"List : {t}")
    elif t is tuple:
        print(f"Tuple : {t}")
    elif t is set:
        print(f"Set : {t}")
    elif t is dict:
        print(f"Dict : {t}")
    elif t is str:
        print(f"{object} is in the kitchen : {t}")
    else:
        print("Type not found")
    return 42