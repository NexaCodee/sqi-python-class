print("stage1")
confirmed_guest ='Alice, Charlie, Eve, Bob, Frank, Grace, David, Hannah, Liam, Mia'.split(', ')

waitlist = []
waitlist.append("Ken")
waitlist.append("Jack")
waitlist.append("Ivy")
print(f"confirmed guests: {confirmed_guest}\n waitlist: {waitlist}")

waitlist.append("Noah")
waitlist.append("Oliver")
print(f"confirmed guests: {confirmed_guest}\n waitlist: {waitlist}")

confirmed_guest.remove("Alice")
new_confirmed_guest = waitlist.pop(0)
confirmed_guest.append(new_confirmed_guest)
print(f"confirmed guests: {confirmed_guest}\n waitlist: {waitlist}")

is_confirmed = "Charlie" in confirmed_guest
print(f"It is {is_confirmed} that charlie is present")

confirmed_guest.remove("David")
confirmed_guest.remove("Eve")

print(f"confirmed guests: {confirmed_guest}\n waitlist: {waitlist}")

confirmed_guest.append(waitlist.pop(0))
confirmed_guest.append(waitlist.pop(0))

print(f"confirmed guests: {confirmed_guest}\n waitlist: {waitlist}")

waitlist.remove("Oliver")

print(f"confirmed guests: {confirmed_guest}\n waitlist: {waitlist}")


print(f"the last 3 confirmed guests: {"$ ".join(confirmed_guest[-3:])}")

