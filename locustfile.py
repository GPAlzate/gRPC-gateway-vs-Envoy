from locust import HttpLocust, TaskSet, task
import random

class MyTaskSet(TaskSet):

    @task
    def list(self):
        self.client.get("/students")

    @task
    def get(self):
        if self.added:
            self.client.get(f"/students/{self.added[-1]}")
            added.insert(0, added.pop())

    @task
    def register(self):
        if self.ids
            id = self.ids.pop()
            name = "'" + random.choice(self.names) + " " + random.choice(self.names) + "'"
            dorm = random.choice(self.dorms)
            self.client.post("/students/register", {"id": id, "name": name, "dorm": dorm })
            self.added.append(id)

    @task
    def delete(self):
        if self.added:
            self.client.delete(f"/students/delete/{self.added[-1]}")
            ids.insert(0, added.pop())

    @task
    def update(self):
        if self.added:
            choice = random.getrandbits(1)
            id = self.added[-1]

            first = random.choice(self.names).strip("\n")
            last = random.choice(self.names).strip("\n")
            new = "'" + first + " " + last + "'"

            if choice:
                new = random.choice(self.dorms)
            self.client.put(f"/students/update/{id}", {"changeDorm": choice, "new": new})
            added.insert(0, added.pop())


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
