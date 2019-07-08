from locust import HttpLocust, TaskSet, TaskSequence, task, seq_task
import random, time, threading, string

import resource
resource.setrlimit(resource.RLIMIT_NOFILE, (10240, 9223372036854775807))

_lock = threading.Lock()
_CHARS = string.ascii_letters
class MyTaskSet(TaskSequence):

    @seq_task(2)
    def list(self):
        #with _lock:
        self.client.get("/students")

    @seq_task(3)
    def get(self):
        #with _lock:
        id = random.randint(10000000, 99999999)
        self.client.get(f"/students/{id}", name=": single student")

    @seq_task(1)
    @task(2)
    def register(self):
        id = random.randint(10000000, 99999999)
        name = ''.join(random.sample(_CHARS, 8)) + " " + ''.join(random.sample(_CHARS, 8))
        dorm = ''.join(random.sample(_CHARS, 12)) 

        #with _lock:
        self.client.post("/students/register", json = {
                "id": id,
                "name": name,
                "dorm": dorm
        }, name=": new student")

    @seq_task(4)
    def delete(self):
        #with _lock:
        id = random.randint(10000000, 99999999)
        self.client.delete(f"/students/delete/{id}", name=": remove student")

    @seq_task(5)
    def update(self):
        changeDorm = bool(random.getrandbits(1))
        new = ''.join(random.sample(_CHARS, 12)) 
        if not changeDorm:
            new = ''.join(random.sample(_CHARS, 8)) + " " + ''.join(random.sample(_CHARS, 8))

        body = {"changeDorm": changeDorm, "new": new}

        #with _lock:
        id = random.randint(10000000, 99999999)
        self.client.put(f"/students/update/{id}", json = body, name=": update student")

class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 5000
    max_wait = 15000
