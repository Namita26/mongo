from flask import Flask
from flask_restful import Resource, Api
from pymongo import MongoClient
import pprint, json
from apis.students import StudentsAPIHandler, StudentClasses, StudentPerformance
from apis.classes import Classes, ClassStudent, ClassStudentPerformance
from apis.student_class import CourseStudentPerformance, StudentCoursePerformance


app = Flask(__name__)
api = Api(app)


client = MongoClient('mongodb+srv://prodigal_be_test_01:prodigaltech@test-01-ateon.mongodb.net/sample_training')
db = client['sample_training']
app.config['db'] = db


@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"


api.add_resource(StudentsAPIHandler, '/students')
api.add_resource(StudentClasses, '/student/<int:student_id>/classes')
api.add_resource(StudentPerformance, '/student/<int:student_id>/performance')
api.add_resource(Classes, '/classes')
api.add_resource(ClassStudent, '/class/<int:class_id>/students')
api.add_resource(ClassStudentPerformance, '/class/<int:class_id>/performance')
api.add_resource(CourseStudentPerformance, '/class/<int:class_id>/student/<int:student_id>')
api.add_resource(StudentCoursePerformance, '/student/<int:student_id>/class/<int:class_id>')



if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
