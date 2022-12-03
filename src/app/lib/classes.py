# class User(object):
#     def __init__(self, name, age, gender, job, hobby):
#         self.name   = name
#         self.age    = age
#         self.gender = gender
#         self.job    = job
#         self.hobby  = hobby

class User(object):
    def __init__(self, id, name, surname, age):
        self.id = id
        self.name = name
        self.surname = surname
        self.age = age


# class Music(object):
#     def __init__(self, title, album, group, bpm):
#         self.title  = title
#         self.album  = album
#         self.group  = group
#         self.bpm    = bpm

class Music(object):
    def __init__(self, name, author, raiting):
        self.name  = name
        self.author  = author
        self.raiting  = raiting
