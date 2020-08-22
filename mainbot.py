import tweepy
import time
def emoji_follower_count(user):
    emoji_numbers = {0: "0️⃣", 1: "1️⃣", 2: "2️⃣", 3: "3️⃣",
                     4: "4️⃣", 5: "5️⃣", 6: "6️⃣", 7: "7️⃣", 8: "8️⃣", 9: "9️⃣"}

    follower_count_list = [int(i) for i in str(user.followers_count)]

    emoji_followers = ''.join([emoji_numbers[k]
                               for k in follower_count_list if k in emoji_numbers.keys()])

    return emoji_followers # FOLLOWERS IN SMILEYS



def main():
    api = create_api()

    while True:
        # change to your own twitter_handle
        user = api.get_user('the_ameen_manna')

        api.update_profile(name=f'aMEEr|{emoji_follower_count(user)} Followers')
        print(f'Updating twitter profile: {emoji_follower_count(user)}')
        print("Waiting to refresh..")
        time.sleep(60)


main()
