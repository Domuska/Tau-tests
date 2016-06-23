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
        date_fourth = "04" + currentMonthAndYear
        date_fifth = "05" + currentMonthAndYear
        date_fifteenth = "15" + currentMonthAndYear
        date_twentythird = "23" + currentMonthAndYear
        
        #initialize the notes in right order
        notes_correct_order = [noteName2, noteName1, noteName4, noteName3]
        
        
        self.closeDrawer()
        
        # create first note
        self.createNoteWithName(noteName1)
        tap.resourceId('com.nononsenseapps.notepad:id/dueDateBox')
        tap.description(date_fifth)
        tap.resourceId('com.nononsenseapps.notepad:id/done')
        self.navigateUp()
        
        #create second note
        self.createNoteWithName(noteName2)
        tap.resourceId('com.nononsenseapps.notepad:id/dueDateBox')
        tap.description(date_fourth)
        tap.resourceId('com.nononsenseapps.notepad:id/done')
        self.navigateUp()
        
        #third note
        self.createNoteWithName(noteName3)
        tap.resourceId('com.nononsenseapps.notepad:id/dueDateBox')
        tap.description(date_twentythird)
        tap.resourceId('com.nononsenseapps.notepad:id/done')
        self.navigateUp()
        
        #fourth note
        self.createNoteWithName(noteName4)
        tap.resourceId('com.nononsenseapps.notepad:id/dueDateBox')
        tap.description(date_fifteenth)
        tap.resourceId('com.nononsenseapps.notepad:id/done')
        self.navigateUp()
        
        #order the notes
        tap.resourceId('com.nononsenseapps.notepad:id/menu_sort')
        tap.text('Order by due date')
        
        note2_right_place = find.text(noteName2, index=0)
        note1_right_place = find.text(noteName1, index=1)
        note4_right_place = find.text(noteName4, index=2)
        note3_right_place = find.text(noteName3, index=3)
        
        
        notes = get.items.instanceOf('android.widget.TextView', \
        description='Item title')
        note_names = []
        
        #get actual note names
        for note in notes:
            note_names.append(note.Text)
        
        #check that notes are in right order
        if not (notes_correct_order == note_names):
            log("correct order of notes:")
            log(notes_correct_order)
            log("order gotten:")
            log(note_names)
            fail("notes in wrong order")
            
            
    @testCaseInfo('<Add a new task list and delete it>', deviceCount=1)
    def testCreateTaskListAndDeleteIt(self):
        """
            1. create new task list
            2. delete it
            3. assert that the task list is not visible
        """
        
        #create the task list
        tap.text('Create new')
        tap.resourceId('com.nononsenseapps.notepad:id/titleField')
        input.text(taskListName)
        tap.resourceId('com.nononsenseapps.notepad:id/dialog_yes')
        
        #delete the task list
        tap.description('Open navigation drawer')
        tap.long.text(taskListName)
        tap.resourceId('com.nononsenseapps.notepad:id/deleteButton')
        tap.text('OK')
        
        #assert it is not visible
        textViews = get.items.instanceOf('android.widget.TextView', \
            resourceId='android:id/text1')
            
        for item in textViews:
            log(item)
            if item.Text == taskListName:
                fail("task list is still in the list")
        
    
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
        
        
