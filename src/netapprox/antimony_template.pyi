from typing import Generic, TypeVar, List, Optional, Any
T = TypeVar('T')


class AntimonyTemplate(Generic[T]):

    def __init__(self, antimony: str)->None: ...

    def initialize(self)->tuple[str, str]: ...

    def _extractModelName(self, line: str)->str: ...

    def _findMainModelName(self)->str: ...
    
    def copy(self)->AntimonyTemplate: ...
    
    def __repr__(self)->str: ...
    
    def setTemplateVariable(self, var_name: str, value: str)->None: ...

    def makeModularModel(self)->None: ...

    def isValidAntimony(self)->bool: ...

    @staticmethod
    def makeSubmodelTemplateName(idx: int)->str: ...