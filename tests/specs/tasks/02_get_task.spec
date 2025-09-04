# Tasks - Get by ID

## Get task by ID

* I send a GET request for task with id "created_task_id"
* the response status code should be "200"
* the response should contain "{\"title\":\"Test Task\",\"description\":\"Test description\",\"status\":\"CREATED\"}"


## Get non-existing task

* I send a GET request to "/tasks/00000000-0000-0000-0000-000000000000"
* the response status code should be "404"

## Get task with invalid UUID format

* I send a GET request to "/tasks/invalid-uuid-format"
* the response status code should be "500"
