import requests

def main():
    username = input("Enter your username: ")
    user = get_user(username)

    for name, link in user:
        print(name, link)

def get_data(mode, username):
    loop = True
    iteration = 1
    data = []
    while loop == True:
        followers_api = requests.get(
            'https://api.github.com/users/'+username+'/' + mode + '?page='+str(iteration))
        followers_json = followers_api.json()

        for f in range(len(followers_json)):
            data.append((followers_json[f]['login'], followers_json[f]['html_url']))
        iteration += 1
        if not followers_json:
            break
    
    return data

def get_user(username):
    followers = get_data('followers', username)
    following = get_data('following', username)
    user = list(set(following) - set(followers))
    return user

if __name__ == "__main__":
    main()