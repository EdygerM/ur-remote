# UR Dashboard
A library in progress to control a Universal Robot using the Dashboard server

### Installation
``
pip install ur-dashboard
``

### Get started
```Python
from ur_dashboard import URDashboard

robot1 = URDashboard("127.0.0.1")

print(robot1.connect())
```