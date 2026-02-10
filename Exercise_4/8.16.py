import greetings
greetings.greet_user("Alice")
from greetings import greet_user
greet_user("Bob")

from greetings import greet_user as gu
gu("Josh")

import greetings as gr
gr.greet_user("Jacob")

from greetings import *
greet_user("Eve")
