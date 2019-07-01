from locust import HttpLocust, TaskSet

class MyTaskSet(TaskSet):
    @task
    def list(self):
        self.client.get("/students")

    @task
    def get(self):
        self.client.get("/students/10357854")

class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 5000
    max_wait = 10000
