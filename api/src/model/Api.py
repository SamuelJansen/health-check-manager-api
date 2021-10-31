from python_framework import SqlAlchemyProxy as sap
from python_framework import ConverterStatic
from ModelAssociation import MODEL, API

from constant import ApiConstant

class Api(MODEL):
    __tablename__ = API

    id = sap.Column(sap.Integer(), sap.Sequence(f'{__tablename__}{sap.ID}{sap.SEQ}'), primary_key=True)
    environmentKey = sap.Column(sap.String(256), unique=True, nullable=False)
    environment = sap.Column(sap.String(32), default=ApiConstant.DEFAULT_API_ENVIRONMENT)
    key = sap.Column(sap.String(128), nullable=False)
    healthUrl = sap.Column(sap.String(512), nullable=False)
    name = sap.Column(sap.String(128), nullable=False)

    def __init__(self,
        id = None,
        environmentKey = None,
        environment = None,
        key = None,
        healthUrl = None,
        name = None
    ):
        self.id = id
        self.environmentKey = environmentKey
        self.environment = ConverterStatic.getValueOrDefault(environment, ApiConstant.DEFAULT_API_ENVIRONMENT)
        self.key = key
        self.healthUrl = healthUrl
        self.name = name


    def __repr__(self):
        return f'{self.__tablename__}(id={self.id}, environmentKey={self.environmentKey}, name={self.name}, environment={self.environment}, key={self.key})'
