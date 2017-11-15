#!/bin/python
"""
The application gives the user the possibility to create a database
of people working in the office. User will have the possibility to 
add, delete and update person data. The data will be stored in a 
separate file that will be saved in folder where application is placed.
User will be able to store following data: First Name, Middle Name, 
Last Name, Email, Phone. Additionally each database entry will get a 
unique ID in order to distinguish between entries.
"""
import wx
import random


class PeopleDatabase(wx.Frame):
    """
    """
    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(PeopleDatabase, self).__init__(*args, **kw)
        self._people = {}

        # create a panel in the frame
        self._pnl = wx.Panel(self)

        # create a People area
        self._peopleStaticBox = wx.StaticBox(self._pnl, wx.ID_ANY, "People",
                                             size=wx.Size(200, 250))
        # people list
        self._peopleList = wx.ListCtrl(self._pnl, size=wx.Size(190, 225),
                                       pos=wx.Point(5, 20),
                                       style=wx.LC_REPORT)
        self._peopleList.InsertColumn(0, ' First Name')
        self._peopleList.InsertColumn(1, ' Last Name')
        self._peopleList.Arrange()

        # create Person Details area
        self._personDetBox = wx.StaticBox(self._pnl, wx.ID_ANY, "Person Details",
                            pos=wx.Point(210, 0), size=wx.Size(400, 250))

        # ID
        wx.StaticText(self._pnl, label="ID", pos=(220, 25))
        self._idEditId = wx.TextCtrl(self._pnl, pos=(300, 20), size=(300, 25))
        self._idEditId.Disable()

        # First Name
        wx.StaticText(self._pnl, label="First Name", pos=(220, 65))
        self._firstNameEditId = wx.TextCtrl(self._pnl, pos=(300, 60), size=(300, 25))

        # Middle Name
        wx.StaticText(self._pnl, label="Middle Name", pos=(220, 105))
        self._middleNameEditId = wx.TextCtrl(self._pnl, pos=(300, 100), size=(300, 25))

        # Last Name
        wx.StaticText(self._pnl, label="Last Name", pos=(220, 145))
        self._lastNameEditId = wx.TextCtrl(self._pnl, pos=(300, 140), size=(300, 25))

        # Email
        wx.StaticText(self._pnl, label="Email", pos=(220, 185))
        self._emailEditId = wx.TextCtrl(self._pnl, pos=(300, 180), size=(300, 25))

        # Phone
        wx.StaticText(self._pnl, label="Phone", pos=(220, 225))
        self._phoneEditId = wx.TextCtrl(self._pnl, pos=(300, 220), size=(300, 25))

        # Delete button
        self._deleteButton = wx.Button(self._pnl, label="Delete", pos=(0, 255))
        # TODO: BUG - Delete button should be disabled (grayed out)
        # when no item is chosen from the People list. Also when
        # starting the application

        # Add button
        self._addButton = wx.Button(self._pnl, label="Add", pos=(210, 255))

        # Update button
        self._updateButton = wx.Button(self._pnl, label="Update", pos=(300, 255))
        self._updateButton.Disable()

        # Save button
        self._saveButton = wx.Button(self._pnl, label="Save", pos=(430, 255))
        self._saveButton.Disable()

        # Load button
        self._loadButton = wx.Button(self._pnl, label="Load", pos=(520, 255))

        # and a status bar
        self.CreateStatusBar()
        self.SetStatusText("ver 1.1")

        # Add events to the buttons
        self._pnl.Bind(wx.EVT_BUTTON, self.on_delete_button, self._deleteButton)
        self._pnl.Bind(wx.EVT_BUTTON, self.on_add_button, self._addButton)
        self._pnl.Bind(wx.EVT_BUTTON, self.on_update_button, self._updateButton)
        self._pnl.Bind(wx.EVT_BUTTON, self.on_save_button, self._saveButton)
        self._pnl.Bind(wx.EVT_BUTTON, self.on_load_button, self._loadButton)

    def on_delete_button(self, event):
        pass

    def on_add_button(self, event):
        person_id = self.generate_id()
        self._people[person_id] = {'FirstName': "Name", 'LastName': "Surname"}

        self.set_person_details_fields(self._people[person_id], person_id)
        self.add_person_to_list(self._people[person_id]['FirstName'],
                                self._people[person_id]['LastName'])

    def on_update_button(self, event):
        pass

    def on_save_button(self, event):
        pass

    def on_load_button(self, event):
        pass

    def add_person_to_list(self, firstName, lastName):
        self._peopleList.Append([firstName, lastName])

    def set_person_details_fields(self, person, personId):
        self._idEditId.SetValue(str(personId))
        if 'FirstName' in person:
            self._firstNameEditId.SetLabelText(person['FirstName'])
        if 'MiddleName' in person:
            self._middleNameEditId.SetLabelText(person['MiddleName'])
        if 'LastName' in person:
            self._lastNameEditId.SetLabelText(person['LastName'])
        if 'Email' in person:
            self._emailEditId.SetLabelText(person['Email'])
        if 'Phone' in person:
            self._phoneEditId.SetLabelText(person['Phone'])

    def generate_id(self):
        while True:
            num = random.randrange(0, 99999999)
            if num not in self._people.keys():
                return num

if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = PeopleDatabase(None, title='peopleFinder', size=wx.Size(627, 350))
    frm.Show()
    app.MainLoop()

