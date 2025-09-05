# Tasks - Update

## Update existing task

* I send a PUT request for task with id "created_task_id" with payload "{\"title\":\"Updated Task\",\"description\":\"Updated description\",\"status\":\"IN_PROGRESS\"}"
* the response status code should be "200"
* the response should contain "{\"title\":\"Updated Task\",\"description\":\"Updated description\",\"status\":\"IN_PROGRESS\"}"


## Update non-existing task

* I send a PUT request to "/tasks/00000000-0000-0000-0000-000000000000" with payload "{\"title\":\"Non-existing\"}"
* the response status code should be "404"


## Update task with non-existing field

* I send a PUT request for task with id "created_task_id" with payload "{\"non_existing_field\":\"value\"}"
* the response status code should be "422"


## Update task with invalid status

* I send a PUT request for task with id "created_task_id" with payload "{\"status\":\"INVALID_STATUS\"}"
* the response status code should be "422"
* the response should contain validation error for field "status"


## Update task with empty title

* I send a PUT request for task with id "created_task_id" with payload "{\"title\":\"\"}"
* the response status code should be "422"
* the response should contain validation error for field "title"


## Update task with wrong data types

* I send a PUT request for task with id "created_task_id" with payload "{\"title\":123,\"description\":true,\"status\":[]}"
* the response status code should be "422"
* the response should contain validation error for field "title"
* the response should contain validation error for field "description"
* the response should contain validation error for field "status"
