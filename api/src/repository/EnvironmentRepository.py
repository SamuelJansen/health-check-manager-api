from python_helper import ObjectHelper
from python_framework import SqlAlchemyProxy as sap
from python_framework import Repository

from model import Environment

@Repository(model = Environment.Environment)
class EnvironmentRepository:

    def findAll(self) :
        return self.repository.findAllAndCommit(self.model)

    def existsById(self, id) :
        return self.repository.existsByIdAndCommit(id, self.model)

    def findById(self, id) :
        if self.existsById(id) :
            return self.repository.findByIdAndCommit(id, self.model)

    def existsByKey(self, key) :
        return self.repository.existsByKeyAndCommit(key, self.model)

    def existsByApiKeyAndCreatedAtAfter(self, apiKey, afterDateTime) :
        exists = self.repository.session.query(sap.exists().where(
            sap.and_(
                self.model.apiKey == apiKey,
                self.model.createdAt >= afterDateTime
            )
        )).one()[0]
        self.repository.session.commit()
        return exists

    def findByKey(self, key) :
        if self.existsByKey(key) :
            return self.repository.findByKeyAndCommit(key, self.model)

    def findByName(self, name) :
        if self.existsByName(name) :
            model = self.repository.session.query(self.model).filter(self.model.name == name).order_by(self.model.id.desc()).first()
            self.repository.session.commit()
            return model

    def notExistsById(self, id) :
        return not self.existsById(id)

    def save(self, model) :
        return self.repository.saveAndCommit(model)

    def saveAll(self, modelList):
        return self.repository.saveAllAndCommit(modelList)

    def deleteById(self, id):
        self.repository.deleteByIdAndCommit(id, self.model)

    def findAllByApiKeyAndCreatedAtAfterOrderedByCreatedAtDescendent(self, apiKey, createdAt) :
        modelList = self.repository.session.query(self.model).filter(
            sap.and_(
                self.model.apiKey == apiKey,
                self.model.createdAt >= createdAt
            )
        ).order_by(self.model.createdAt.desc()).all()
        self.repository.session.commit()
        return modelList

    def findAllByIdIn(self, idList) :
        modelList = self.repository.session.query(self.model).filter(self.model.id.in_(idList)).all()
        self.repository.session.commit()
        return modelList

    def findMostRecentByApiKey(self, apiKey) :
        model = self.repository.session.query(self.model).filter(self.model.apiKey == apiKey).order_by(self.model.id.desc()).first()
        self.repository.session.commit()
        return model

    def findAllByKey(self, key):
        modelList = self.repository.session.query(self.model).filter(self.model.key == key).all()
        self.repository.session.commit()
        return modelList

    def findAllByApiKey(self, apiKey):
        modelList = self.repository.session.query(self.model).filter(self.model.apiKey == apiKey).all()
        self.repository.session.commit()
        return modelList

    def findAllByName(self, name):
        modelList = self.repository.session.query(self.model).filter(self.model.name == name).all()
        self.repository.session.commit()
        return modelList

    def findAllByApiKeyAndName(self, key, name):
        modelList = self.repository.session.query(self.model).filter(
            sap.and_(
                self.model.key == key,
                self.model.name == name
            )
        ).all()
        self.repository.session.commit()
        return modelList

    def findAllByQuery(self, query):
        return self.repository.findAllByQueryAndCommit({k:v for k,v in query.items() if ObjectHelper.isNotNone(v)}, self.model)

    def findByApiKeyAndName(self, key, name):
        modelList = self.repository.session.query(self.model).filter(
            sap.and_(
                self.model.key == key,
                self.model.name == name
            )
        ).order_by(self.model.id.desc()).first()
        self.repository.session.commit()
        return modelList

    def existsByApiKey(self, apiKey):
        exists = self.repository.session.query(sap.exists().where(self.model.apiKey == apiKey)).one()[0]
        self.repository.session.commit()
        return exists

    def existsByName(self, name):
        exists = self.repository.session.query(sap.exists().where(self.model.name == name)).one()[0]
        self.repository.session.commit()
        return exists

    def existsByApiKeyAndName(self, key, name):
        exists = self.repository.session.query(sap.exists().where(
            sap.and_(
                self.model.key == key,
                self.model.name == name
            )
        )).one()[0]
        self.repository.session.commit()
        return exists

    def existsByKeyIn(self, keyList) :
        # condition = sap.or_(False, False)
        # for key in keyList:
        #     condition = sap.or_(
        #         condition,
        #         self.model.key == key
        #     )
        exists = self.repository.session.query(sap.exists().where(self.model.key.in_(keyList))).one()[0]
        self.repository.session.commit()
        return exists

    def existsByApiKeyIn(self, apiKeyList) :
        # condition = sap.or_(False, False)
        # for apiKey in apiKeyList:
        #     condition = sap.or_(
        #         condition,
        #         self.model.apiKey == apiKey
        #     )
        exists = self.repository.session.query(sap.exists().where(self.model.apiKey.in_(apiKeyList))).one()[0]
        self.repository.session.commit()
        return exists
