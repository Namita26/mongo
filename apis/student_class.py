"""
API for sending SMS
"""
from flask import current_app as app
from flask import request
from flask_restful import Resource



def fetch_student_course_performance(db, student_id, class_id):
	marks = []
	class_wise_records = db['grades'].find_one({"student_id": student_id, "class_id": class_id})

	for record in class_wise_records.get("scores"):
		record["marks"] = int(record.get("score"))
		del record["score"]

	return {
		"class_id": class_id, "student_id": student_id,
		"student_name": db["students"].find_one({"_id": student_id}).get("name"),
		"marks": class_wise_records.get("scores")
	}


# get grades remaining:

class StudentCoursePerformance(Resource):

	def __init__(self):
		self.db = app.config["db"]

	def get(self, student_id, class_id):
		"""
		Fetch all classes a user student belongs to and total marks
		a student has obtained in a class.
		:param student_id:
		:param class_id
		"""
		if not self.db["students"].find_one({"_id": student_id}):
			return {"message": "Invalid student id."}

		if not self.db['grades'].find_one({"student_id": student_id, "class_id": class_id}):
			return {"message": "This student is not in this class."}

		return fetch_student_course_performance(self.db, student_id, class_id)


class CourseStudentPerformance(Resource):

	def __init__(self):
		self.db = app.config["db"]

	def get(self, class_id, student_id):
		"""
		Fetch all classes a user student belongs to and total marks
		a student has obtained in a class.
		:param student_id:
		:param class_id
		"""
		if not self.db["students"].find_one({"_id": student_id}):
			return {"message": "Invalid student id."}

		if not self.db['grades'].find_one({"student_id": student_id, "class_id": class_id}):
			return {"message": "This student is not in this class."}

		return fetch_student_course_performance(self.db, student_id, class_id)