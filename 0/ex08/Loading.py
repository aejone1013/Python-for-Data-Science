# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jaoh <jaoh@student.42.fr>                  +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/10/11 15:22:43 by jaoh              #+#    #+#              #
#    Updated: 2026/10/11 15:22:44 by jaoh             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import time


def format_time(seconds: float) -> str:
    """Format a duration in seconds as MM:SS."""
    minutes, secs = divmod(int(seconds), 60)
    return f"{minutes:02d}:{secs:02d}"


def ft_tqdm(lst: range) -> None:
    """Yield items of lst while displaying a tqdm-like progress bar."""
    total = len(lst)
    start = time.time()
    for i, elem in enumerate(lst, start=1):
        percent = i / total
        try:
            columns = os.get_terminal_size().columns
        except OSError:
            columns = 80
        suffix = f"| {i}/{total}"
        elapsed = time.time() - start
        rate = i / elapsed if elapsed > 0 else 0
        remaining = (total - i) / rate if rate > 0 else 0
        suffix += (
            f" [{format_time(elapsed)}<{format_time(remaining)}, "
            f"{rate:.2f}it/s]"
        )
        prefix = f"{int(percent * 100):3d}%|"
        bar_width = max(columns - len(prefix) - len(suffix) - 1, 1)
        filled = int(bar_width * percent)
        bar = "=" * filled
        if filled < bar_width:
            bar += ">" + " " * (bar_width - filled - 1)
        print(f"\r{prefix}{bar}{suffix}", end="", flush=True)
        yield elem
