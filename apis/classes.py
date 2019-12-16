"""
API for sending SMS
"""
from flask import current_app as app
from flask import request
from flask_restful import Resource


class Classes(Resource):

	def __init__(self):
		self.db = app.config["db"]

	def get(self):
		"""
		Fetch all classes present.
		"""
		class_objects = []
		class_id_objects = {}
		grade_records = self.db['grades'].find()

		for obj in grade_records:
			if obj.get("class_id") not in class_id_objects:
				class_id_objects[obj.get("class_id")] = 1
				class_objects.append({"class_id": obj.get("class_id")})

		return class_objects


class ClassStudent(Resource):

	def __init__(self):
		self.db = app.config["db"]

	def get(self, class_id):
		"""
		Fetch all classes present.
		"""
		student_objects = []
		class_wise_records = self.db['grades'].find({"class_id": class_id})

		for class_record in class_wise_records:
			student_record = self.db["students"].find_one({"_id": class_record.get("student_id")})
			student_objects.append({"student_id": student_record.get("_id"), "student_name": student_record.get("name")})

		return {"class_id": class_id, "students": student_objects}


class ClassStudentPerformance(Resource):

	def __init__(self):
		self.db = app.config["db"]

	def get(self, class_id):
		"""
		Fetch all classes present.
		"""
		student_objects = []
		class_wise_records = self.db['grades'].find({"class_id": class_id})

		for class_record in class_wise_records:
			student_record = self.db["students"].find_one({"_id": class_record.get("student_id")})
			student_objects.append({
				"student_id": student_record.get("_id"),
				"student_name": student_record.get("name"),
				"total_marks": int(sum(map(lambda x: x.get("score"), class_record.get("scores"))))
			})

		return {"class_id": class_id, "students": student_objects}


class ClassStudentGrades(Resource):

	def __init__(self):
		self.db = app.config["db"]

	def get(self, class_id):
		"""
		Fetch all classes present.
		"""
		student_objects = []
		# class_wise_records = grades.get_grade_records_by_class_id(self.db, class_id)
		class_wise_records = self.db['grades'].find({"class_id": class_id})

		for class_record in class_wise_records:
			student_record = self.db["students"].find_one({"_id": class_record.get("student_id")})
			student_objects.append({
				"student_id": student_record.get("_id"),
				"student_name": student_record.get("name"),
				"total_marks": int(sum(map(lambda x: x.get("score"), class_record.get("scores"))))
			})

		student_objects = sorted(student_objects, key = lambda i: i['total_marks'], reverse=True)
		total_students = len(student_objects)

		# 1st 1/12th grade A
		grade_A = int(total_students/12)
		for item in student_objects[0:grade_A]:
			item.update({"grade": "A"})

		# 2nd 1/6th grade B
		grade_B = int((total_students-grade_A)/6)
		for item in student_objects[grade_A:(grade_A+grade_B)]:
			item.update({"grade": "B"})

		# 3rd 1/4th grade C
		grade_C = int((total_students-grade_A-grade_B)/4)
		for item in student_objects[(grade_A+grade_B): (grade_A+grade_B+grade_C)]:
			item.update({"grade": "C"})

		# 4th
		grade_D = total_students - grade_A - grade_B - grade_C
		for item in student_objects[grade_D:]:
			item.update({"grade": "D"})

		return {"class_id": class_id, "students": student_objects}