def to_json_array(rows) -> str:
    json = '['

    for entity in rows:
        json += str(entity) + ', '

    if (json != '['):
        json = json[:-2]
    json += ']'
    return json


def is_exist(rows) -> bool:
    line = str(rows[0])
    return int(line[-2]) >= 1