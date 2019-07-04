from locust import HttpLocust, TaskSet, TaskSequence, task, seq_task
import random, time, json, threading

_lock = threading.Lock()
class MyTaskSet(TaskSequence):

    names = open("names.txt").readlines()
    dorms = ["'Harwood'", "'Wig'", "'Oldenborg'", "'Lyon'", "'Smiley'",
                    "'Mudd'", "'Blaisdell'", "'Sontag'", "'Dialynas'",
                    "'Walker'", "'Clark I'", "'Clark III'"]
    #available id and database ringbuf
    ids = list(range(10357855, 100000000))
    db = []

    @seq_task(2)
    def list(self):
        with _lock:
            self.client.get("/students")

    @seq_task(3)
    def get(self):
        with _lock:
            id = self.db[-1]
            self.client.get(f"/students/{id}", name=": single student")

    @seq_task(1)
    @task(2)
    def register(self):
        first = random.choice(self.names).strip("\n")
        last = random.choice(self.names).strip("\n")
        name = "'" + first + " " + last + "'"

        dorm = random.choice(self.dorms)

        with _lock:
            try:
                id = self.ids[-1]
                self.client.post("/students/register", json = {
                        "id": id,
                        "name": name,
                        "dorm": dorm
                }, name=": new student")
            except:
                print(f"POST failed. Putting back {id}...")
            else:
                self.db.append(self.ids.pop())

    @seq_task(4)
    def delete(self):
        with _lock:
            id = self.db[-1]
            self.client.delete(f"/students/delete/{id}", name=": remove student")
            self.ids.append(self.db.pop())

    @seq_task(5)
    def update(self):
        changeDorm = bool(random.getrandbits(1))
        new = random.choice(self.dorms)
        if not changeDorm:
            first = random.choice(self.names).strip("\n")
            last = random.choice(self.names).strip("\n")
            new = "'" + first + " " + last + "'"

        body = {"changeDorm": changeDorm, "new": new}

        with _lock:
            try:
                id = self.db[-1]
                self.client.put(f"/students/update/{id}", json = body, name=": update student")
            except:
                print(f"PUT failed.... Update cancelled")

class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 5000
    max_wait = 15000
