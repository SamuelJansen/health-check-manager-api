from python_framework import SqlAlchemyProxy as sap
from python_framework import ConverterStatic
from ModelAssociation import MODEL, ENVIRONMENT

from constant import EnvironmentConstant

class Environment(MODEL):
    __tablename__ = ENVIRONMENT

    id = sap.Column(sap.Integer(), sap.Sequence(f'{__tablename__}{sap.ID}{sap.SEQ}'), primary_key=True)
    key = sap.Column(sap.String(256), unique=True, nullable=False)
    name = sap.Column(sap.String(32), default=EnvironmentConstant.DEFAULT_ENVIRONMENT_NAME)
    apiKey = sap.Column(sap.String(128), nullable=False)
    healthUrl = sap.Column(sap.String(512), nullable=False)
    apiName = sap.Column(sap.String(128), nullable=False)

    def __init__(self,
        id = None,
        key = None,
        name = None,
        apiKey = None,
        healthUrl = None,
        apiName = None
    ):
        self.id = id
        self.key = key
        self.name = ConverterStatic.getValueOrDefault(name, EnvironmentConstant.DEFAULT_ENVIRONMENT_NAME)
        self.apiKey = apiKey
        self.healthUrl = healthUrl
        self.apiName = apiName


    def __repr__(self):
        return f'{self.__tablename__}(id={self.id}, key={self.key}, apiName={self.apiName}, name={self.name}, apiKey={self.apiKey})'
