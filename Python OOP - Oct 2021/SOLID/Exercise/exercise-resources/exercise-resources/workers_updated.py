from abc import abstractmethod, ABC
import time


class WorkableWorker(ABC):
    @abstractmethod
    def work(self):
        pass


class EatableWorker(ABC):
    @abstractmethod
    def eat(self):
        pass


class Worker(WorkableWorker, EatableWorker):
    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(WorkableWorker, EatableWorker):
    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Manager(ABC):
    def __init__(self):
        self.worker = None

    @abstractmethod
    def set_worker(self, worker):
        pass


class WorkManager(Manager):
    def set_worker(self, worker):
        assert isinstance(worker, WorkableWorker), "`worker` must be of type {}".format(WorkableWorker)

        self.worker = worker

    def manage(self):
        self.worker.work()


class BreakManager(Manager):
    def set_worker(self, worker):
        assert isinstance(worker, EatableWorker), "`worker` must be of type {}".format(EatableWorker)

        self.worker = worker

    def lunch_break(self):
        self.worker.eat()


class Robot(WorkableWorker):
    def work(self):
        print("I'm a robot. I'm working....")


work_manager = WorkManager()
break_manager = BreakManager()
work_manager.set_worker(Worker())
break_manager.set_worker(Worker())
work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(SuperWorker())
break_manager.set_worker(SuperWorker())
work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(Robot())
work_manager.manage()
try:
    break_manager.set_worker(Robot())
    break_manager.lunch_break()
except:
    pass