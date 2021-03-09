# Shared state
currently_running_instances = set()


# Web-Tier
IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif']

# SQS
REQUEST_QUEUE = "Request-Queue"
RESPONSE_QUEUE = "Response-Queue"
MAX_NUMBER_OF_MSGS_TO_FETCH = 5
WAIT_TIME_SECONDS = 3

# EC2
AMI_ID = "ami-0ee8cf7b8a34448a6"
EC2_KEY_PAIR = "rizz_key_pair"
SECURITY_GROUP_NAME = ["AllowSSH"]
INSTANCE_TYPE = "t2.micro"
APP_SERVER_NAME = "App-Server"
MIN_POSSIBLE_INSTANCES = 1
MAX_POSSIBLE_INSTANCES = 3
MAX_REQUESTS_PER_INSTANCE = 1

# S3
INPUT_BUCKET = "cse546-input-bucket"
OUTPUT_BUCKET = "cse546-output-bucket"
