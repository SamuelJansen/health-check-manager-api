from converter.static import SpeakConverterStatic

class SpeakRequestDto:
    def __init__(self,
        text = None,
        path = None,
        name = None,
        extension = None
    ):
        self.text = text
        self.path = path
        self.name = SpeakConverterStatic.getValidName(name)
        self.extension = extension
        SpeakConverterStatic.toRequestDto(self)

class SpeakResponseDto:
    def __init__(self,
        key = None,
        text = None,
        path = None,
        name = None,
        extension = None,
        staticFileCreatedAt = None,
        staticUrl = None,
        duration = None
    ):
        self.key = key
        self.text = text
        self.path = path
        self.name = SpeakConverterStatic.getValidName(name)
        self.extension = extension
        self.staticFileCreatedAt = staticFileCreatedAt
        self.staticUrl = staticUrl
        self.duration = duration
