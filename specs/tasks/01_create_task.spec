# Tasks — Create

## Create a new task

* the API is running
* I send a POST request to "/tasks" with payload "{\"title\":\"Test Task\",\"description\":\"Test description\",\"status\":\"CREATED\"}"
* the response status code should be "200"
* the response should contain "{\"title\":\"Test Task\",\"description\":\"Test description\",\"status\":\"CREATED\"}"
* save the response task id as "created_task_id"


## Create task with missing required field

* I send a POST request to "/tasks" with payload "{\"description\":\"Test description\",\"status\":\"CREATED\"}"
* the response status code should be "422"
* the response should contain validation error for field "title"


## Create task with empty title

* I send a POST request to "/tasks" with payload "{\"title\":\"\",\"description\":\"Test description\",\"status\":\"CREATED\"}"
* the response status code should be "422"
* the response should contain validation error for field "title"


## Create task with invalid status

* I send a POST request to "/tasks" with payload "{\"title\":\"Test Task\",\"description\":\"Test description\",\"status\":\"INVALID_STATUS\"}"
* the response status code should be "422"
* the response should contain validation error for field "status"


## Create task with wrong data types

* I send a POST request to "/tasks" with payload "{\"title\":123,\"description\":true,\"status\":[]}"
* the response status code should be "422"
* the response should contain validation error for field "title"
* the response should contain validation error for field "description"
* the response should contain validation error for field "status"


## Create task with non-existing field

* I send a POST request to "/tasks" with payload "{\"non_existing_field\":\"value\"}"
* the response status code should be "422"
