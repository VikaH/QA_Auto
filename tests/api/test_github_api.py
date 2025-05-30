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
# The first version of the search for existing and non-existing users, for comparison tests 
# lines 20 to 28 are more concise and correct  

@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'

# user can find existing repository on GitHub
@pytest.mark.api 
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')  

    assert r['total_count'] == 57
    assert 'become-qa-auto' in r['items'][0]['name']

# user can find a non-existent repo on GitHub
@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0

# user can find a repository on GitHub whose name is one character
@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0

# Get a list of all Emoji
@pytest.mark.api
def test_get_all_available_emoji(github_api):
    r = github_api.get_emojis()

    assert r['alarm_clock'] == 'https://github.githubassets.com/images/icons/emoji/unicode/23f0.png?v8'
    assert r['hippopotamus'] == 'https://github.githubassets.com/images/icons/emoji/unicode/1f99b.png?v8'
    assert r['beers'] == 'https://github.githubassets.com/images/icons/emoji/unicode/1f37b.png?v8'


# Check for Emoji on GitHub
@pytest.mark.api
def test_check_emoji_exists(github_api):
    r = github_api.check_emojis('beetle')

    assert r == True


# Check for missing Emoji on GitHub
@pytest.mark.api
def test_check_emoji_absence(github_api):
    r = github_api.check_emojis('ghjkhiuh')

    assert r == False

# Checking the presence of the main branch in the repository
@pytest.mark.api
def test_repo_has_main_branch(github_api):
    r = github_api.get_branches('VikaH', 'QA_Auto')

    assert r[0]['name'] == 'main'

# Checking the presence of the master branch in the repository
@pytest.mark.api
def test_repo_has_master_branch(github_api):
    r = github_api.get_branches('noJokesCoder', 'project_final')

    assert r[0]['name'] == 'master'



