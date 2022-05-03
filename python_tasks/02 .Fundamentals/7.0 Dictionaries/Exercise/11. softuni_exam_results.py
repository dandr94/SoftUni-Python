def valid_user(language: str):
    if language != 'banned':
        return True

    return False


def new_user(my_dict: dict, username: str):
    if username not in my_dict:
        my_dict[username] = 0


def new_lang(sub_dict: dict, lang_name: str):
    if lang_name not in sub_dict:
        sub_dict[lang_name] = 0


def add_points(sub_dict: dict, lang_name: str):
    if lang_name in sub_dict:
        sub_dict[lang_name] += 1


def check_points(my_dict: dict, username: str, username_points: int):
    if my_dict[username] < username_points:
        my_dict[username] = username_points


def banned(my_dict: dict, username: str):
    if username in my_dict:
        del my_dict[username]


user_points = {}
lang_submission = {}
cmd = input()

while cmd != 'exam finished':
    cmd_split = cmd.split('-')
    user = cmd_split[0]
    lang = cmd_split[1]

    if valid_user(lang):
        points = int(cmd_split[2])

        new_user(user_points, user)
        new_lang(lang_submission, lang)
        check_points(user_points, user, points)
        add_points(lang_submission, lang)
    else:
        banned(user_points, user)

    cmd = input()

print('Results:')
for key, value in sorted(user_points.items(), key=lambda x: (-x[1], x[0])):
    print(f'{key} | {value}')
print('Submissions:')
for key, value in sorted(lang_submission.items(), key=lambda x: (-x[1], x[0])):
    print(f'{key} - {value}')