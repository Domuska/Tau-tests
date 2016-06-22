# -*- coding: utf-8 -*-
import time
class NotesTests(UITestCase):
    
    
    def setUp(self):
        #launch.app('com.nononsenseapps.notepad/.activities.ActivityList')
        launch.activity('com.nononsenseapps.notepad', '.activities.ActivityList')
        
        global taskListName
        taskListName = "a random task list"
        
        global noteName1 
        noteName1 = "prepare food"
        
        global noteName2
        noteName2 = "take dogs out"
        
        global noteName3
        noteName3 = "water plants"
        
        global noteName4
        noteName4 = "sleep"
        
        
        
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
        
        #verify month is shown
        found = find.resourceId('com.nononsenseapps.notepad:id/notificationDate', scroll=True)
        
        if not found:
            fail("month is not visible even though reminder was added")
        
    @testCaseInfo('<Add note with due date>', deviceCount=1)
    def testAddNewNoteWithDueDateCheckDateIsVisible(self):
        """
            1. add new note
            2. check that due date is visible in list
        """
        self.closeDrawer()
        
        self.createNoteWithName(noteName1)
        tap.resourceId('com.nononsenseapps.notepad:id/dueDateBox')
        tap.resourceId('com.nononsenseapps.notepad:id/done')
        
        self.navigateUp()
        
        
        found = find.resourceId('com.nononsenseapps.notepad:id/date', scroll=True)
        
        if not found:
            fail("due date is not visible!")

        
    @testCaseInfo('<Add note and delete it>', deviceCount=1)
    def testCreateNoteAndDeleteIt(self):
        """
            1. add new note
            2. delete it
            3. verify it's not in the list any more
        """
        
        self.closeDrawer()
        self.createNoteWithName(noteName1)
        self.navigateUp()
        tap.text(noteName1)
        
        tap.resourceId('com.nononsenseapps.notepad:id/menu_delete')
        tap.resourceId('android:id/button1')
        
        found = find.text(noteName1, index=1, scroll=True)
        
        if found:
            fail("note found, was not deleted properly!")
        
        
    @testCaseInfo('<Add notes and order by due date>', deviceCount=1)
    def testAddNotesOrderByDueDate(self):
        """
            1. add notes with due dates
            2. sort by due date
            3. check that notes sorted correctly
            
        """
        
        # initialize the strings that are used with content descriptions
        # could maybe use regexes for those too but this works
        currentMonthAndYear = \
        " " +  time.strftime("%B") + " " + time.strftime("%Y")
        firstDate = "04" + currentMonthAndYear
        secondDate = "05" + currentMonthAndYear
        thirdDate = "15" + currentMonthAndYear
        fourthDate = "23" + currentMonthAndYear
        
        
        self.closeDrawer()
        
        # create first note
        self.createNoteWithName(noteName1)
        tap.resourceId('com.nononsenseapps.notepad:id/dueDateBox')
        tap.description(secondDate)
        tap.resourceId('com.nononsenseapps.notepad:id/done')
        self.navigateUp()
        
        #create second note
        self.createNoteWithName(noteName2)
        tap.resourceId('com.nononsenseapps.notepad:id/dueDateBox')
        tap.description(firstDate)
        tap.resourceId('com.nononsenseapps.notepad:id/done')
        self.navigateUp()
        
        #third note
        self.createNoteWithName(noteName3)
        tap.resourceId('com.nononsenseapps.notepad:id/dueDateBox')
        tap.description(fourthDate)
        tap.resourceId('com.nononsenseapps.notepad:id/done')
        self.navigateUp()
        
        #fourth note
        self.createNoteWithName(noteName4)
        tap.resourceId('com.nononsenseapps.notepad:id/dueDateBox')
        tap.description(thirdDate)
        tap.resourceId('com.nononsenseapps.notepad:id/done')
        self.navigateUp()
        
        #order the notes
        tap.resourceId('com.nononsenseapps.notepad:id/menu_sort')
        tap.text('Order by due date')
        
        note2_right_place = find.text(noteName2, index=0)
        note1_right_place = find.text(noteName1, index=1)
        note4_right_place = find.text(noteName4, index=2)
        note3_right_place = find.text(noteName3, index=3)
        
        
        """
        this doesnt actually work like this.
        we are with the note names and every time we search
        for a note it has an index of 0 since its the first of
        that kind of element that is found. we need to search
        with maybe the ID of the elements and check that the found
        elements are then in order, 
        """
        if not note1_right_place:
            fail("first note in wrong place")
            
        if not note2_right_place:
            fail("second note in wrong place")
            
        if not note3_right_place:
            fail("third note in wrong place")
            
        if not note4_right_place:
            fail("fourth note in wrong place")
        
        
    
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
        
        
