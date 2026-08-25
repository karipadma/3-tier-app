2. Frontend — index.html

Your HTML can remain almost exactly the same. The only important change is the API_URL.

Change:

const API_URL = "http://BACKEND_PUBLIC_IP:5000";  - This is for aws ec2s

to:

const API_URL = "/api"; - This is docker containers
