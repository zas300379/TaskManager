# Tasks - Delete

## Delete existing task

* I send a DELETE request for task with id "created_task_id"
* the response status code should be "200"
* the response should contain "{\"message\":\"Task deleted\"}"
* verify task "created_task_id" is deleted


## Delete non-existing task

* I send a DELETE request to "/tasks/00000000-0000-0000-0000-000000000000"
* the response status code should be "404"
