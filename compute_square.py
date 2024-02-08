transitions = {
    ('q0', '0'): ('q1', '1', 'R'),
    ('q1', '0'): ('q1', '0', 'R'),
    ('q1', '$'): ('q2', '$', 'L'),
    ('q2', 'ç'): ('q6', 'ç', 'R'),
    ('q2', '0'): ('q3', 'x', 'R'),
    ('q2', '1'): ('q3', 'y', 'R'),
    ('q2', 'x'): ('q2', 'x', 'L'),
    ('q2', 'y'): ('q2', 'y', 'L'),
    ('q3', 'x'): ('q3', 'x', 'R'),
    ('q3', 'y'): ('q3', 'y', 'R'),
    ('q3', '$'): ('q4', '$', 'R'),
    ('q4', '1'): ('q4', '1', 'R'),
    ('q4', 'B'): ('q5', '1', 'L'),
    ('q5', '1'): ('q5', '1', 'L'),
    ('q5', '$'): ('q2', '$', 'L'),
    ('q6', 'x'): ('q6', '0', 'R'),
    ('q6', 'y'): ('q6', '1', 'R'),
    ('q6', '$'): ('q7', '$', 'L'),
    ('q7', '0'): ('q7', '0', 'L'),
    ('q7', '1'): ('q8', '1', 'R'),
    ('q8', '0'): ('q1', '1', 'R'),
    ('q8', '$'): ('q9', '$', 'R')
}

def compute_square(input_num):
    tape = list('ç' + input_num + '$')
    state = 'q0'
    head = 1

    configurations = []

    current_config = ''.join(tape)
    configurations.append(current_config)

    while state != 'q9':
        symbol = tape[head]
        key = (state, symbol)
        if key not in transitions:
            return None, configurations

        tape[head] = transitions[key][1]
        if transitions[key][2] == 'R':
            if head == len(tape) - 1:
                tape.append('B')
            head += 1
        elif transitions[key][2] == 'L':
            if head == 0:
                tape.insert(0, 'B')
            else:
                head -= 1

        state = transitions[key][0]

        new_config = ''.join(tape)
        if new_config != current_config:
            configurations.append(new_config)
            current_config = new_config

    result = ''
    for symbol in tape[1:]:
        if symbol == 'x':
            result += '0'
        elif symbol == 'y':
            result += '1'

    return result, configurations


number = int(input("Karesini hesaplamak istediğiniz sayıyı girin: "))
input_num = '0' * number
result, configurations = compute_square(input_num)

if result is not None:
    print("Konfigürasyonlar:")
    for config in configurations:
        print('|'.join(list(config)))
    print(f"{number} sayısının karesi: {number ** 2}")
else:
    print(f"{number} sayısı için geçerli bir sonuç bulunamadı.")