from python_framework import SqlAlchemyProxy as sap
from python_framework import ConverterStatic
from ModelAssociation import MODEL, API

from constant import ApiConstant

class Api(MODEL):
    __tablename__ = API

    id = sap.Column(sap.Integer(), sap.Sequence(f'{__tablename__}{sap.ID}{sap.SEQ}'), primary_key=True)
    key = sap.Column(sap.String(128), unique=True, nullable=False)
    environment = sap.Column(sap.String(32), default=ApiConstant.DEFAULT_API_ENVIRONMENT)
    healthUrl = sap.Column(sap.String(512), nullable=False)
    name = sap.Column(sap.String(128), nullable=False)

    def __init__(self,
        id = None,
        key = None,
        healthUrl = None,
        environment = None,
        name = None
    ):
        self.id = id
        self.key = key
        self.healthUrl = healthUrl
        self.environment = ConverterStatic.getValueOrDefault(environment, ApiConstant.DEFAULT_API_ENVIRONMENT)
        self.name = name


    def __repr__(self):
        return f'{self.__tablename__}(id={self.id}, key={self.key}, name={self.name}, type={self.type})'
