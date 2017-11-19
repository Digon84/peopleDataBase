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
import re
import sys
import traceback
import wx.lib.agw.genericmessagedialog as GMD

def MyExceptionHook(etype, value, trace):
    frame = wx.GetApp().GetTopWindow()
    tmp = traceback.format_exception(etype, value, trace)
    exception = "".join(tmp)

    dlg = ExceptionDialog(exception)
    dlg.ShowModal()
    dlg.Destroy()

    frame.Destroy()


class ExceptionDialog(GMD.GenericMessageDialog):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self, msg):
        """Constructor"""
        GMD.GenericMessageDialog.__init__(self, None, msg, "Exception!",
                                          wx.OK | wx.ICON_ERROR)


class PeopleDatabase(wx.Frame):
    """
    """
    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(PeopleDatabase, self).__init__(*args, **kw)
        sys.excepthook = MyExceptionHook
        self._people = {}
        self._contentNotSaved = False

        # create a panel in the frame
        self._pnl = wx.Panel(self)

        # create a People area
        #TODO: BUG - spelling People -> Peaple
        self._peopleStaticBox = wx.StaticBox(self._pnl, wx.ID_ANY, "Peaple",
                                             size=wx.Size(200, 250))
        # people list
        self._peopleList = wx.ListCtrl(self._pnl, size=wx.Size(190, 225),
                                       pos=wx.Point(5, 20),
                                       style=wx.LC_REPORT | wx.LC_SINGLE_SEL)
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
        #TODO: BUG - Mail right-justified
        self._emailEditId = wx.TextCtrl(self._pnl, pos=(300, 180), size=(300, 25), style = wx.TE_RIGHT)

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
        self.SetStatusText("ver 1.22")

        # Add events to the buttons
        self._pnl.Bind(wx.EVT_BUTTON, self.on_delete_button, self._deleteButton)
        self._pnl.Bind(wx.EVT_BUTTON, self.on_add_button, self._addButton)
        self._pnl.Bind(wx.EVT_BUTTON, self.on_update_button, self._updateButton)
        self._pnl.Bind(wx.EVT_BUTTON, self.on_save_button, self._saveButton)
        self._pnl.Bind(wx.EVT_BUTTON, self.on_load_button, self._loadButton)

        # Add events on the textCtrls
        self._pnl.Bind(wx.EVT_TEXT, self.on_text_change, self._firstNameEditId)
        self._pnl.Bind(wx.EVT_TEXT, self.on_text_change, self._middleNameEditId)
        self._pnl.Bind(wx.EVT_TEXT, self.on_text_change, self._lastNameEditId)
        self._pnl.Bind(wx.EVT_TEXT, self.on_text_change, self._emailEditId)
        #TODO: BUG - When updating phone field update button will not get enabled

        # Add event to the list
        self._pnl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.on_select, self._peopleList)

        # Add on close event
        self.Bind(wx.EVT_CLOSE, self.on_close)

    def on_delete_button(self, event):
    #    #TODO: BUG - delete only item from list and not from variable
    #    selected = self._peopleList.GetFirstSelected()
    #    self._peopleList.DeleteItem(selected)
    #    # set first as selected
    #    self._peopleList.Focus(0)
    #    self._peopleList.Select(0)
        pass


    def on_add_button(self, event):
        person_id = self.generate_id()
        self._people[person_id] = {'FirstName': "Name", 'LastName': "Surname"}

        self.set_person_details_fields(self._people[person_id], person_id)
        self.add_person_to_list(self._people[person_id]['FirstName'],
                                self._people[person_id]['LastName'])
        #TODO: BUG - on add all person details should be cleared
        self._people[person_id]["OnList"] = self._peopleList.GetItemCount() - 1

        self._peopleList.Focus(self._peopleList.GetItemCount() - 1)
        self._peopleList.Select(self._peopleList.GetItemCount() - 1)

        self._addButton.Disable()
        self._updateButton.Enable()
        #TODO: BUG - save should be also disabled or it will cause crash
        #       when saving without updating (no **Name field KeyError)

    def on_update_button(self, event):
        person_id = int(self._idEditId.GetValue())
        self._people[person_id]['FirstName'] = self._firstNameEditId.GetValue()
        self._people[person_id]['MiddleName'] = self._middleNameEditId.GetValue()
        self._people[person_id]['LastName'] = self._lastNameEditId.GetValue()
        self._people[person_id]['Email'] = self._emailEditId.GetValue()
        self._people[person_id]['Phone'] = self._phoneEditId.GetValue()

        selected = self._peopleList.GetFirstSelected()
        self._peopleList.SetStringItem(selected, 0, self._firstNameEditId.GetValue())
        self._peopleList.SetStringItem(selected, 1, self._lastNameEditId.GetValue())

        self._updateButton.Disable()
        self._addButton.Enable()
        self._saveButton.Enable()
        self._contentNotSaved = True
        pass

    def on_save_button(self, event):
        with wx.FileDialog(self, "Save pdb file", wildcard="pdb files (*.pdb)|*.pdb",
                           style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:
            # otherwise ask the user what new file to open
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return  # the user changed their mind

            # save the current contents in the file
            pathname = fileDialog.GetPath()
            try:
                with open(pathname, 'w') as file:
                    self.do_save_data(file)
                    self._saveButton.Disable()
                    self._contentNotSaved = False
            except IOError:
                wx.LogError("Cannot save current data in file '%s'." % pathname)
            pass

    def on_load_button(self, event):
    #    if self._contentNotSaved:
    #        if wx.MessageBox("Current content has not been saved! Proceed?", "Please confirm",
    #                         wx.ICON_QUESTION | wx.YES_NO, self) == wx.NO:
    #            return

    #            # otherwise ask the user what new file to open
    #    with wx.FileDialog(self, "Open pdb file", wildcard="pdb files (*.pdb)|*.pdb",
    #                       style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:

    #        if fileDialog.ShowModal() == wx.ID_CANCEL:
    #            return  # the user changed their mind

    #        # Proceed loading the file chosen by the user
    #        pathname = fileDialog.GetPath()
    #        try:
    #            with open(pathname, 'r') as file:
    #                #TODO: BUG - will crash when opening empty file ;)
    #                self.do_load_data(file)
    #                self.set_new_data()
    #                # set first selected as default
    #                self._peopleList.Focus(0)
    #                self._peopleList.Select(0)
    #                # Update button will get enabled after loading data
    #                # we don't want that
    #                self._updateButton.Disable()
    #        except IOError:
    #            wx.LogError("Cannot open file '%s'." % pathname)
        pass

    def on_select(self, event):
        selected_item = self._peopleList.GetFirstSelected()
        for person_id in self._people.keys():
            if selected_item == self._people[person_id]["OnList"]:
                self.set_person_details_fields(self._people[person_id], person_id)
                break

    def add_person_to_list(self, firstName, lastName):
        self._peopleList.Append([firstName, lastName])

    def set_person_details_fields(self, person, personId):
        self._idEditId.SetValue(str(personId))
        if 'FirstName' in person:
            self._firstNameEditId.SetValue(person['FirstName'])
        if 'MiddleName' in person:
            self._middleNameEditId.SetValue(person['MiddleName'])
        if 'LastName' in person:
            self._lastNameEditId.SetValue(person['LastName'])
        if 'Email' in person:
            self._emailEditId.SetValue(person['Email'])
        if 'Phone' in person:
            self._phoneEditId.SetValue(person['Phone'])

    def generate_id(self):
        while True:
            #TODO: BUG - up to 9 digits per ID, should be 8
            num = random.randrange(100000000, 999999999)
            if num not in self._people.keys():
                return num

    def print_people_details(self):
        for id in self._people.keys():
            print(id)
            print(self._people[id]['FirstName'])
            print(self._people[id]['MiddleName'])
            print(self._people[id]['LastName'])
            print(self._people[id]['Email'])
            print(self._people[id]['Phone'])

    def do_save_data(self, file):
        for id in self._people.keys():
            file.write("%s**%s**%s**%s**%s**%s**\n"
                       % (str(id), self._people[id]['FirstName'],
                       self._people[id]['MiddleName'],
                       self._people[id]['LastName'],
                       self._people[id]['Email'],
                       self._people[id]['Phone']))

    def do_load_data(self, file):
        self._people = {}
        for line in file:
            lineSplit = re.split("\*\*", line, 6)
            #TODO: BUG - last and first name swapped
            [id, lastName, middleName, firstName, email, phone, _] = lineSplit
            self._people[id] = {}
            self._people[id]['FirstName'] = firstName
            self._people[id]['MiddleName'] = middleName
            self._people[id]['LastName'] = lastName
            self._people[id]['Email'] = email
            self._people[id]['Phone'] = phone

    def set_new_data(self):
        self._peopleList.DeleteAllItems()
        # TODO: BUG - fields will remember all data, its needed to clear also
        # details fields
        onList = 0
        for persons_id in self._people.keys():
            self.add_person_to_list(self._people[persons_id]["FirstName"],
                                    self._people[persons_id]["LastName"])
            self._people[persons_id]["OnList"] = onList
            onList = onList + 1

    def on_text_change(self, event):
        #TODO: BUG - when ID is empty (starting application without data) changing other fields
        #will make update button enabled. That can cause a crash when pressing it (no items on list)
        self._updateButton.Enable()

    def on_close(self, event):
        if event.CanVeto() and self._contentNotSaved:

            if wx.MessageBox("The file has not been saved... continue closing?",
                             "Please confirm",
                             wx.ICON_QUESTION | wx.YES_NO) != wx.YES:
                event.Veto()
                return

        self.Destroy()  # you may also do:  event.Skip()
        # since the default event handler does call Destroy(), too


if __name__ == '__main__':
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
    app = wx.App()
    frm = PeopleDatabase(None, title='peopleFinder', size=wx.Size(627, 350))
    frm.Show()
    app.MainLoop()


