from flask_appbuilder.models.mixins import AuditMixin, BaseMixin, FileColumn, ImageColumn
from sqlalchemy import Table, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from flask_appbuilder import Base
from flask_appbuilder.security.models import User
from flask_appbuilder import Base

"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""

class Project(AuditMixin, Base):
    id = Column(Integer, primary_key=True)
    name =  Column(String(150), unique = True, nullable=False)
    
class ProjectFiles(Base):
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('project.id'))
    project = relationship("Project")
    file = Column(FileColumn, nullable=False)
    
