from locust import HttpLocust, TaskSet, task
import random

class MyTaskSet(TaskSet):

    def list(self):
        name = "'" + random.choice(names) + " " + random.choice(names) + "'"
        self.client.get("/students")

    @task
    def get(self):
        if len(list):
            self.client.get(f"/students/{added[-1]}")
            added.insert(0, added.pop())

    @task
    def register(self):
        id = self.ids.pop()
        name = "'" + random.choice(self.names) + " " + random.choice(self.names) + "'"
        dorm = random.choice(self.dorms)
        self.client.post("/students/register", {"id": id, "name": name, "dorm": dorm })
        self.added.append(id)

    @task
    def delete(self):
        if len(list):
            id = self.added.pop()
            self.client.delete(f"/students/delete/{id}")
            self.ids.append(id)

    def on_stop(self):
        self.client.delete("/students/clear")
    
    def __init__(self, names, ids, added):
        self.ids = list(range(10000000, 100000000))
        self.names = open("names.txt").readlines()
        self.dorms = ["'Harwood'", "'Wig'", "'Oldenborg'", "'Lyon'", "'Smiley'",
                        "'Mudd'", "'Blaisdell'", "'Sontag'", "'Dialynas'",
                        "'Walker'", "'Clark I'", "'Clark III'"]
        self.added = []



class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 5000
    max_wait = 10000
