"""
grey User Database
"""
import motor

from grey.config import MONGODB

mongodb = motor.MotorClient(MONGODB).grey
