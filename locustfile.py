from locust import HttpLocust, TaskSet, task
import random, time

class MyTaskSet(TaskSet):

    names = open("names.txt").readlines()
    ids = list(range(10000000, 100000000))
    db = []
    dorms = ["'Harwood'", "'Wig'", "'Oldenborg'", "'Lyon'", "'Smiley'",
                    "'Mudd'", "'Blaisdell'", "'Sontag'", "'Dialynas'",
                    "'Walker'", "'Clark I'", "'Clark III'"]

    def on_start(self):
        self.register()

    @task
    def list(self):
        self.client.get("/students")

    @task
    def get(self):
        if self.db:
            id = self.db[-1]
            self.client.get(f"/students/{id}")

    @task(2)
    def register(self):
        if self.ids:
            first = random.choice(self.names).strip("\n")
            last = random.choice(self.names).strip("\n")
            name = "'" + first + " " + last + "'"

            dorm = random.choice(self.dorms)
            try:
                id = self.ids[-1]
                self.client.post("/students/register", json = {
                        "id": id,
                        "name": name,
                        "dorm": dorm
                })
            except:
                print(f"POST failed. Putting back {id}...")
            else:
                self.db.append(self.ids.pop())


    @task
    def delete(self):
        if self.db:
            id = self.db[-1]
            self.client.delete(f"/students/delete/{id}")
            self.ids.append(self.db.pop())

    @task
    def update(self):
        if len(self.db):
            id = self.db[-1]
            changeDorm = random.getrandbits(1)
            new = random.choice(self.dorms)
            if not changeDorm:
                first = random.choice(self.names).strip("\n")
                last = random.choice(self.names).strip("\n")
                new = "'" + first + " " + last + "'"

            try:
                self.client.put(f"/students/update/{id}", json = {
                        "changeDorm": changeDorm,
                        "new": new
                })
            except:
                print(f"PUT failed.... Update cancelled")

    def on_stop(self):
        self.client.delete("/students/clear")

class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 5000
    max_wait = 10000
