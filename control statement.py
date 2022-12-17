watches = ["ok", "ok", "ok", "faulty", "ok", "ok"]
# for status in watches:
#     if status == "faulty":
#         print("Stoping the production line")
#         break
#     print(f"This watch is {status}")
# for status in watches:
#     if status == "faulty":
#         print("Found faulty watch, skipping ...")
#         continue
#     print(f"This watch is {status}")
# for status in watches:
#     pass

for i in range(3) :
    x = input("Enter your password : ").lower()
    if x == "cheikh12":
        print("Correct password")
        break
    if i == 2:
        print("No more attempts")
        break
    print("not Correct password")

    
    