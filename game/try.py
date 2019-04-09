"""Persistent object and data manager for departments.

Version: %A%"""

import sybaseDataServer
import persistentDM
import persistentPD

class Department (persistentPD.PersistentPD):
    """Persistent department."""

    def __init__ (self,
                  departmentID = None,
                  deptCode = None,
                  name = None,
                  managerID = None,
                  inDatabase = 0, changed = 0):
        """Initialize a department with optional initial values."""
        self.departmentID = departmentID
        self.deptCode = deptCode
        self.name = name
        self.mission = persistentPD.LongField ("mission", self)
        self.managerID = managerID
        self.manager = None
        self.roster = None
        persistentPD.PersistentPD.__init__ (self, inDatabase, changed)

    def getID (self):
        """Return a unique ID value."""
        return self.departmentID

    def getDepartmentID (self):
        """Get the unique id."""
        return self.departmentID

    def updateDeptCode (self, newValue):
        """Try to update the department code."""
        self.updateValue ("deptCode", newValue)

    def getDeptCode (self):
        """Get the department code."""
        return self.deptCode

    def updateName (self, newValue):
        """Try to update the name."""
        self.updateValue ("name", newValue)

    def getName (self):
        """Get the name."""
        return self.name

    def updateMission (self, newValue):
        """Try to update the mission statement."""
        self.mission.updateValue (newValue)

    def getMission (self):
        """Get the mission statement."""
        return self.mission.getValue ()

    def updateManager (self, newValue):
        """Try to update the manager."""
        self.updateObjectValue ("manager", "managerID", newValue)

    def getManager (self):
        """Get the manager."""
        if self.manager == None and self.managerID != None:
            dataManager = self.getDataManagerForClass ("Employee")
            self.manager = dataManager.getByID (self.managerID)
        return self.manager

    def getRoster (self):
        """Get the employee roster."""
        if self.roster == None:
            dataManager = self.getDataManagerForClass ("Employee")
            self.roster = dataManager.getAllByDepartmentID (self.departmentID)
        return self.roster

    def addToRoster (self, theEmployee):
        """Add the Employee to the employee roster."""
        self.getRoster ().append (theEmployee)

    def deleteFromRoster (self, theEmployee):
        """Delete the Employee from the employee roster."""
        self.getRoster ().remove (theEmployee)

    def delete (self):
        """Delete myself and all my list items."""
        for anObject in getRoster ():
            anObject.delete ()
        persistentPD.PersistentPD.delete (self)

    def refresh (self):
        """Refresh the a department with the latest values from the database."""
        if self.dataManager.refreshShortFields (self):
            self.mission.refresh ()
            self.roster = None
            self.manager = None

    def save (self):
        """Save the a department in the database."""
        self.dataManager.save (self)
        self.mission.save ()

def new (deptCode = None,
        name = None,
        managerID = None,
        mission = None):
    """Create and save a department with optional initial values."""
    newDepartment = Department (None,
                        deptCode,
                        name,
                        managerID, 0, 1)
    newDepartment.updateMission (None)
    newDepartment.save ()
    newDepartment.updateMission (mission)
    newDepartment.save ()
    return newDepartment


class DepartmentDataManager (persistentDM.DataManager):
    """Manager of departments in the database."""

    def createTable (self):
        """Create a database table to hold departments ."""
        self.server.sql ("""create table Department (
                departmentID numeric (8, 0) identity not null,
                deptCode int,
                name varchar (50),
                mission text null,
                managerID numeric (8, 0) null)""")

    def insert (self, anObject):
        """Insert a new department into the database."""
        lock = self.server.acquireLock ()
        self.server.sql ("""insert Department (
                        deptCode,
                        name,
                        managerID)
                values (%s, %s, %s)""" % ( \
                        self.sqlInt (anObject.deptCode),
                        self.sqlString (anObject.name),
                        self.sqlInt (anObject.managerID),
                ))
        anObject.departmentID = self.server.getIdentity ()
        anObject.setInDatabase ()

    def update (self, anObject):
        """Update an existing department in the database."""
        self.server.sql ("""update Department
                set        deptCode = %s,
                        name = %s,
                        managerID = %s
                where departmentID = %d""" \
                % ( \
                        self.sqlInt (anObject.deptCode),
                        self.sqlString (anObject.name),
                        self.sqlInt (anObject.managerID),
                        anObject.departmentID
                ))

    def delete (self, anObject):
        """Delete a department from the database."""
        self.server.sql ("""delete Department where departmentID = %d""" % anObject.departmentID)

    def refreshShortFields (self, anObject):
        """Refresh short fields of a department."""
        lock = self.server.acquireLock ()
        self.server.sql (self.sqlSelect () + "where departmentID = %d" % anObject.departmentID)
        rowTuple = self.server.resultRow ()
        if not rowTuple:
            return 0
        ignoredIDfield, \
            anObject.deptCode, \
            anObject.name, \
            anObject.managerID = rowTuple
        if anObject.managerID != None:
            anObject.managerID = int (anObject.managerID)
        anObject.changed = 0
        return 1

    def getLongFieldValue (self, id, fieldName):
        """Get a long field value, given an id number."""
        lock = self.server.acquireLock ()
        self.server.sql ("""select %s from Department where departmentID = %d""" % (fieldName, id))
        value, = self.server.resultRow ()
        return value

    def saveLongFieldValue (self, id, fieldName, value):
        """Save a long field value, given an id number."""
        self.server.writeLong ("Department", "departmentID", id, fieldName, value)

    def retrieveByID (self, id):
        """Get a department by its ID number."""
        return self.getOne ("where departmentID = %d" % id)

    def getAllSortedBySample (self):
        """Get a list of all departments sorted by some fields."""
        return self.getAll ("order by departmentID, deptCode, name")

    def getAllSortedForList (self):
        """Get a list of all departments sorted for a selection list."""
        return self.getAllSortedBySample ()

    def getAllByManagerID (self, managerID):
        """Get a list of all departments matching the manager ID."""
        return self.getAll ("where managerID = %d" % managerID)

    def sqlSelect (self):
        """Return an SQL "Select ... From ..." clause for retrieving a department."""
        return """select x.departmentID,
                 x.deptCode,
                 x.name,
                 x.managerID from Department x """

    def rowToObject (self, rowTuple):
        """Convert a database row tuple to a department."""
        if rowTuple:
            departmentID, \
                deptCode, \
                name, \
                managerID = rowTuple
            if managerID != None:
                managerID = int (managerID)
            newDepartment = Department (int (departmentID),
                                        deptCode,
                                        name,
                                        managerID, 1, 0)
            return self.cachedObject (newDepartment)
        else:
            return None

DepartmentDM = DepartmentDataManager (sybaseDataServer.DMserver, Department)