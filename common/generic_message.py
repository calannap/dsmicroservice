from jsonizable import Jsonizable


class GenericMessage(Jsonizable):
    
    def __init__(self, json):
        super(GenericMessage, self).__init__(json=json)


    # def __init__(self, metadata_type, message):
    #     self.metadata_type = metadata_type
    #     self.message = message

    class Meta:
        schema = dict(
            metadata_type=str,
            message=dict
        )



