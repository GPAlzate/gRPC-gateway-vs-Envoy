from locust import HttpLocust, TaskSet, TaskSequence, task, seq_task
import random, time, threading, string

import resource
resource.setrlimit(resource.RLIMIT_NOFILE, (10240, 9223372036854775807))

_CHARS = string.ascii_letters
class MyTaskSet(TaskSequence):

    #@task(1)
    def list(self):
        self.client.get("/companies")

    @task
    def read(self):
        code = random.randint(10000000, 99999999)
        self.client.get(f"/companies/{code}", name=": single company")

    @task
    def register(self):
        code = random.randint(10000000, 99999999)
        name = ''.join(random.sample(_CHARS, 12))
        ops = random.randint(1, 99)

        self.client.post("/register", json = {
                "companyCode": code,
                "companyName": name,
                "numOpenings": ops,
                "isBrokerage": bool(random.getrandbits(1))
        }, name=": new company")

    @task
    def delete(self):
        code = random.randint(10000000, 99999999)
        self.client.delete(f"/delete/{code}", name=": remove company")

    @task
    def update(self):
        code = random.randint(10000000, 99999999)
        name = ''.join(random.sample(_CHARS, 12))
        ops = random.randint(1, 99)

        self.client.put("/update/{code}", json = {
                "companyCode": code,
                "companyName": name,
                "numOpenings": ops,
                "isBrokerage": bool(random.getrandbits(1))
        }, name=": update company")

class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 5000
    max_wait = 15000
