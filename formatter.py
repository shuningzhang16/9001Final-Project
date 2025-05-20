def print_boxed_title(title: str, width=50):
    line = "+" + "-" * width + "+"
    print(line)
    print("|" + title.center(width) + "|")
    print(line)

def print_divider(width=50):
    print("-" * width)

def print_summary_line(label: str, value, width=50):
    print(f"{label.ljust(20)} {str(value).rjust(width - 22)}")
