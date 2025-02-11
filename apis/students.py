"""
API for sending SMS
"""
from flask import current_app as app
from flask import request
from flask_restful import Resource


class Student(Resource):

    def __init__(self):
        self.db = app.config["db"]

    def get(self):
        """
        Fetch all students with id and name as details.
        """
        student_documents = []
        students = self.db['students']
        for student in students.find().sort("_id"):
            student_documents.append({"student_id": student.get("_id"), "student_name": student.get("name")})

        return student_documents


class StudentClass(Resource):

	def __init__(self):
		self.db = app.config["db"]

	def get(self, student_id):
		"""
		Fetch all classes a user student belongs to.
		:param student_id<int>
		"""
		if not self.db["students"].find_one({"_id": student_id}):
			return {"message": "Invalid student id."}

		class_objects = []
		classes = self.db['grades'].find({"student_id": student_id})

		# find out class_ids
		for obj in classes:
			class_objects.append({"class_id": obj.get("class_id")})

		return {"student_id":student_id, "student_name": self.db["students"].find_one({"_id": student_id}).get("name"), "classes": class_objects}


class StudentPerformance(Resource):

	def __init__(self):
		self.db = app.config["db"]
	
	def get(self, student_id):
		"""
		Fetch all classes a user student belongs to and total marks
		a student has obtained per class.
		:param student_id<int>
		"""
		if not self.db["students"].find_one({"_id": student_id}):
			return {"message": "Invalid student id."}

		class_objects = []
		classes = self.db['grades'].find({"student_id": student_id})

		# find out class_ids
		for obj in classes:
			class_objects.append({
				"class_id": obj.get("class_id"),
				"total_marks": int(sum(map(lambda x: x.get("score"), obj.get("scores"))))
			})

		return {"student_id":student_id, "student_name": self.db["students"].find_one({"_id": student_id}).get("name"), "classes": class_objects}