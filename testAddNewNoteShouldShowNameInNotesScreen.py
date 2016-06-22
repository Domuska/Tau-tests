# -*- coding: utf-8 -*-

class NotesTests(UITestCase):
    
    
    def setUp(self):
        #launch.app('com.nononsenseapps.notepad/.activities.ActivityList')
        launch.activity('com.nononsenseapps.notepad', '.activities.ActivityList')
        
        global taskListName
        taskListName = 'a random task list'
        
        global noteName1 
        noteName1 = 'prepare food'
        
        
    #def tearDown(self):
        #kill('com.nononsenseapps.notepad')
        #packages.clearData('com.nononsenseapps.notepad')
        
        

    @testCaseInfo('<Add a new note>', deviceCount=1)
    def testAddNewNoteShouldShowNameInNotesScreen(self):
        """ Insert brief description of the test case

            1. Close the navigation drawer
            2. Tap on the fab
            3. Enter the name for the note and close the note
            4. Verify that the note is in the list
           
        """
        # goto('Notes')
        log('Step1: Insert test step description')
        #tap.description('Apps')
        #tap.description('Notes')
        swipe.description('List of tasks').to.location((0, 0.5))
        tap.description('Floating action button')
        tap.text('Note')
        input.text('prepare food')
        tap.description('Navigate up')
        verify.text('prepare food', scroll=True)
        

    @testCaseInfo('<Add new notelist>', deviceCount=1)
    def testAddTaskListCheckItIsAddedToDrawer(self):
        """
            1. do stuff
        """
        #goto('Notes')
        #tap.description('Apps')
        #tap.description('Notes')
        #tap.description('List of tasks')
        #tap.description('Apps')
        #tap.description('Notes')
        tap.text('Create new')
        input.text('a random tasklist')
        tap.text('OK')
        tap.description('Open navigation drawer')
        verify.text('a random tasklist', scroll=True)
        
    @testCaseInfo('<Add note to tasklist>', deviceCount=1)
    def testAddNoteToTaskList(self):
        """
            1. do stuff
        """
        tap.text('Create new')
        tap.resourceId('com.nononsenseapps.notepad:id/titleField')
        input.text(taskListName)
        tap.resourceId('com.nononsenseapps.notepad:id/dialog_yes')
        
        tap.description('Open navigation drawer')
        tap.text(taskListName)
        self.createNoteWithName(noteName1)
        self.navigateUp()
        #tap.description('Floating action button')
        #tap.text('Note')
        #input.text(noteName1)
        #tap.description('Navigate up')
        verify.text(noteName1, scroll=True)
        self.openDrawer()
        verify.text('1', scroll=True)
        
    @testCaseInfo('<Add note and add reminder date>', deviceCount=1)
    def testAddNewNoteWithReminderDateAndTime(self):
        """
            1. add new note
            2. add reminder date and time
            3. open note and verify the date is visible        
        """
        #swipe.location((0.09, 0.1)).to.location((0.07, 0.1))
        #swipe.location((0.09, 0.1)).to.location((0.07, 0.1))
        #swipe.description('List of tasks').to.location((0, 0.47))
        self.closeDrawer()
        
        self.createNoteWithName(noteName1)
        
        tap.resourceId("com.nononsenseapps.notepad:id/notificationAdd")
        
        #add date
        tap.resourceId("com.nononsenseapps.notepad:id/notificationDate")
        tap.resourceId("com.nononsenseapps.notepad:id/done")
        
        #add time
        tap.resourceId("com.nononsenseapps.notepad:id/notificationTime")
        tap.resourceId("com.nononsenseapps.notepad:id/done_button")
        
        self.navigateUp()
        
        tap.text(noteName1)
        
        #verify current month and date
        exists.resourceId('com.nononsenseapps.notepad:id/notificationDate', scroll=True)
        #verify.text('June 22', scroll=True)
        
    def createNoteWithName(self, noteName):
        tap.resourceId("com.nononsenseapps.notepad:id/fab")
        tap.resourceId("com.nononsenseapps.notepad:id/taskText")
        input.text(noteName)
        
    def closeDrawer(self):
        swipe.description('List of tasks').to.location((0, 0.5))
    
    def openDrawer(self):
        tap.description('Open navigation drawer')
        
    def navigateUp(self):
        tap.description('Navigate up')
        
        
