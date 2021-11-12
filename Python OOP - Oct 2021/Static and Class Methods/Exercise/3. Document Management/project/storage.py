from project.category import Category
from project.topic import Topic
from project.document import Document


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        category = self.__get_object_by_id(self.categories, category_id)
        category.name = new_name

    def edit_topic(self, topic_id, new_topic, new_storage_filder):
        topic = self.__get_object_by_id(self.topics, topic_id)
        topic.topic = new_topic
        topic.storage_folder = new_storage_filder

    def edit_document(self, document_id, new_file_name):
        document = self.__get_object_by_id(self.documents, document_id)
        document.file_name = new_file_name

    def delete_category(self, category_id):
        category = self.__get_object_by_id(self.categories, category_id)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.__get_object_by_id(self.topics, topic_id)
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = self.__get_object_by_id(self.documents, document_id)
        self.documents.remove(document)

    def get_document(self, document_id):
        return self.__get_object_by_id(self.documents, document_id)

    def __get_object_by_id(self, objects, id):
        for object in objects:
            if object.id == id:
                return object

    def __repr__(self):
        return "\n".join([str(x) for x in self.documents])