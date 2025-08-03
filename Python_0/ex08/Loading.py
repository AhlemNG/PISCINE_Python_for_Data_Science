def ft_tqdm(lst: range) -> None:
    total = len(lst)
    for i, val in enumerate(lst, start=1):
        percent = int(i / total * 100)
        bar_length = 20
        filled_length = int(bar_length * i / total)
        bar = '#' * filled_length + '-' * (bar_length - filled_length)
        print(f'{percent}% |{bar}| {i}/{total}')


ft_tqdm(range(10))
