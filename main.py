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

class PeopleDatabase(wx.Frame):
    """
    """
    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(PeopleDatabase, self).__init__(*args, **kw)

        # create a panel in the frame
        self._pnl = wx.Panel(self)

        # create a People area
        self._peopleStaticBox = wx.StaticBox(self._pnl, wx.ID_ANY, "People",
                                             size=wx.Size(200, 250))
        # people list
        self._peopleList = wx.ListCtrl(self._pnl, size=wx.Size(200, 250))

        # create Person Details area
        self._personDetBox = wx.StaticBox(self._pnl, wx.ID_ANY, "Person Details",
                            pos=wx.Point(210, 0), size=wx.Size(400, 250))

        # ID
        wx.StaticText(self._pnl, label="ID", pos=(220, 25))
        self._idEditId = wx.TextCtrl(self._pnl, pos=(300, 20), size=(300, 25),
                             style=wx.TE_READONLY)

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

        # Add button
        self._addButton = wx.Button(self._pnl, label="Add", pos=(210, 255))

        # Update button
        self._updateButton = wx.Button(self._pnl, label="Update", pos=(300, 255))

        # Save button
        self._saveButton = wx.Button(self._pnl, label="Save", pos=(430, 255))

        # Load button
        self._loadButton = wx.Button(self._pnl, label="Load", pos=(520, 255))

        # and a status bar
        self.CreateStatusBar()
        self.SetStatusText("ver 1.1")

        # Add events to the buttons
        self._pnl.Bind(wx.EVT_BUTTON, self._OnDeleteButton, self._deleteButton)
        self._pnl.Bind(wx.EVT_BUTTON, self._OnAddButton, self._addButton)
        self._pnl.Bind(wx.EVT_BUTTON, self._OnUpdateButton, self._updateButton)
        self._pnl.Bind(wx.EVT_BUTTON, self._OnSaveButton, self._saveButton)
        self._pnl.Bind(wx.EVT_BUTTON, self._OnLoadButton, self._loadButton)


    def _OnDeleteButton(self, event):
        pass


    def _OnAddButton(self, event):
        pass


    def _OnUpdateButton(self, event):
        pass


    def _OnSaveButton(self, event):
        pass


    def _OnLoadButton(self, event):
        pass

if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = PeopleDatabase(None, title='peopleFinder', size=wx.Size(627, 350))
    frm.Show()
    app.MainLoop()