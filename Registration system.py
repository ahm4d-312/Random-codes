amount_of_users = int(input())
usernames_map = {}
for i in range(amount_of_users):
    user_name = input()
    if user_name not in usernames_map:
        usernames_map[user_name] = 1
        print("OK")
    else:
        print(user_name, usernames_map[user_name], sep="")
        usernames_map[user_name] += 1
