

path = "../test/video/vid"


def save_parts(part, byte):
    with open(f'{path}/{1000 + part}', 'wb') as file:
        file.write(byte)


file_name = "../source/vid.mp4"


with open(file_name, 'rb') as f:
    byte_stream = f.read()

size = len(byte_stream) - 40000
count = size / 2048000
count = count if count % 1 == 0 else int(count) + 1

print(f'size = {size} count = {count}')

for i in range(count):
    save_parts(i, byte_stream[i * 2048000:(i + 1) * 2048000])

with open(f"{path}/data", 'w', encoding='utf-8') as file:
    file.write(f'{path}\n{count}')
