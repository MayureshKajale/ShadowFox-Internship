def do_jumping_jacks():
    total_jumping_jacks = 100
    jumping_jacks_done = 0

    while jumping_jacks_done < total_jumping_jacks:
        remaining_jacks = total_jumping_jacks - jumping_jacks_done
        print(f"You have {remaining_jacks} jumping jacks remaining.")
        print("1 set of jumping jacks done of 10......")
        for _ in range(10):
            jumping_jacks_done += 1
            if jumping_jacks_done >= total_jumping_jacks:
                print("Congratulations! You completed the workout.")
                return

        tired = input("Are you tired? (yes/no): ").lower()
        if tired == "yes" or tired == "y":
            skip_remaining_sets = input("Do you want to skip the remaining sets? (yes/no): ").lower()
            if skip_remaining_sets == "yes" or skip_remaining_sets == "y":
                print(f"You completed a total of {jumping_jacks_done} jumping jacks.")
                return
        else:
            continue

    print("Congratulations! You completed the workout.")

do_jumping_jacks()
