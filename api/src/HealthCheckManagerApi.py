from python_framework import ResourceManager
import ModelAssociation

api, app, jwt = ResourceManager.initialize(__name__, ModelAssociation.MODEL)
