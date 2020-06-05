from locust import User, TaskSet, task, between

class MyTaskSet(TaskSet):
    @task
    def my_task(self):
        print("executing my_task")

class MyUser(User):
    tasks = [MyTaskSet]
    wait_time = between(5, 15)