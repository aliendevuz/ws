import json
import os


dicts = []
uz_dicts = []


class Dict:
    def __init__(self, word, transcript, t, describe, sample):
        self.word = word
        self.transcript = transcript
        self.type = t
        self.describe = describe
        self.sample = sample


def get_tag(tag: str, string: str):
    return string[string.find(f'<{tag}>')+len(f'<{tag}>'):string.find(f'</{tag}>')]


for i in range(5000, 8600):
    with open(f"C:/Users/alien/Documents/Loyiha/Alien/sources/source/dictup__/{i}", encoding="utf-8") as f:
        data = f.read()
        word = get_tag('EN', data)
        transcript = get_tag('TR', data)
        t = get_tag('TY', data)
        describe = get_tag('DC', data)
        sample = get_tag('SP', data)
        uz_word = get_tag('UZ', data)
        uz_transcript = 'null'
        uz_t = 'null'
        uz_describe = 'null'
        uz_sample = 'null'
        dicts.append(Dict(word, transcript, t, describe, sample))
        uz_dicts.append(Dict(uz_word, uz_transcript, uz_t, uz_describe, uz_sample))


# def write_to_file(dat, path):
#     try:
#         with open(path, 'w') as f:
#             json.dump(dat, f)
#     except Exception as e:
#         print(f"Xatolik yuz berdi: {e}")


json_data = json.dumps([{'word': d.word, 'transcript': d.transcript, 'type': d.type, 'describe': d.describe, 'sample': d.sample} for d in dicts])
json_data_2 = json.dumps([{'word': d.word, 'transcript': d.transcript, 'type': d.type, 'describe': d.describe, 'sample': d.sample} for d in uz_dicts])

print(json_data)
print(json_data_2)
with open("C:\\Users\\alien\\Documents\\Loyiha\\Alien\\sources\\dictup\\book\\essential\\strings\\dict.json", 'w', encoding="utf-8") as f:
    f.write(json_data)
with open("C:\\Users\\alien\\Documents\\Loyiha\\Alien\\sources\\dictup\\book\\essential\\strings-uz\\dict.json", 'w', encoding="utf-8") as f:
    f.write(json_data_2)

# write_to_file(dat, "C:\\Users\\alien\\Documents\\Loyiha\\Alien\\sources\\dictup\\book\\essential\\barcha_ma'lumotlar.json")
