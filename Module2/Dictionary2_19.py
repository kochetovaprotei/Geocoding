# list (выводится весь список строго по порядку)
friends = ['Ross', 'Chandler', 'Joey', 'Monica', 'Phoebe', 'Rachel', 'Ross']
print(friends[0] + friends[5])

# множество (выводится только одно значение, регистрозависимы)
friends_2 = {'Ross', 'Chandler', 'Joey', 'Monica', 'Phoebe', 'Rachel', 'Ross'}
print(friends_2)

# словарь (ключ:значение)
friends_3 = {'Ross':'a paleontologist', 'Chandler':'works with numbers', 'Joey':'an actor', 'Monica':'a chief', 'Phoebe':'a masseuse', 'Rachel':'a fashion manager'}
print(friends_3['Ross'])  # напишет значение из словаря

friends_3 = {'Ross':'a paleontologist', 'Chandler':'works with numbers', 'Joey':'an actor', 'Monica':'a chief', 'Phoebe':'a masseuse', 'Rachel':'a fashion manager'}
for key, value in friends_3.items():
    print(key)  # выведет ключи

friends_3 = {'Ross':'a paleontologist', 'Chandler':'works with numbers', 'Joey':'an actor', 'Monica':'a chief', 'Phoebe':'a masseuse', 'Rachel':'a fashion manager'}
for key, value in friends_3.items():
    print(key + ' - ' + value)