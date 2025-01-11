# Funktsiya: Har bir qatorda logotipni ishlab chiqish
def generate_line(spaces, chars, extra_spaces=0):
    return ' ' * spaces + 'H' * chars + ' ' * extra_spaces + 'H' * chars

# Logotipning har bir qatorini saqlash uchun ro'yxat
logo_lines = []

# Yuqori qismi
logo_lines.append(generate_line(4, 1))
logo_lines.append(generate_line(3, 3))
logo_lines.append(generate_line(2, 5))
logo_lines.append(generate_line(1, 7))
logo_lines.append(generate_line(0, 9))

# O'rta qismi (asosiy harf H)
for _ in range(6):
    logo_lines.append(generate_line(0, 5, 15))

# O'rta qismi (H harfi bilan to'liq qatorlar)
logo_lines.append('H' * 20)
logo_lines.append('H' * 20)
logo_lines.append('H' * 20)

# O'rta qismi (asosiy harf H)
for _ in range(6):
    logo_lines.append(generate_line(0, 5, 15))

# Pastki qismi
logo_lines.append(generate_line(15, 9))
logo_lines.append(generate_line(16, 7))
logo_lines.append(generate_line(17, 5))
logo_lines.append(generate_line(18, 3))
logo_lines.append(generate_line(19, 1))

# Logotipni chop etish
for line in logo_lines:
    print(line)
