justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

num_members = len(justice_league)
print(f"Number of members: {num_members}")

justice_league.extend(["Batgirl", "Nightwing"])
print("After adding Batgirl and Nightwing:", justice_league)

justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("After moving Wonder Woman to the beginning:", justice_league)

justice_league.remove("Green Lantern")
justice_league.insert(justice_league.index("Aquaman") + 1, "Green Lantern")
print("After moving Green Lantern between Aquaman and Flash:", justice_league)

justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("After replacing with new members:", justice_league)

justice_league.sort()
print("After sorting alphabetically:", justice_league)
print(f"The new leader is: {justice_league[0]}")
