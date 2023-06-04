from enum import Enum
from typing import Union


class BeanieExceptionNames(Enum):
    WRONG_DOCUMENT_UPDATE_STRATEGY = "WrongDocumentUpdateStrategy"
    DOCUMENT_NOT_FOUND = "DocumentNotFound"
    DOCUMENT_ALREADY_CREATED = "DocumentAlreadyCreated"
    DOCUMENT_WAS_NOT_SAVED = "DocumentWasNotSaved"
    COLLECTION_WAS_NOT_INITIALIZED = "CollectionWasNotInitialized"
    MIGRATION_EXCEPTION = "MigrationException"
    REPLACE_ERROR = "ReplaceError"
    STATE_MANAGEMENT_IS_TURNED_OFF = "StateManagementIsTurnedOff"
    STATE_NOT_SAVED = "StateNotSaved"
    REVISION_ID_WAS_CHANGED = "RevisionIdWasChanged"
    NOT_SUPPORTED = "NotSupported"
    MONGODB_VERSION_ERROR = "MongoDBVersionError"
    VIEW_WAS_NOT_INITIALIZED = "ViewWasNotInitialized"
    VIEW_HAS_NO_SETTINGS = "ViewHasNoSettings"
    UNION_HAS_NO_REGISTERED_DOCS = "UnionHasNoRegisteredDocs"
    UNION_DOC_NOT_INITED = "UnionDocNotInited"
    DOC_WAS_NOT_REGISTERED_IN_UNION_CLASS = "DocWasNotRegisteredInUnionClass"
    DEPRECATION = "Deprecation"


class WikiModuleNotFoundError(Exception):
    """
    Exception raised when a WikiModule is not found in the database.

    Attributes:
        wiki_module_id (str): The ID of the requested wiki module that was not found.
    """

    def __init__(self, wiki_module_id: str):
        self.wiki_module_id = wiki_module_id


class WikiModuleDatabaseError(Exception):
    """
    Exception raised when a database error occurs while working with WikiModule.

    Attributes:
        wiki_module_id (str): The ID of the wiki module related to the database error. Left blank if not applicable.
        message (str): A custom error message describing the database error.
    """

    def __init__(
        self,
        wiki_module_id: str = "",
        message: Union[str, BeanieExceptionNames] = "Database error",
    ):
        self.wiki_module_id = wiki_module_id
        self.message = message
