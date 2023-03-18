from typing import Dict, List, Optional, Union

from revChatGPT.V1 import Chatbot 

from .model import Model

class ChatGPT(Model):
    name = "ChatGPT"
    description = "Reverse engineered ChatGPT model for text completion"

    def __init__(self, config: Dict[str, str], model: str = "gpt-4"):
        """
        Initialize the ChatGPT model given the browser login config and model
        config:
            is a Dict type, and has the following keys:

            - "email": OpenAI account email.
            - "password": OpenAI account password.
            - "session_token": Session token used by ChatGPT
            - "access_token": Access token used by ChatGPT, can be obtained by viewing 
                              https://chat.openai.com/api/auth/session
            - "proxy": "...", 
            - "paid": Whether the account is plus (paid) or not.

        model:
            "gpt-4" only at this moment. For other option, please use openAI GPT API.

        More details on these are available at https://github.com/acheong08/ChatGPT#configuration
        """

        assert model in self.list_models(), "model not supported"

        self.model = model

        config["model"] = self.model
        self._config = config
        model_args = {}
        
        self.chartbot_variables = model_args



    def list_models(self):
        return ["gpt-4"]
    
    def run(
        self, 
        prompts: Union[str, List[str]],
        conversation_id: Optional[str] = None,
        parent_id: Optional[str] = None,
        session_client = None,
        lazy_loading: bool = False,
        collect_data: bool = False
    ) -> List[str]:
        """
        prompts: The prompt(s) to generate completions for, encoded as a string, array of strings, 
                 array of tokens, or array of token arrays.
        conversation_id: Id of the conversation to continue on. Defaults to None.
        parent_id: Id of the previous response message to continue on. Defaults to None.
        session_client (_type_, optional): _description_. Defaults to None.


        """
        chatbot = Chatbot(config = self._config,
                          conversation_id = conversation_id,
                          parent_id = parent_id,
                          session_client = session_client,
                          lazy_loading = lazy_loading,
                          collect_data = collect_data)
        
        result = []

        for prompt in prompts:
            data = {} 
            for info in chatbot.ask(prompt):
                data['text'] = info["message"]

            result.append(data)

        return result