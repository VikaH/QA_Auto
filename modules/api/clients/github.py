import requests


class GitHub:

    # def get_user_defunkt(self):
    #     r = requests.get('https://api.github.com/users/defunkt')
    #     body = r.json()

    #     return body

    # def get_non_exist_user(self):
    #     r = requests.get('https://api.github.com/users/butenkosergii')
    #     body = r.json()

    #     return body
    # Перша версія пошуку існуючого та неіснуючого юзера


    def get_user(self,username):
        r = requests.get(f'https://api.github.com/users/{username}')
        body = r.json()

        return body
    
    def search_repo(self,name):
        r = requests.get(
            "https://api.github.com/search/repositories",
            params={"q" : name}
            )
        body = r.json()

        return body
    
    def get_emojis(self):
        r = requests.get('https://api.github.com/emojis')

        body = r.json()
        return body
    
    def check_emojis(self, emojis_name):
        all_emojis = self.get_emojis()
        
        # if emojis_name in all_emojis:
        #     return True
        # else:
        #     return False
        return emojis_name in all_emojis
    
    def get_branches(self, owner, repo):
        r = requests.get(f'https://api.github.com/repos/{owner}/{repo}/branches')

        body = r.json()
        return body