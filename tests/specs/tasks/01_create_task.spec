# Tasks — Create

## Create a new task

* the API is running
* I send a POST request to "/tasks" with payload "{\"title\":\"Test Task\",\"description\":\"Test description\",\"status\":\"CREATED\"}"
* the response status code should be "200"
* the response should contain "{\"title\":\"Test Task\",\"description\":\"Test description\",\"status\":\"CREATED\"}"
* save the response task id as "created_task_id"