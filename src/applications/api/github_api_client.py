
import requests
from src.config.config import Config 

class GitHubAPIClient:

    def login(self):
        print("DO LOGIN")
    
    def logout(self):
        print("DO LOGOUT")

    def search_topic(self, topic_to_search):
        """
        Get list of found topics
        """
        r = requests.get(url=f"https://{Config.get_property('API_BASE_URL')}/search/topics",
                         headers={"Accept": "application/vnd.github+json",
                                  "X-GitHub-Api-Version": "2022-11-28"
                                  },                       
                        params={
                            'q': topic_to_search
                            }
                        )
        print("Get search topics response Status Code:", r.status_code)
        r.raise_for_status()
        # throw an error if reponse is not 2xx

        # get body
        body = r.json()

        return body["items"]

    


