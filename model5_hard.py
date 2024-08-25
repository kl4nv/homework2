class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
    def __eq__(self, other):
        if isinstance(other, User):
            if other.nickname == self.nickname:
                return True
        elif other == self.nickname:
            return True
    def __repr__(self):
        item_list = str([self.nickname, self.password, self.age])
        return item_list
    def __str__(self):
        return self.nickname
    def __hash__(self):
        return hash(self.password)

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
    def __eq__(self, other):
        if other.title == self.title:
            return True
    def __repr__(self):
        return self.title

class UrTube:
    def __init__(self):
        self.current_user = None
        self.users = []
        self.videos = []
    def __contains__(self, item):
        return item in self.users or item in self.videos
    def add(self, *video):
        for i in video:
            if i not in self.videos:
                if isinstance(i, Video):
                    self.videos.append(i)
        return self.videos
    def log_in(self, nickname, password):
        for i in range(0, len(self.users)):
            if nickname == self.users[i].nickname and hash(password) == self.users[i].password:
                self.current_user = self.users[i]
                return self.current_user
            else:
                return print(f'Пользователь {nickname} не зарегистрирован')
    def register(self, nickname, password, age):
        user = User(nickname, hash(password), age)
        if user not in self.users:
            self.users.append(user)
            self.current_user = User(nickname, password, age)
        else:
            print(f'Пользователь {nickname} уже существует')
    def log_out(self):
        return self.current_user == None
    def get_videos(self, find_word):
        find_list = []
        for i in range(0, len(self.videos)):
            if str(self.videos[i]).lower().find(find_word.lower()) != -1:
                find_list += [f'{self.videos[i]}']
        if len(find_list) == 0:
            return print(f'По поиску "{find_word}" ничего не нашлось')
        else:
            return find_list
    def time_sleep(self, video):
        import time
        for j in range(video.duration):
            time.sleep(1)
            print(end=f'{j + 1} ')
        print(f"Конец видео")
    def watch_video(self, name_video):
        if self.current_user != None:
            for i in range(0, len(self.videos)):
                if name_video == str(self.videos[i]):
                    if self.videos[i].adult_mode == True:
                        if self.current_user.age >= 18:
                            self.time_sleep(self.videos[i])
                        else:
                            print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    else:
                        self.time_sleep(self.videos[i])
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')




