# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NULL_not_found.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jaoh <jaoh@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/10/11 15:22:23 by jaoh              #+#    #+#              #
#    Updated: 2026/10/13 14:48:17 by jaoh             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

t = type(object)
if object is None:
    print("Nothing:", object, t)
elif t is float and object != object:
    print("Cheese:", object, t)
elif t is int and object == 0:
    print("Zero:", object, t)
elif t is str and object == "":
    print("Empty:", t)
elif t is bool and object is False:
    print("Fake:", object, t)
else:
    print("Type not Found")
    return 1
return 0