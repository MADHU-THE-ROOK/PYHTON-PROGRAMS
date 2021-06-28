import instaloader as insta

mod= insta.Instaloader()

user=input("enter username: ")

mod.download_profile(user,profile_pic_only=True)
