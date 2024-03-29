import wx
import wx.xrc
import Wu_Davison_SyntacticCloaking_HOTSdata as cloak

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 700,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 700,400 ), wx.Size( 700,400 ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer1.SetMinSize( wx.Size( 700,400 ) ) 
		self.tabs = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cloakingTab = wx.ScrolledWindow( self.tabs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.cloakingTab.SetScrollRate( 5, 5 )
		self.cloakingTab.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		self.cloakingTab.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVEBORDER ) )
		self.cloakingTab.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText3 = wx.StaticText( self.cloakingTab, wx.ID_ANY, u"Enter Threshold", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		self.m_staticText3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_staticText3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
		
		bSizer2.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self.cloakingTab, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		self.m_textCtrl2.SetMinSize( wx.Size( 120,-1 ) )
		self.m_textCtrl2.SetMaxSize( wx.Size( 120,-1 ) )
		
		bSizer2.Add( self.m_textCtrl2, 0, wx.ALL, 5 )
		
		self.m_button5 = wx.Button( self.cloakingTab, wx.ID_ANY, u"Find URLs", wx.DefaultPosition, wx.Size( 120,30 ), 0 )
		self.m_button5.SetMinSize( wx.Size( 120,30 ) )
		self.m_button5.SetMaxSize( wx.Size( 120,30 ) )
		
		bSizer2.Add( self.m_button5, 0, wx.ALL, 5 )
		
		self.m_listCtrl1 = wx.ListBox( parent=self.cloakingTab, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size( 600,200 ))
		
		self.m_listCtrl1.SetMinSize( wx.Size( 600,200 ) )
		self.m_listCtrl1.SetMaxSize( wx.Size( 600,200 ) )
		
		bSizer2.Add( self.m_listCtrl1, 0, wx.ALL, 5 )
		
		
		self.cloakingTab.SetSizer( bSizer2 )
		self.cloakingTab.Layout()
		bSizer2.Fit( self.cloakingTab )
		self.tabs.AddPage( self.cloakingTab, u"CloakingDetection", False )
		self.ContentAnalysis = wx.ScrolledWindow( self.tabs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.ContentAnalysis.SetScrollRate( 5, 5 )
		self.ContentAnalysis.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		self.ContentAnalysis.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVEBORDER ) )
		self.ContentAnalysis.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
		
		bSizer22 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText32 = wx.StaticText( self.ContentAnalysis, wx.ID_ANY, u"Enter Threshold", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )
		self.m_staticText32.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_staticText32.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
		
		bSizer22.Add( self.m_staticText32, 0, wx.ALL, 5 )
		
		self.m_textCtrl22 = wx.TextCtrl( self.ContentAnalysis, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		self.m_textCtrl22.SetMinSize( wx.Size( 120,-1 ) )
		self.m_textCtrl22.SetMaxSize( wx.Size( 120,-1 ) )
		
		bSizer22.Add( self.m_textCtrl22, 0, wx.ALL, 5 )
		
		self.m_button52 = wx.Button( self.ContentAnalysis, wx.ID_ANY, u"Find URLs", wx.DefaultPosition, wx.Size( 120,30 ), 0 )
		self.m_button52.SetMinSize( wx.Size( 120,30 ) )
		self.m_button52.SetMaxSize( wx.Size( 120,30 ) )
		
		bSizer22.Add( self.m_button52, 0, wx.ALL, 5 )
		
		self.m_listCtrl12 = wx.ListBox( parent=self.ContentAnalysis, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size( 600,200 ))
		
		self.m_listCtrl12.SetMinSize( wx.Size( 600,200 ) )
		self.m_listCtrl12.SetMaxSize( wx.Size( 600,200 ) )
		
		bSizer22.Add( self.m_listCtrl12, 0, wx.ALL, 5 )
		
		
		self.ContentAnalysis.SetSizer( bSizer22 )
		self.ContentAnalysis.Layout()
		bSizer22.Fit( self.ContentAnalysis )
		self.tabs.AddPage( self.ContentAnalysis, u"ContentAnalysis(NA)", True )
		self.LinkAnalysis = wx.ScrolledWindow( self.tabs, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.LinkAnalysis.SetScrollRate( 5, 5 )
		self.LinkAnalysis.SetFont( wx.Font( 10, 70, 90, 90, False, wx.EmptyString ) )
		self.LinkAnalysis.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVEBORDER ) )
		self.LinkAnalysis.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
		
		bSizer21 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText31 = wx.StaticText( self.LinkAnalysis, wx.ID_ANY, u"Enter Threshold", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )
		self.m_staticText31.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_staticText31.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
		
		bSizer21.Add( self.m_staticText31, 0, wx.ALL, 5 )
		
		self.m_textCtrl21 = wx.TextCtrl( self.LinkAnalysis, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		self.m_textCtrl21.SetMinSize( wx.Size( 120,-1 ) )
		self.m_textCtrl21.SetMaxSize( wx.Size( 120,-1 ) )
		
		bSizer21.Add( self.m_textCtrl21, 0, wx.ALL, 5 )
		
		self.m_button51 = wx.Button( self.LinkAnalysis, wx.ID_ANY, u"Find URLs", wx.DefaultPosition, wx.Size( 120,30 ), 0 )
		self.m_button51.SetMinSize( wx.Size( 120,30 ) )
		self.m_button51.SetMaxSize( wx.Size( 120,30 ) )
		
		bSizer21.Add( self.m_button51, 0, wx.ALL, 5 )
		
		self.m_listCtrl11 = wx.ListBox( parent=self.LinkAnalysis, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size( 600,200 ))
		
		self.m_listCtrl11.SetMinSize( wx.Size( 600,200 ) )
		self.m_listCtrl11.SetMaxSize( wx.Size( 600,200 ) )
		
		bSizer21.Add( self.m_listCtrl11, 0, wx.ALL, 5 )
		
		
		self.LinkAnalysis.SetSizer( bSizer21 )
		self.LinkAnalysis.Layout()
		bSizer21.Fit( self.LinkAnalysis )
		self.tabs.AddPage( self.LinkAnalysis, u"LinkAnalysis(NA)", False )
		
		bSizer1.Add( self.tabs, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button5.Bind( wx.EVT_BUTTON, self.onCloakingPressed )
		self.m_button52.Bind( wx.EVT_BUTTON, self.onContentPresses )
		self.m_button51.Bind( wx.EVT_BUTTON, self.onLinkPressed )

                self.Show()    
	
	def __del__( self ):
		pass
	
	# Virtual event handlers, overide them in your derived class
	def onCloakingPressed( self, event ):
	    if self.m_textCtrl2.GetValue()==wx.EmptyString:
	        print "Please specify a threshold"
	        return
	    self.m_listCtrl1.Append("Please wait for a couple of minutes...")    
	    cloak.calc(self.m_textCtrl2.GetValue())
	    self.m_listCtrl1.Clear()
	    with open("CloakedPages.txt","r") as f:
	        for row in f:
	            self.m_listCtrl1.Append(row)
	    return
	
	def onContentPresses( self, event ):
		event.Skip()
	
	def onLinkPressed( self, event ):
		event.Skip()
		
app = wx.App(False)
 
#create an object of CalcFrame
frame = MyFrame1(None)
#show the frame
frame.Show(True)
#start the applications
app.MainLoop()
