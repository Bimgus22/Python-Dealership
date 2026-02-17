from datetime import datetime, timedelta

now = datetime.now()
print("Current date and time:", now)

future = now + timedelta(days=7)
print("One week from now:", future)

formatted = now.strftime("%B %d, %Y")
print("Formatted date:", formatted)