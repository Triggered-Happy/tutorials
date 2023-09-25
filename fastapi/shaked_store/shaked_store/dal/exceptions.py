class DataSourceException(Exception):
    ...


class NonExistingItemException(DataSourceException):
    ...


class ExistingItemException(DataSourceException):
    ...
