extends Node2D # change to your Node Type

# 
# Godot Script to connect to this backend
# 
# SAMPLE USE:
# Attach this script to a node in your scene, name it "Backend" or whatever you like. Call it from other scenes ($Backend.flow)
# 
# func _ready():
# 	var params = {
# 			"token": "111",
# 			"newuser": {
# 				"username": "user10",
# 				"name": "User10",
# 				"email": "user10@test.com"
# 			}
# 		}
# 	$Backend.flow("Get home data now!!", params, _callback_flow)
# 
# func _callback_flow(result, response_code, headers, body):
# 	print("_callback_flow")
# 	print(result)
# 	print(response_code)
# 	print(headers)
# 	print(body)
	


# Set in editor
@export var backend_url: String = "http://127.0.0.1:5000"
@export var app_token: String = ""

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass


func flow(flowname: String, params = {}, callback: Callable = self._on_request_flow_completed_default):
	var headers = [
		"Content-Type: application/json",
		#"Authorization: Bearer " + app_token  # Replace with your token if needed
	]
	var body = {
		"flow": flowname,
		"params": params
	}
	var json = JSON.new()
	var body_json = json.stringify(body)
	
	var req = HTTPRequest.new()
	add_child(req)
	req.request_completed.connect(callback)
	var err = req.request(backend_url + "/flow", headers, HTTPClient.METHOD_POST, body_json)

func _on_request_flow_completed_default(result, response_code, headers, body):
	var json = JSON.parse_string(body.get_string_from_utf8())
	print("-------")
	print("_on_request_flow_completed_default")
	print(json)
	print("-------")
	pass
