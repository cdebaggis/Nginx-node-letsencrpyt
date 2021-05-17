import base64
import hashlib
import calendar
import datetime

secret = "secret"
url = "/index.html"

future = datetime.datetime.utcnow() + datetime.timedelta(minutes=60)
expiry = calendar.timegm(future.timetuple())

secure_link = f"{secret}{url}{expiry}".encode('utf-8')

hash = hashlib.md5(secure_link).digest()
base64_hash = base64.urlsafe_b64encode(hash)
str_hash = base64_hash.decode('utf-8').rstrip('=')

print(f"{url}?st={str_hash}&e={expiry}")
