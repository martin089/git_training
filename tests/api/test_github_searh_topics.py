
def test_search_topics_positive(git_hub_api_cliet):
    """
    This test search for existing topocis in Github
    """

    topic_to_search = 'arduino'
    # search for the topic
    topics_list = git_hub_api_cliet.search_topic(topic_to_search)
    #Validate the repo search results exist really exists
    assert len(topics_list) != 0

def test_search_topics_less_30(git_hub_api_cliet):
    """
    This test search for existing topocis in Github, found topics should be less than 30
    """

    topic_to_search = 'abcd' # there 22 topics in git hub like this
    # search for the topic
    topics_list = git_hub_api_cliet.search_topic(topic_to_search)
    #Validate the repo search results exist really exists
    assert len(topics_list) <= 30

def test_search_topics_negative(git_hub_api_cliet):
    """
    This test search for non existing topocis in Github
    """

    topic_to_search = 'made_up_name_13'
    # search for the topic
    topics_list = git_hub_api_cliet.search_topic(topic_to_search)
    #Validate the repo search results exist really exists
    assert len(topics_list) == 0

