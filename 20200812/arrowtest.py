import arrow

now = arrow.utcnow()
seoulTime = now.to("Asia/Seoul")
print(seoulTime)
