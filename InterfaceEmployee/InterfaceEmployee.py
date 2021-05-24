from abc import ABC, abstractmethod


class Work(ABC):
    @abstractmethod
    def work(self):
        raise NotImplementedError()

class DevelopApp(ABC):
    @abstractmethod
    def develop_app(self):
        raise NotImplementedError()


class ExecuteTask(ABC):
    @abstractmethod
    def execute_task(self):
        raise NotImplementedError()


class SignDoc(ABC):
    @abstractmethod
    def sign_doc(self):
        raise NotImplementedError()


class RecruitPeople(ABC):
    @abstractmethod
    def recruit_people(self):
        raise NotImplementedError()


class LeadPeople(ABC):
    @abstractmethod
    def lead_people(self):
        raise NotImplementedError()

class GiveTask(ABC):
    @abstractmethod
    def give_task(self):
        raise NotImplementedError()


