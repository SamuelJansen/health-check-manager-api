from python_helper import ObjectHelper
from python_framework import SqlAlchemyProxy as sap
from python_framework import Repository

from model import Api

@Repository(model = Api.Api)
class ApiRepository:

    def findAll(self) :
        return self.repository.findAllAndCommit(self.model)

    def existsById(self, id) :
        return self.repository.existsByIdAndCommit(id, self.model)

    def findById(self, id) :
        if self.existsById(id) :
            return self.repository.findByIdAndCommit(id, self.model)

    def existsByKey(self, key) :
        return self.repository.existsByKeyAndCommit(key, self.model)

    def existsByKeyAndCreatedAtAfter(self, key, afterDateTime) :
        exists = self.repository.session.query(sap.exists().where(
            sap.and_(
                self.model.key == key,
                self.model.createdAt >= afterDateTime
            )
        )).one()[0]
        self.repository.session.commit()
        return exists

    def findByKey(self, key) :
        if self.existsByKey(key) :
            return self.repository.findByKeyAndCommit(key, self.model)

    def findByEnvironmentKey(self, environmentKey) :
        if self.existsByEnvironmentKey(environmentKey) :
            model = self.repository.session.query(self.model).filter(self.model.environmentKey == environmentKey).order_by(self.model.id.desc()).first()
            self.repository.session.commit()
            return model

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

    def findAllByKeyAndCreatedAtAfterOrderedByCreatedAtDescendent(self, key, createdAt) :
        modelList = self.repository.session.query(self.model).filter(
            sap.and_(
                self.model.key == key,
                self.model.createdAt >= createdAt
            )
        ).order_by(self.model.createdAt.desc()).all()
        self.repository.session.commit()
        return modelList

    def findAllByIdIn(self, idList) :
        modelList = self.repository.session.query(self.model).filter(self.model.id.in_(idList)).all()
        self.repository.session.commit()
        return modelList

    def findMostRecentByKey(self, key) :
        model = self.repository.session.query(self.model).filter(self.model.key == key).order_by(self.model.id.desc()).first()
        self.repository.session.commit()
        return model

    def findAllByKey(self, key):
        modelList = self.repository.session.query(self.model).filter(self.model.key == key).all()
        self.repository.session.commit()
        return modelList

    def findAllByEnvironment(self, environment):
        modelList = self.repository.session.query(self.model).filter(self.model.environment == environment).all()
        self.repository.session.commit()
        return modelList

    def findAllByKeyAndEnvironment(self, key, environment):
        modelList = self.repository.session.query(self.model).filter(
            sap.and_(
                self.model.key == key,
                self.model.environment == environment
            )
        ).all()
        self.repository.session.commit()
        return modelList

    def findAllByQuery(self, query):
        return self.repository.findAllByQueryAndCommit(query, self.model)

    def findByKeyAndEnvironment(self, key, environment):
        modelList = self.repository.session.query(self.model).filter(
            sap.and_(
                self.model.key == key,
                self.model.environment == environment
            )
        ).order_by(self.model.id.desc()).first()
        self.repository.session.commit()
        return modelList

    def existsByEnvironmentKey(self, environmentKey) :
        exists = self.repository.session.query(sap.exists().where(self.model.environmentKey == environmentKey)).one()[0]
        self.repository.session.commit()
        return exists

    def existsByName(self, name) :
        exists = self.repository.session.query(sap.exists().where(self.model.name == name)).one()[0]
        self.repository.session.commit()
        return exists

    def existsByEnvironment(self, environment):
        exists = self.repository.session.query(sap.exists().where(self.model.environment == environment)).one()[0]
        self.repository.session.commit()
        return exists

    def existsByKeyAndEnvironment(self, key, environment):
        exists = self.repository.session.query(sap.exists().where(
            sap.and_(
                self.model.key == key,
                self.model.environment == environment
            )
        )).one()[0]
        self.repository.session.commit()
        return exists

    def existsByEnvironmentKeyIn(self, environmentKeyList) :
        existenceCondition = sap.or_(False, False)
        for environmentKey in environmentKeyList:
            existenceCondition = sap.or_(
                self.model.environmentKey == environmentKey
            )
        exists = self.repository.session.query(sap.exists().where(existenceCondition)).one()[0]
        self.repository.session.commit()
        return exists

    def existsByKeyIn(self, keyList) :
        condition = sap.or_(False, False)
        for key in keyList:
            condition = sap.or_(
                self.model.key == key
            )
        exists = self.repository.session.query(sap.exists().where(condition)).one()[0]
        self.repository.session.commit()
        return exists
