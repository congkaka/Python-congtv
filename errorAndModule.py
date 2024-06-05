try:
  print(1/2)
except (ValueError, ZeroDivisionError) as e:
  print(e)
else:
  print("Success")
finally:
  print("Always run")