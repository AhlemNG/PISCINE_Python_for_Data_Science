def ft_tqdm(lst: range) -> None:
    """iterable: an iterable object to decorate
        return: an iterator that behaves like the original iterable,
        but prints a dynamically updating progress bar 
        each time a value is requested"""
    total = len(lst)
    bar_length = 79
    for i in range(total):
        percent = int((i + 1) / total * 100)
        filled_length = int(bar_length * (i + 1) / total)
        bar = '■' * filled_length + '-' * (bar_length - filled_length)
        print(f'\r{percent:3d}% |{bar}| {i + 1}/{total}', end='', flush=True)
        yield lst[i]
    print()

# import time


# for elem in ft_tqdm(range(10)):
#     time.sleep(0.2)
