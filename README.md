# mongo

Indexes to be created on the mongo db to improve the performance are:
1. class_id column from the "grades" table.
1. student_id column from the "grades" table.

I could not create this index on the database as I do not have admin user access. I even tried to create an admin user, however, I could not connect to the database server from my local server as the host was not whitelisted.

Service is deployed at https://prodigal-task.herokuapp.com/

Postman Collection for APIs: https://documenter.getpostman.com/view/9822576/SWECVEsa