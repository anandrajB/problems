class Base:

    def __init__(self, value) -> None:
        self.value = value

    def find_common_user(self):
        common_users = set(self.value[0])
        for item in self.value:
            common_users.intersection_update(item)
        return sorted(common_users, reverse=True)

    def find_atleast_one_user(self):
        user_data = {}
        for item in self.value:
            for user in item:
                if user in user_data:
                    user_data[user] += 1
                else:
                    user_data[user] = 1
        return sorted(
            [value for value, count in user_data.items() if count == 1], reverse=True
        )

    def find_atleast_one_user_m2(self):
        from collections import Counter

        return [
            user
            for user, count in Counter(
                user for value in self.value for user in value
            ).items()
            if count == 1
        ]

    def find_unique_users(self):
        return sorted(
            set([user for value in self.value for user in value]), reverse=False
        )

    def find_most_frequent_user(self):
        from collections import Counter

        counter = Counter(user for value in self.value for user in value)
        return {user: count for user, count in counter.most_common(2)}


data = [
    ["Anand", "Sheik", "Rahul", "Dinesh"],
    ["Anand", "Sheik", "Ibson", "Dinesh"],
    ["Anand", "Sheik", "Rahul", "Dinesh"],
    ["Anand", "Sheik", "Dinesh", "Donald"],
    ["Anand", "Sheik", "Ibson", "Dinesh"],
]
ds = Base(value=data)
print(ds.find_most_frequent_user())
# print(ds.find_common_user())
# print(ds.find_atleast_one_user())
# print(ds.find_unique_users())
