def make_pyramid(x):
    lines = []
    for i in range(1, x + 1):
        spasi = x - i
        lines.append(" " * spasi + "*" * (2*i - 1))
    return "\n".join(lines)

def make_segitiga_kiri(x):
    return "\n".join("*" * i for i in range(1, x + 1))

def make_segitiga_kanan(x):
    lines = []
    for i in range(1, x + 1):
        spasi = x - i
        lines.append(" " * spasi + "*" * i)
    return "\n".join(lines)

def make_belah_ketupat(x):
    lines = []
    for i in range(1, x + 1):
        spasi = x - i
        lines.append(" " * spasi + "*" * (2*i - 1))
    for i in range(x - 1, 0, -1):
        spasi = x - i
        lines.append(" " * spasi + "*" * (2*i - 1))
    return "\n".join(lines)
