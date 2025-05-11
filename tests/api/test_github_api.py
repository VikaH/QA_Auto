import pytest
# from modules.api.clients.github import GitHub


# @pytest.mark.api
# def test_user_exists():
#     api = GitHub()
#     user = api.get_user_defunkt()
#     assert user['login'] == 'defunkt'

    
# @pytest.mark.api
# def test_user_not_exists():
#     api = GitHub()
#     r = api.get_non_exist_user()
#     assert r['message'] == 'Not Found' 
# Перша версія пошуку існуючого та неіснуючого юзера,для порівняння тести 
# з 19 по 28 рядок більш лаконічні і правильні   

@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'

# користувач може знайти існуючій репозиторійій на ГітХАбі
@pytest.mark.api 
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')  

    assert r['total_count'] == 57
    assert 'become-qa-auto' in r['items'][0]['name']

# користувач може знайти неіснуючій реп ій на ГітХАбі
@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0

# користувач може знайти репозиторій на ГітХАбі ім я якого один символ
@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0

# Отримати список усіх Emoji
@pytest.mark.api
def test_get_all_available_emoji(github_api):
    r = github_api.get_emojis()

    assert r['alarm_clock'] == 'https://github.githubassets.com/images/icons/emoji/unicode/23f0.png?v8'
    assert r['hippopotamus'] == 'https://github.githubassets.com/images/icons/emoji/unicode/1f99b.png?v8'
    assert r['beers'] == 'https://github.githubassets.com/images/icons/emoji/unicode/1f37b.png?v8'


# Перевірити наявність Emoji на ГітХаб
@pytest.mark.api
def test_check_emoji_exists(github_api):
    r = github_api.check_emojis('beetle')

    assert r == True


# Перевірити відсутність Emoji на ГітХаб
@pytest.mark.api
def test_check_emoji_absence(github_api):
    r = github_api.check_emojis('ghjkhiuh')

    assert r == False

#Перевірка наявності в репозиторіі гілки main
@pytest.mark.api
def test_repo_has_main_branch(github_api):
    r = github_api.get_branches('VikaH', 'QA_Auto')

    assert r[0]['name'] == 'main'

#Перевірка наявності в репозиторіі гілки master
@pytest.mark.api
def test_repo_has_master_branch(github_api):
    r = github_api.get_branches('noJokesCoder', 'project_final')

    assert r[0]['name'] == 'master'


